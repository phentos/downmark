import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("Nested Notebooks Example")

# Create the main notebook
main_notebook = ttk.Notebook(root)
main_notebook.pack(expand=True, fill='both')

# Create a frame for the first notebook tab
frame_for_nested_notebook = ttk.Frame(main_notebook)
main_notebook.add(frame_for_nested_notebook, text="Nested Notebook")

# Create the nested notebook
nested_notebook = ttk.Notebook(frame_for_nested_notebook)
nested_notebook.pack(expand=True, fill='both')

# Create a frame for the nested notebook tab
frame_for_text_widget = ttk.Frame(nested_notebook)
nested_notebook.add(frame_for_text_widget, text="Text Widget Tab")

# Create a text widget in the nested notebook tab
text_widget = tk.Text(frame_for_text_widget)
text_widget.pack(expand=True, fill='both')

# Start the application
root.mainloop()
