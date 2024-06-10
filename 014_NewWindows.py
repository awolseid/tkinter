### creating New Windows

# from tkinter import *
# from PIL import ImageTk, Image 
# from tkinter import messagebox

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# top = Toplevel()

# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 
# from tkinter import messagebox

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# top = Toplevel()
# label = Label(top, text = "Hello World").pack()

# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 
# from tkinter import messagebox

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# top = Toplevel()
# my_img = ImageTk.PhotoImage(Image.open("images/food1.png"))
# my_label = Label(top, image = my_img).pack()

# mainloop()


# from tkinter import *
# from PIL import ImageTk, Image 
# from tkinter import messagebox

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# top = Toplevel()
# top.title("My Second WIndow")
# top.iconbitmap("logo_image.ico")
# my_img = ImageTk.PhotoImage(Image.open("images/food1.png"))
# my_label = Label(top, image = my_img).pack()

# mainloop()




# from tkinter import *
# from PIL import ImageTk, Image 
# from tkinter import messagebox

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")


# def open():
#     top = Toplevel()
#     top.title("My Second WIndow")
#     top.iconbitmap("logo_image.ico")
#     my_img = ImageTk.PhotoImage(Image.open("images/food1.png"))
#     my_label = Label(top, image = my_img).pack()

# button = Button(root, text = "My Second Window", command = open).pack()
# ## clicking this button opens Second window but doesnot display the image
# ## because in python it is treated as a local variable now

# mainloop()




# from tkinter import *
# from PIL import ImageTk, Image 
# from tkinter import messagebox

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")


# def open():
#     global my_img
#     top = Toplevel()
#     top.title("My Second WIndow")
#     top.iconbitmap("logo_image.ico")
#     my_img = ImageTk.PhotoImage(Image.open("images/food1.png"))
#     my_label = Label(top, image = my_img).pack()

# button = Button(root, text = "My Second Window", command = open).pack()

# mainloop()



from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox

root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")


def open():
    global my_img
    top = Toplevel()
    top.title("My Second WIndow")
    top.iconbitmap("logo_image.ico")
    my_img = ImageTk.PhotoImage(Image.open("images/food1.png"))
    my_label = Label(top, image = my_img).pack()
    button2 = Button(top, text = "close window", command = top.destroy).pack()

button = Button(root, text = "My Second Window", command = open).pack()

mainloop()