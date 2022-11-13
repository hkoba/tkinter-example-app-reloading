#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Redraw()

    def Redraw(self):
        self.text = tk.Text()
        self.text.pack()
        self.pack()

if __name__ == "__main__":
    root = tk.Tk()
    myapp = App(root)
    myapp.mainloop()
