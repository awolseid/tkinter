### Radio Buttons

# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# r = IntVar() # TKinter variable
# Radiobutton(root, text = "Option 1", variable = r, value = 1).pack()
# Radiobutton(root, text = "Option 2", variable = r, value = 2).pack()

# # r = StringVar() # TKinter variable
# # Radiobutton(root, text = "Option 1", variable = r, value = "1").pack()
# # Radiobutton(root, text = "Option 2", variable = r, value = "2").pack()

# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# r = IntVar() # TKinter variable
# Radiobutton(root, text = "Option 1", variable = r, value = 1).pack()
# Radiobutton(root, text = "Option 2", variable = r, value = 2).pack()

# myLabel = Label(root, text = r.get())
# myLabel.pack()

# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# r = IntVar() # TKinter variable
# r.set("2")
# Radiobutton(root, text = "Option 1", variable = r, value = 1).pack()
# Radiobutton(root, text = "Option 2", variable = r, value = 2).pack()

# myLabel = Label(root, text = r.get())
# myLabel.pack()

# mainloop()


# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# r = IntVar() # TKinter variable
# r.set("2")

# def clicked(value):
#     myLabel = Label(root, text = value)
#     myLabel.pack()

# Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
# Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

# myLabel = Label(root, text = r.get())
# myLabel.pack()

# mainloop()


# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# r = IntVar() # TKinter variable
# r.set("2")

# def clicked(value):
#     myLabel = Label(root, text = value)
#     myLabel.pack()

# Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
# Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

# myLabel = Label(root, text = r.get())
# myLabel.pack()

# myButton = Button(root, text = "Click Me!", command = lambda: clicked(r.get()))
# myButton.pack()

# mainloop()


# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# MODES = [
#     ("Pepperoni", "Pepperoni"),
#     ("Cheese", "Cheese"),
#     ("Mushroom", "Mushroom"),
#     ("Onion", "Onion")
# ]

# pizza = StringVar()
# pizza.set("Pepperoni")

# for text, mode in MODES:
#     Radiobutton(root, text = text, variable = pizza, value = mode).pack() # commnad not included here. Hence, checking doesnt result, but click does
# def clicked(value):
#     myLabel = Label(root, text = value)
#     myLabel.pack()


# myLabel = Label(root, text = pizza.get())
# myLabel.pack()

# myButton = Button(root, text = "Click Me!", command = lambda: clicked(pizza.get()))
# myButton.pack()

# mainloop()


from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text = text, variable = pizza, value = mode).pack(anchor = W) 
def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()


# myLabel = Label(root, text = pizza.get())
# myLabel.pack()

myButton = Button(root, text = "Click Me!", command = lambda: clicked(pizza.get()))
myButton.pack()

mainloop()