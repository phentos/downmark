import tkinter as tk
from tkinter import ttk, font, messagebox


from threading import Thread
import sys

class Notebook:
    def __init__(self, parent):
        self.parent = parent
        self.notebook = self.setupNotebook()
        self.tabs = self.loadTabs()
        self.__bindEvents()
    
    def __bindEvents(self):
        binds = [
            ("<<NotebookTabChanged>>", self.onTabChanged)
        ]
        
        for e,f in binds:
            self.notebook.bind(e, f)

    def onTabChanged(self, event):
        self.getCurrentText().focus_set()
    
    def getCurrentFrame(self):
        nb = self.notebook
        frameName = nb.select()
        return nb.nametowidget(frameName)
    
    def getCurrentText(self):
        return self.tabs[self.getCurrentFrame()].textWidget

    def loadTabs(self):
        tabTitles = ["Tab 1", "Tab 2"]

        textWidgets = {}
        for title in tabTitles:
            newFrame = ttk.Frame(self.notebook)
            textWidget = self.createTextTab(newFrame, title)
            textWidgets[newFrame] = textWidget
            self.notebook.add(newFrame, text=title)

        return textWidgets
    
    def setupNotebook(self):
        notebook = ttk.Notebook(self.parent)
        notebook.pack(expand=True, fill='both')
        return notebook        

    def createTextTab(self, frame, title):
        return self.textTab(frame, title)
    
    class textTab:
        def __init__(self, parent, title):
            self.textWidget = tk.Text(parent, wrap="word", width=40, height=10, undo=True)
            self.textWidget.pack(expand=True, fill='both', padx=5, pady=5)
            self.enabled = True
            self.__bindEvents()
            self.buildFonts()
        
        def buildFonts(self):
            boldFont = font.Font(self.textWidget, self.textWidget.cget('font'))
            boldFont.configure(weight="bold")
            self.textWidget.tag_configure("bold", font=boldFont)
            self.textWidget.tag_configure("bluebg", background="blue")
            
        def applyBlueBackgroundToRange(self, left, right):
            self.textWidget.tag_add("bluebg", left, right)
        
        def applyBoldToRange(self, left, right):
            self.textWidget.tag_add("bold", left, right)
        
        def __bindEvents(self):
            binds = [
                ("<Key>", self.anyKeyPressed),
                ("<Control-z>", self.undo),
                ("<Escape>", self.toggleReadOnly),
                ("<Control-w>", self.abandon)
            ]
            
            for e,f in binds:
                self.textWidget.bind(e, f)

        def abandon(self, event):
            if messagebox.askokcancel("Quit", "Really quit?"):
                quit()
        
        def undo(self, event):
            self.textWidget.edit_undo()
        
        def anyKeyPressed(self, event):
            if self.textWidget.edit_modified():
                self.textWidget.edit_separator()
            if event.char == ']' and not self.linkScan(event):
                return 'break'
        
        def linkScan(self, event):
            right = self.textWidget.index("insert")
            left = self.textWidget.search('[', right, backwards=True, stopindex="1.0")
            if left:
                return self.handleLink(left, right)

        def handleLink(self, left, right):
            self.applyBlueBackgroundToRange(left, right)
            return True
        
        def setEnableState(self, newState):
            self.textWidget['state'] = {True: 'normal', False: 'disabled'}[newState]
            self.enabled = newState
        
        def toggleReadOnly(self, event):
            toggleState = not self.enabled
            self.setEnableState(toggleState)
        
        def shiftIndex(self, index, drow=0, dcol=0):
            row, col = (int(_) for _ in index.split('.'))
            row += drow
            col += dcol
            return f"{row}.{col}"            

def launchDownmark():
    root = tk.Tk()
    root.title("Downmark")
    global notebook
    notebook = Notebook(root)

    root.mainloop()

if __name__ == "__main__":
    if "--thread" in sys.argv:
        th = Thread(target=launchDownmark)
        th.start()
    else:
        launchDownmark()