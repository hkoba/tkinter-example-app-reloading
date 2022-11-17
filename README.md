# Please do not try this for now. ~GUI Hot Reloading idiom in tkinter~

(Disclaimer: I'm very new to python. If you find a better way than this, please tell me!)

This is an introduction to my coding idiom to achieve "Hot Reloading" of tkinter GUI. The key function is `Widget()` which has the following signature:

```python
def Widget(parentWidget, elementName, widgetConstructor, **kwargs):
```

See the uses of `decltk.Widget` and `decltk.Reload` in the following code, which is a modified version of <https://docs.python.org/3/library/tkinter.html#a-hello-world-program>:

```python
import tkinter as tk
from tkinter import ttk

import decltk

def GUI(self):
    frm = decltk.Widget(self, 'frm', ttk.Frame, padding=10)
    frm.grid()
    decltk.Widget(frm, 'lab1', ttk.Label, text="Hello World!").grid(column=0, row=0)
    decltk.Widget(frm, 'b1',   ttk.Button, text="Quit", command=root.destroy).grid(column=1, row=0)
    decltk.Widget(frm, 'b2',   ttk.Button, text="Reload", command=lambda: decltk.Reload(__file__)).grid(column=0, row=1)

if 'root' not in locals():
    root = tk.Tk()
    GUI(root)
    root.mainloop()
else:
    GUI(root)

if __name__ == "__main__":
    raise Exception("Reloading of toplevel is not suppoted")
```

You can try above like followings:

```sh
git clone https://github.com/hkoba/tkinter-example-app-reloading.git ex
cd ex
python3
```

Then

```python
import ex1
```

## Basic Idea - Idempotency helps GUI construction code (too)

Constructing a good GUI is difficult, especially if the app becomes larger. It is painful to repeat starting the entire app and navigating to a specific GUI state in non-trivial-sized apps. That is why Hot Reloading matters.

To achieve Hot Reloading of a GUI, you can write a GUI construction function in an idempotent way. With the term "idempotent" here, I mean the GUI construction function returns the same GUI instance when it is invoked several times. Suppose we have a function G which constructs a GUI widget. The first invocation of G should return a new widget. And subsequent invocations of G should return the same widgets, which probably with new properties. In Tcl/Tk, you can write such function easily like below:

```tcl
proc WIDGET {kind name args} {
    if {[winfo exists $name]} {
        $name configure {*}$args
    } else {
        $kind $name {*}$args
    }
    set name
}
```

With the above function `WIDGET`, you can write a GUI which can be reloaded with the "Reload" button.

```tcl
package require Ttk

set frm [WIDGET ttk::frame .frm]
grid $frm

grid [WIDGET ttk::label $frm.lab1 -text "Hello aaa World!"] \
    -column 0 -row 0

grid [WIDGET ttk::button $frm.b1 -text "Quit" \
          -command [list destroy .]] \
    -column 1 -row 0

grid [WIDGET ttk::button $frm.b2 -text "Reload" \
          -command [list source [info script]]] \
    -column 0 -row 1
```

Since tkinter uses Tcl/Tk under the hood, we can implement a similar function. That is `decltk.Widget` in this repo.


## About hkoba

I started Tk with Perl/Tk in the '90s, switched to Tcl/Tk around early 2000, and still been using Tcl/Tk actively.
