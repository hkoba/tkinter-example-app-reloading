#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import importlib
import os
import sys

print("Hello!")

def Reload():
    if __name__ == "__main__":
        raise Exception("Can't use reload feature in toplevel module!")
    bn = os.path.basename(__file__)
    (modName, _x) = os.path.splitext(bn)
    mod = sys.modules[modName]
    # print(mod)
    # x globalx()
    # x locals()
    importlib.reload(mod)

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Redraw()


    def Redraw(self):
        if __name__ != "__main__":
            self.reload_btn = tk.Button(self, text="reload", command=Reload)
            self.reload_btn.pack()
        self.text = tk.Text(self)
        self.text.pack()
        self.pack()

if __name__ == "__main__":
    if 'root' not in locals():
        root = tk.Tk()
        myapp = App(root)
        myapp.mainloop()
