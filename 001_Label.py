### Create Graphical User Interfaces
from tkinter import *
# in TKinter every thing is a widget

# Create the root widget, which has to happen before anything to happen in TKinter
root = Tk()

myLabel = Label(root, text = "Hello World!")    # creating a Label Widget
myLabel.pack()                                  # shoving it onto the screen

root.mainloop()
