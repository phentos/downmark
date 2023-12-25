import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
        nb = self.notebook
        nb.nametowidget(nb.select()).winfo_children()[0].focus_set()
            
    def loadTabs(self):
        tabTitles = ["Tab 1", "Tab 2"]

        textWidgets = {}
        for title in tabTitles:
            newFrame = ttk.Frame(self.notebook)
            textWidget = self.createTextTab(newFrame, title)
            textWidgets[title] = textWidget
            self.notebook.add(newFrame, text=f"Frame {title}")

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
        
        def setEnableState(self, newState):
            self.textWidget['state'] = {True: 'normal', False: 'disabled'}[newState]
            self.enabled = newState
        
        def toggleReadOnly(self, event):
            toggleState = not self.enabled
            self.setEnableState(toggleState)

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