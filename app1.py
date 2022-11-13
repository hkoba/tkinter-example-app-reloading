#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from decltk import *

if __name__ == "__main__":
    raise Exception("Please load as a module!")

#========================================
#
# Change the function GUI below and hit Reload button!
#
def GUI(self):
    print("GUI is called!")
    self.reload_btn = Packed(Widget(self, 'reload', tk.Button,
                                    text="reload", command=self.Reload))

    self.text = Packed(Widget(self, 'editor', tk.Text,
                              width=80))
    self.pack()

#========================================

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        GUI(self)
    def Reload(self):
        Reload(__file__)

if 'root' not in locals():
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()
else:
    GUI(myapp)
