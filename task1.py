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

def clickStory():
    a = entry1.get()
    a = str(a)
    b = entry2.get()
    b = str(b)
    story = "This is " + a + ". And it is a crazy " + b + "."
    a_entry.delete(0,END)
    a_entry.insert(0, story)

    


eoutput = StringVar()
eoutput.set("Finished Story goes here")

#text variables for inputs
labelName = StringVar()
labelName.set("Name")
labelAnimal = StringVar()
labelAnimal.set("Animal")

#text code
label1 = Label(win, text = "This is ")
entry1 = Entry(win, textvariable=labelName)
period = Label (win, text = ".")
label2 = Label (win, text = "And it is a crazy ")
entry2 = Entry (win, textvariable=labelAnimal)
period2 = Label (win, text = ".")
button1 = Button(win, text = "Show me the story!", command = clickStory)
a_label = Label(win, text = "Here is your story: ")
a_entry = Entry(win, width = 40, textvariable=eoutput)

#position code
label1.grid(row = 1, column = 1, sticky = E)
entry1.grid(row = 1, column = 2)
period.grid(row = 1, column = 3, sticky = W)
label2.grid(row = 2, column = 1, sticky = E)
entry2.grid(row = 2, column = 2)
period2.grid(row =2, column = 3, sticky = W)
button1.grid(row = 3, column = 2, columnspan = 2)
a_label.grid(row =4, column = 1)
a_entry.grid(row = 5, column = 1, columnspan = 4)



win.mainloop()