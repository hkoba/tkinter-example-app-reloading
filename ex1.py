import tkinter as tk
from tkinter import ttk

import decltk

def GUI(self):
    frm = decltk.Widget(self, 'frm', ttk.Frame, padding=10)
    frm.grid()
    decltk.Widget(frm, 'lab1', ttk.Label, text="Hello World!").grid(column=0, row=0)
    decltk.Widget(frm, 'b1',   ttk.Button, text="Quit", command=root.destroy).grid(column=1, row=0)
    decltk.Widget(frm, 'b2',   ttk.Button, text="Reload", command=lambda: decltk.Reload(__file__)).grid(column=0, row=1)

if __name__ == "__main__":
    raise Exception("Reloading of toplevel is not suppoted")

if 'root' not in locals():
    root = tk.Tk()
    GUI(root)
    root.mainloop()
else:
    GUI(root)
