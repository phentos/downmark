import tkinter as tk
from tkinter import font

def apply_styles(text_widget):
    """ Apply bold and italic styles to specific ranges of text. """
    bold_font = font.Font(text_widget, text_widget.cget("font"))
    bold_font.configure(weight="bold")

    italic_font = font.Font(text_widget, text_widget.cget("font"))
    italic_font.configure(slant="italic")

    # Applying bold to a range of text
    text_widget.tag_configure("bold", font=bold_font)
    text_widget.tag_add("bold", "1.0", "1.4")  # Bold from start to 4th character of first line

    # Applying italic to a different range
    text_widget.tag_configure("italic", font=italic_font)
    text_widget.tag_add("italic", "1.5", "1.end")  # Italic from 5th character to end of first line

def main():
    root = tk.Tk()
    root.title("Text Widget with Rich Text")

    text_widget = tk.Text(root, wrap="word", height=10)
    text_widget.pack(expand=True, fill='both', padx=5, pady=5)

    text_widget.insert("1.0", "This is bold and this is italic.")

    apply_styles(text_widget)

    root.mainloop()

if __name__ == "__main__":
    main()
