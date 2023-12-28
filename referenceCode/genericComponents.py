import tkinter as tk
from tkinter import ttk

def addComponent(parent, which, **kwargs):
    componentConstructor = {
        'nb': ttk.Notebook, 
        'frame': ttk.Frame, 
        'text':tk.Text
    }[which]

    newComponent = componentConstructor(parent)
    if which == 'frame':
        title = kwargs.get('title')
        parent.add(newComponent, text=title)
    else:
        newComponent.pack(expand=True, fill='both')
    
    return newComponent

root = tk.Tk()
root.title("Nested Notebooks Example")

rootBook = addComponent(root, 'nb')
rootBookFrame = addComponent(rootBook, 'frame', title="Nested Notebook")
rootBookFrameBook = addComponent(rootBookFrame, 'nb')
rootBookFrameBookFrame = addComponent(rootBookFrameBook, 'frame', title="Text Widget Tab")
rootBookFrameBookFrameText = addComponent(rootBookFrameBookFrame, 'text')

root.mainloop()
