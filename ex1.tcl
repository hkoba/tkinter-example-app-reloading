#!/usr/bin/wish

proc WIDGET {kind name args} {
    if {[winfo exists $name]} {
        $name configure {*}$args
    } else {
        $kind $name {*}$args
    }
    set name
}

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
