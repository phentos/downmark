import tkinter as tk
from tkinter import ttk
from threading import Thread

class Notebook:
    def __init__(self, parent):
        self.parent = parent
        self.notebook = self.setupNotebook()
        self.tabs = self.loadTabs()
    
    def loadTabs(self):
        tabTitles = ["Tab 1", "Tab 2"]

        textWidgets = {}
        for title in tabTitles:
            textWidget = self.createTextTab(title)
            textWidgets[title] = textWidget
        
        return textWidgets
    
    def setupNotebook(self):
        notebook = ttk.Notebook(self.parent)
        notebook.pack(expand=True, fill='both')
        
        return notebook        

    class textTab:
        def __init__(self, parent, title):
            self.frame = ttk.Frame(parent)
            parent.add(self.frame, text=title)
            self.textWidget = tk.Text(self.frame, wrap="word", width=40, height=10, undo=True)
            self.textWidget.pack(expand=True, fill='both', padx=5, pady=5)
            self.enabled = True
            self.bindEvents()
        
        def bindEvents(self):
            self.textWidget.bind("<Key>", self.keyPressed)
            self.textWidget.bind("<Control-z>", self.undo)
            self.textWidget.bind("<Escape>", self.toggleReadOnly)
        
        def undo(self):
            self.edit_undo()
        
        def keyPressed(self):
            if self.textWidget.edit_modified(): 
                self.textWidget.edit_separator()
        
        def setEnableState(self, newState):
            self.textWidget['state'] = {True: 'enabled', False: 'disabled'}[newState]
            self.enabled = newState
        
        def toggleReadOnly(self):
            toggleState = not self.enabled
            self.setEnableState(toggleState)
    
    def createTextTab(self, title):
        return self.textTab(self.notebook, title)

def launchDownmark():
    root = tk.Tk()
    root.title("Downmark")
    global notebook
    notebook = Notebook(root)

    root.mainloop()


# th = Thread(target=launchDownmark)
# th.start()
if __name__ == "__main__":
    launchDownmark()