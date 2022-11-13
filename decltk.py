#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tkinter with declarative manner

import tkinter as tk

import importlib
import os
import sys

def Reload(filename):
    bn = os.path.basename(filename)
    (modName, _x) = os.path.splitext(bn)
    mod = sys.modules[modName]
    importlib.reload(mod)

def Packed(widget, **kwargs):
    widget.pack(**kwargs)
    widget

#
# ttk.Label(frm, text="Hello World!")
# =>
# Widget(frm, 'lab1', ttk.Label, text="Hello World!")
#
def Widget(parent, elName, type, **kwargs):
    pathName = parent._w + '.' + elName
    # print(pathName)
    if parent.tk.getint(parent.tk.call('winfo', 'exists', pathName)):
        w = parent.children[elName]
        w.configure(**kwargs)
        return w
    else:
        return type(parent, name=elName, **kwargs)
