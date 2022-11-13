#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import importlib
import os
import sys

print("Hello!")

def Reload():
    print("Hello again!")
    if __name__ == "__main__":
        raise Exception("Can't use reload feature in toplevel module!")
    bn = os.path.basename(__file__)
    (modName, _x) = os.path.splitext(bn)
    mod = sys.modules[modName]
    # print(mod)
    # x globalx()
    # x locals()
    importlib.reload(mod)

def Packed(widget, **kwargs):
    widget.pack(**kwargs)
    widget

def Widget(parent, elName, type, **kwargs):
    print("New widget")
    pathName = parent._w + '.' + elName
    print(pathName)
    if parent.tk.getint(parent.tk.call('winfo', 'exists', pathName)):
        w = parent.children[elName]
        w.configure(**kwargs)
        print("configure", elName, kwargs)
        return w
    else:
        return type(parent, name=elName, **kwargs)

def GUI(self):
    print("GUI is called!")
    if __name__ != "__main__":
        self.reload_btn = Packed(Widget(self, 'reload', tk.Button, text="reload", command=Reload))

    self.text = Packed(Widget(self, 'editor', tk.Text, width=120))
    self.pack()

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        GUI(self)

if 'root' not in locals():
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()
else:
    GUI(myapp)
