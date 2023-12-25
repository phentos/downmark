import tkinter as tk
from tkinter import ttk

def onTabChanged(event):
    notebook.nametowidget(notebook.select()).winfo_children()[0].focus_set()

root = tk.Tk()

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Creating tabs with text widgets inside frames
for i in range(3):
    frame = ttk.Frame(notebook)
    text_widget = tk.Text(frame)
    text_widget.pack(expand=True, fill='both')
    notebook.add(frame, text=f"Tab {i+1}")

# Bind the event to the function
notebook.bind("<<NotebookTabChanged>>", onTabChanged)

root.mainloop()