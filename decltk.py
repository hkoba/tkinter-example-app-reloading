#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Tkinter with declarative manner

from tkinter import *

import importlib
import os
import sys

def Reload(filename: str):
    bn = os.path.basename(filename)
    (modName, _x) = os.path.splitext(bn)
    mod = sys.modules[modName]
    return importlib.reload(mod)

def Packed(widget: Widget, **kwargs):
    widget.pack(**kwargs)
    return widget

#
# ttk.Label(frm, text="Hello World!")
# =>
# Widget(frm, 'lab1', ttk.Label, text="Hello World!")
#
def Widget(parent: Widget, elName: str, type, **kwargs):
    if parent._w == '.':
        pathName = '.' + elName
    else:
        pathName = parent._w + '.' + elName
    # print(pathName)
    if parent.tk.getint(parent.tk.call('winfo', 'exists', pathName)):
        w = parent.children[elName]
        w.configure(**kwargs)
        return w
    else:
        return type(parent, name=elName, **kwargs)
