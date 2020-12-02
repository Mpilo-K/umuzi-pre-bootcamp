x = 0
y = 1
# Print the value of x
print(f"The value of x is {x}")
# Print the value of y
print(y)

x = x + 3
y = y + x
# Print the value of x
print(x)
# Print the value of y
print(y)

###################################################################

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