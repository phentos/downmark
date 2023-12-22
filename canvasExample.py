from tkinter import *
from tkinter import ttk

root = Tk()

h, v = ttk.Scrollbar(root, orient=HORIZONTAL), ttk.Scrollbar(root, orient=VERTICAL)

canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)

h['command'], v['command'] = canvas.xview, canvas.yview

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y

def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)        

toBind = [
    ("<Button-1>", xy), 
    ("<B1-Motion>", addLine), 
    ("<B1-ButtonRelease>", doneStroke)
]

toRects = [
    ((10, 10, 30, 30), "red", ('palette', 'palettered')),
    ((10, 35, 30, 55), "blue", ('palette', 'paletteblue')),
    ((10, 60, 30, 80), "black", ('palette', 'paletteblack', 'paletteSelected'))
]

for b,f in toBind:
    canvas.bind(b, f)

for w,f,t in toRects:
    id = canvas.create_rectangle(w, fill=f, tags=t)
    canvas.tag_bind(id, "<Button-1>", lambda x, color=f: setColor(color))

setColor('black')

canvas.itemconfigure('palette', width=5)

root.mainloop()