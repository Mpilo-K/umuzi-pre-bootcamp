# This task isn’t compulsory but we’ll be impressed if you do it.
# Can you make a user interface for each of the previous tasks?
# You’ll need HTML and CSS to do it.

# Import Tkinter
from tkinter import *
root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text = hello)
    myLabel.pack()


myButton = Button(root, text = "Enter your name:", command=myClick, fg='blue')
myButton.pack()

# Creating labels
#myLabel1 = Label(root, text = "gui example")
#myLabel2 = Label(root, text = "My name is Mpilo Khumalo")

# Positioning labels
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)

# Puting it onto the screen
# myLabel.pack()

root.mainloop()