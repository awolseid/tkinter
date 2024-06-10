### Creating Input Fields/Boxes

# from tkinter import *
# root = Tk()

# e = Entry(root)
# e.pack()

# def myClick():
#     myLabel = Label(root, text = "Look! I clicked a Button")
#     myLabel.pack()
    
# myButton = Button(root, text = "Click Me!", command = myClick, fg = "blue") 
# myButton.pack()                                                

# root.mainloop()


# from tkinter import *
# root = Tk()

# e = Entry(root, width = 50, bg = "orange", fg = "red")
# e.pack()

# def myClick():
#     myLabel = Label(root, text = "Look! I clicked a Button")
#     myLabel.pack()
    
# myButton = Button(root, text = "Click Me!", command = myClick, fg = "blue") 
# myButton.pack()                                                

# root.mainloop()




# from tkinter import *
# root = Tk()

# e = Entry(root, width = 50, borderwidth = 5)
# e.pack()

# def myClick():
#     myLabel = Label(root, text = "Look! I clicked a Button")
#     myLabel.pack()
    
# myButton = Button(root, text = "Click Me!", command = myClick, fg = "blue") 
# myButton.pack()                                                

# root.mainloop()



# from tkinter import *
# root = Tk()

# e = Entry(root, width = 50)
# e.pack()


# def myClick():
#     myLabel = Label(root, text = e.get())
#     myLabel.pack()
    
# myButton = Button(root, text = "Click Me!", command = myClick) 
# myButton.pack()                                                

# root.mainloop()



# from tkinter import *
# root = Tk()

# e = Entry(root, width = 50)
# e.pack()


# def myClick():
#     myLabel = Label(root, text = "Hello " + e.get())
#     myLabel.pack()
    
# myButton = Button(root, text = "Click Me!", command = myClick) 
# myButton.pack()                                                

# root.mainloop()


from tkinter import *
root = Tk()

e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter Your Name:")


def myClick():
    myLabel = Label(root, text = "Hello " + e.get())
    myLabel.pack()
    
myButton = Button(root, text = "Click Me!", command = myClick) 
myButton.pack()                                                

root.mainloop()
