import tkinter as tk
from tkinter import ttk

def addFrame(parent, title):
    newFrame = ttk.Frame(parent)
    parent.add(newFrame, text=title)
    return newFrame

def addNotebook(parent):
    newNotebook = ttk.Notebook(parent)
    newNotebook.pack(expand=True, fill='both')
    return newNotebook

def addText(parent):
    newText = tk.Text(parent)
    newText.pack(expand=True, fill='both')
    return newText


root = tk.Tk()
root.title("Nested Notebooks Example")

main_notebook = addNotebook(root)

# Create a frame for the first notebook tab
frame_for_nested_notebook = addFrame(main_notebook, "Nested Notebook")

# Create the nested notebook
nested_notebook = addNotebook(frame_for_nested_notebook)

# Create a frame for the nested notebook tab
frame_for_text_widget = addFrame(nested_notebook, "Text Widget Tab")

# Create a text widget in the nested notebook tab
text_widget = addText(frame_for_text_widget)

# Start the application
root.mainloop()
