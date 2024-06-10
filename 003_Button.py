### Creating Buttons

# from tkinter import *
# root = Tk()

# # myButton = Button(root, text = "Click Me!") 
# # myButton = Button(root, text = "Click Me!", padx = 50) 
# # myButton = Button(root, text = "Click Me!", pady = 50) 
# # myButton = Button(root, text = "Click Me!", padx = 50, pady = 50) 
# myButton = Button(root, text = "Click Me!", state = "disabled") 
# myButton.pack()                                                

# root.mainloop()



# from tkinter import *
# root = Tk()

# def myClick():
#     myLabel = Label(root, text = "Look! I clicked a Button")
#     myLabel.pack()

# # Executing it do not make the function happen unless it is called.
# myButton = Button(root, text = "Click Me!") 
# myButton.pack()                                                

# root.mainloop()


from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root, text = "Look! I clicked a Button")
    myLabel.pack()
    
myButton = Button(root, text = "Click Me!", command = myClick, fg = "blue") 
# foreground color, background = bg, xcolor codes =
# Everytime clicking the Click Me button creates the label.
# In a python prog, a function is called like fun().
# If we make command = myClick(), it executes once when 
# the program runs and clicking does nothing on the GUI
myButton.pack()                                                

root.mainloop()