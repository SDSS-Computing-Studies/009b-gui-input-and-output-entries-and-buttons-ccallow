"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()
#text code
entry1 = tk.Entry(win, textVariable = labelName)

#text variables
labelName = StringVar()
labelName.set("Name")
labelVerb = StringVar()
labelVerb.set("Verb")
labelAdj = StringVar()
labelAdj.set("Adjective")
labelAnimal = StringVar()
labelAnimal.set("Animal")

win.mainloop