from tkinter import *
from tkinter import ttk

from decltk  import *

def GUI(self):
    frm = Widget(self, 'frm', ttk.Frame, padding=10)
    frm.grid()
    Widget(frm, 'lab1', ttk.Label, text="Hello World!").grid(column=0, row=0)
    Widget(frm, 'b1',   ttk.Button, text="Quit", command=root.destroy).grid(column=1, row=0)
    Widget(frm, 'b2',   ttk.Button, text="Reload", command=lambda: Reload(__file__)).grid(column=0, row=1)

if 'root' not in locals():
    root = tk.Tk()
    GUI(root)
    root.mainloop()
else:
    GUI(root)
