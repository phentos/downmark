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

    def createTextTab(self, title):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=title)
        
        textWidget = tk.Text(frame, wrap="word", width=40, height=10)
        textWidget.pack(expand=True, fill='both', padx=5, pady=5)
    
        return textWidget

def launchDownmark():
    root = tk.Tk()
    root.title("Downmark")
    global notebook
    notebook = Notebook(root)

    root.mainloop()


th = Thread(target=launchDownmark)
th.start()