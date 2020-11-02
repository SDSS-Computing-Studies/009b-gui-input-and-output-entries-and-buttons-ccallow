"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit      to see some Madlibs
you might use in your assignment
"""

import tkinter as tk 
from tkinter import *

win = tk.Tk()

def clickStory():
    a = Adj1.get()
    a = str(a)
    b = verb1.get()
    b = str(b)
    c = Adj2.get()
    c = str(c)
    d = Food1.get()
    d = str(d)
    e = Adj3.get()
    e = str(e)
    f = Noun.get()
    f = str(f)
    g = Fam.get()
    g = str(g)
    h = Food2.get()
    h = str(h)
    i = Adj4.get()
    i = str(i)
    line1 = "Our school cafeteria has really " + a + " food. Just thinking about it makes"
    line2 = "my stomach " + b + ". The spaghetti is " + c +"and tastes like " + d + "The turkey"
    line3 = "tacos are totally " + e + " and they look like old " + f + ". My " + g
    line4 = " said that they would make my lunches, but on the first day , I got a"
    line5 =  "sandwich made of "+ h + "and mayo. I think I'd rather take my chances with"
    line6 = "the " + i + "cafeteria!"
    story = line1 + "\n" + line2 + "\n" + line3 + "\n" +line4 + "\n"+ line5 +"\n" + line6
    a_entry.delete(0,END)
    a_entry.insert(0, story)

    
eoutput = StringVar()
eoutput.set("Finished Story goes here")

#text variables for inputs
labelFam = StringVar()
labelFam.set("Family Member")

labelFood1 = StringVar()
labelFood1.set("Food")
labelFood2 = StringVar()
labelFood2.set("Food")

labelAdj = StringVar()
labelAdj.set =("Adjective")
labelAdj2 = StringVar()
labelAdj2.set =("Adjective")
labelAdj3 = StringVar()
labelAdj3.set =("Adjective")
labelAdj4 = StringVar()
labelAdj4.set =("Adjective")

labelVerb1 = StringVar()
labelVerb1.set =("Verb")

labelNoun = StringVar()
labelNoun.set =("Noun-plural")

#text code - adj
label1 = Label(win, text = "Enter four adjectives:")
Adj1 = Entry(win, textvariable=labelAdj)
Adj2 = Entry(win, textvariable=labelAdj2)
Adj3 = Entry(win, textvariable=labelAdj3)
Adj4 = Entry(win, textvariable=labelAdj4)

#text code - verbs
label2 = Label (win, text = "Enter a verb:")
verb1 = Entry (win, textvariable=labelVerb1)

#text code - food
label3 = Label(win, text = "Enter two types of food:")
Food1 = Entry (win, textvariable=labelFood1)
Food2 = Entry (win, textvariable=labelFood2)

#remainder of code
label4 = Label(win, text = "Enter a plural noun")
label5 = Label(win, text = "Enter a family member:")
Noun = Entry(win, textvariable = labelNoun)
Fam = Entry(win, textvariable = labelFam)
button1 = Button(win, text = "Show me the story!", command = clickStory)
a_label = Label(win, text = "Here is your story: ")
a_entry = Entry(win, width = 75, textvariable=eoutput)

#adjectives code
label1.grid(row = 1, column = 1, sticky = W)
Adj1.grid(row = 1, column = 2)
Adj2.grid(row = 1, column = 3)
Adj3.grid(row = 2, column = 2)
Adj4.grid(row = 2, column = 3)
#verbs code
label2.grid(row = 3, column = 1, sticky = W)
verb1.grid(row = 3, column = 2)
#food code
label3.grid(row =4 , column = 1, sticky = W)
Food1.grid(row = 4, column =2)
Food2.grid(row = 4, column = 3)
#noun and family
label4.grid(row = 5, column = 1, sticky = W)
Noun.grid(row =5, column = 2)
label5.grid(row = 6, column = 1, sticky = W)
Fam.grid(row = 6, column = 2)
#remainder
button1.grid(row = 6, column = 2, columnspan = 2)
a_label.grid(row =7, column = 1, sticky = W)
a_entry.grid(row = 8, column = 1, columnspan = 3, sticky = W)



win.mainloop()