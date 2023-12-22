import tkinter as tk
from tkinter import ttk

def create_tab(notebook, title, content):
    """ Create a tab with specified title and content. """
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=title)
    label = ttk.Label(frame, text=content, padding=10)
    label.pack(expand=True)

def setup_notebook(parent):
    """ Setup the notebook widget and its tabs. """
    notebook = ttk.Notebook(parent)
    notebook.pack(expand=True, fill='both')
    return notebook

def main():
    """ Main function to create the main window and add tabs. """
    root = tk.Tk()
    root.title("ttk.Notebook Demo")

    notebook = setup_notebook(root)

    # Tab titles and contents can be easily modified or extended
    tabs = [
        ("Tab 1", "This is the first tab"),
        ("Tab 2", "This is the second tab")
    ]

    for title, content in tabs:
        create_tab(notebook, title, content)

    root.mainloop()

if __name__ == "__main__":
    main()
