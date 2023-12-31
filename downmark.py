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
            ("<<NotebookTabChanged>>", self.onTabChanged),
            ("<<childBorn>>", self.onChildBorn)
        ]
        
        for e,f in binds:
            self.notebook.bind_all(e, f)

    def onChildBorn(self, event):
        childTitle = 'CHILD'
        newFrame = ttk.Frame(self.notebook)
        textWidget = self.createTextTab(newFrame, childTitle)
        
        self.tabs[newFrame] = textWidget
        self.notebook.add(newFrame, text=childTitle)

        self.notebook.select(newFrame)
        textWidget.textWidget.focus_set()

    def onTabChanged(self, event):
        self.getCurrentText().focus_set()
    
    def getCurrentFrame(self):
        nb = self.notebook
        frameName = nb.select()
        return nb.nametowidget(frameName)
    
    def getCurrentText(self):
        return self.tabs[self.getCurrentFrame()].textWidget

    def loadTabs(self):
        tabTitles = ["0"]

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
            self.parent = parent
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
            self.textWidget.tag_configure("light", foreground='#808080')    

        def applyTagToRange(self, tag, left, right):
            self.textWidget.tag_add(tag, left, right)
        
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
            if event.char == ']':
                self.linkScan(event)
                
        def linkScan(self, event):
            right = self.textWidget.index("insert")
            left = right
            breakChars = [']', '\n']

            while left != '1.0':
                left = self.textWidget.index(f"{left}-1c")
                char = self.textWidget.get(left)
                
                if char == '[':
                    return self.handleLink(left, right)
                if char in breakChars:
                    return

        def handleLink(self, left, right):
            self.applyTagToRange("light", f"{left}+1c", right)
            
            root.event_generate("<<childBorn>>")
        
        def setEnableState(self, newState):
            self.textWidget['state'] = {True: 'normal', False: 'disabled'}[newState]
            self.enabled = newState
        
        def toggleReadOnly(self, event):
            toggleState = not self.enabled
            self.setEnableState(toggleState)     

def launchDownmark():
    global root
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
