"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.title("Factoring Trinomials")

#textvaribles
binput = StringVar()
binput.set("_")
cinput = StringVar()
cinput.set("_")

#interface
instructions = Label (win, text = "Today we are going to factor trinomials. \nEnter two values for the b-coefficient and c-coefficient ", )

a = Label (win, text = "x^2")
bentry = Entry (win, textvariable = binput)

#grid
instructions.grid(row = 1, column = 1, columnspan = 2, rowspan = 2, sticky = W)
a.grid(row = 3, column = 1)


win.mainloop()