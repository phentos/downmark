import tkinter as tk
from tkinter.font import Font

def replace_text_and_style(start, end, new_text, text_widget):
    # Delete the existing text
    text_widget.delete(start, end)

    # Insert new text
    text_widget.insert(start, new_text)

    # Define custom fonts for bold and italic
    bold_font = Font(text_widget, text_widget.cget("font"), weight="bold")
    italic_font = Font(text_widget, text_widget.cget("font"), slant="italic")

    # Configure tags with these fonts
    text_widget.tag_configure("bold", font=bold_font)
    text_widget.tag_configure("italic", font=italic_font)

    # Apply the tags to specific ranges
    # Adjust these indices based on your new text
    text_widget.tag_add("bold", "1.0", "1.4")  # First 4 characters (Bold)
    text_widget.tag_add("italic", "1.9", "1.15")  # Next 6 characters (Italic)

root = tk.Tk()
text_widget = tk.Text(root, wrap="word")
text_widget.pack(expand=True, fill='both')

# Replace text and apply styles
replace_text_and_style("1.0", "1.end", "ASS", text_widget)

root.mainloop()
