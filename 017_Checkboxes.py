### Checkboxes

# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# var = IntVar()

# c = Checkbutton(root, text = "Check this box, I dare you!", variable = var)
# c.pack()
# label = Label(root, text = var.get()).pack() # value is 0 since unchecked by default

# mainloop()




# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# var = IntVar()

# c = Checkbutton(root, text = "Check this box, I dare you!", variable = var)
# c.pack()
# def show():
#     label = Label(root, text = var.get()).pack() 

# button = Button(root, text = "Show Selection", command = show).pack()

# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# var = StringVar()

# c = Checkbutton(root, text = "Check this box, I dare you!", variable = var, onvalue = "ON", offvalue = "OFF")
# ## the box will be checked by default, when clicking show selection button ==> nothing happens
# ## Unless we unchecked, the show selection button do not display the values
# c.pack()
# def show():
#     label = Label(root, text = var.get()).pack() 

# button = Button(root, text = "Show Selection", command = show).pack()

# mainloop()




from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")
root.geometry("400x400")

var = StringVar()

c = Checkbutton(root, text = "Check this box, I dare you!", variable = var, onvalue = "ON", offvalue = "OFF")
c.deselect()
c.pack()
def show():
    label = Label(root, text = var.get()).pack() 

button = Button(root, text = "Show Selection", command = show).pack()

mainloop()