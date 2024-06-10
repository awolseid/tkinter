### More Button Types

# In Tkinter, there are several types of buttons that you can create:

# Button: The standard button that executes a command when clicked.
# Checkbutton: A button that toggles between two states (checked and unchecked).
# Radiobutton: A button that is part of a group where only one button can be selected at a time.
# Menubutton: A button that opens a menu when clicked.
# Scale: A slider widget that allows the user to select a value from a range.
# Spinbox: A widget that allows the user to select from a fixed set of values by clicking arrow buttons.
# Message box button: Buttons that are displayed in message boxes created using the messagebox module.
# These are the primary button types available in Tkinter for creating graphical user interfaces. Each type has its own specific use case and behavior.

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Button Types Example")

check_var = IntVar() # to integer values in Checkbutton and Radiobutton Widgets
check_button = Checkbutton(root, text="Check me!", variable="check_var")
check_button.pack()

radio_var = StringVar()
radio_button1 = Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio_button2 = Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio_button1.pack()
radio_button2.pack()

options = ["Option 1", "Option 2", "Option 3"]
menu_var = StringVar(root)
menu_var.set(options[0])
menu_button = OptionMenu(root, menu_var, *options)
menu_button.pack()

scale = Scale(root, from_=0, to=10, orient=HORIZONTAL)
scale.pack()

spinbox = Spinbox(root, values=("Option 1", "Option 2", "Option 3"))
spinbox.pack()

def show_message():
    messagebox.showinfo("Info", "This is a message box!")

message_button = Button(root, text="Show Message", command=show_message)
message_button.pack()

root.mainloop()