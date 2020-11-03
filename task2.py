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
binput.set("")
cinput = StringVar()
cinput.set("")

#instructions
inst1 = Label (win, text = "Today we are going to factor trinomials. \n 1. Enter two values for the b-coefficient and c-coefficient. \n 2. Hit the factor button and the answer will appear. \n *** If you want to make the b or c values negative, remember a negative sign.***", anchor = W, justify = LEFT)
inst2  = Label (win, text  = "1. Enter two values for the b-coefficient and c-coefficient.")
inst3 = Label (win, text = "2. Hit the factor button and the answer will appear.")
instNote = Label(win, text  = "*** If you want to make the b or c values negative, remember a negative sign.***" )
entry = Label(win, text = "Enter your values:")

#entry boxes
a = Label (win, text = "x^2 +")
bentry = Entry (win, textvariable = binput, width = 5)
b = Label (win, text = "x")
centry = Label (win, textvariable = cinput, width = 5)

#grid for instructions
inst1.grid(row = 1, column = 1, columnspan = 15)
#inst2.grid(row = 2, column = 1, columnspan = 6, sticky = W)
#inst3.grid(row = 3, column = 1, columnspan = 5, sticky = W)
#instNote.grid(row = 4, column = 1, columnspan= 8, sticky = W)
entry.grid( row = 5, column = 1, columnspan = 2, sticky = W)

#grid for code
a.grid(row = 6, column = 1, sticky = E)
bentry.grid(row = 6, column = 2, sticky = W)
b.grid(row = 6, column = 3, sticky = E)
centry.grid (row = 6, column = 4, sticky = W)


win.mainloop()