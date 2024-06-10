### Sliders

# from tkinter import *
# from PIL import ImageTk, Image 


# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400") # window size

# vertical = Scale(root, from_ = 0, to = 200)
# vertical.pack()
# horizontal = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL).pack()


# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 


# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400") # window size

# vertical = Scale(root, from_ = 0, to = 200)
# vertical.pack()
# horizontal = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL)
# horizontal.pack()
# label = Label(root, text = horizontal.get()).pack()


# mainloop()





# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400") # window size

# vertical = Scale(root, from_ = 0, to = 200)
# vertical.pack()
# horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL)
# horizontal.pack()
# def slide():
#     label = Label(root, text = horizontal.get()).pack()
#     root.geometry(str(horizontal.get()) + "x400")

# button = Button(root, text = "Click Me", command = slide).pack()


# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400") # window size

# vertical = Scale(root, from_ = 0, to = 200)
# vertical.pack()

# def slide():
#     label = Label(root, text = horizontal.get()).pack()
#     root.geometry(str(horizontal.get()) + "x400")

# horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL, command = slide) # will not work unless there is something in slide fun
# horizontal.pack()

# label = Label(root, text = horizontal.get()).pack()

# button = Button(root, text = "Click Me", command = slide).pack()

# mainloop()


# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400") # window size

# vertical = Scale(root, from_ = 0, to = 200)
# vertical.pack()

# def slide(var = 0): # unless there is something in this function, it won't work
#     label = Label(root, text = horizontal.get()).pack()
#     root.geometry(str(horizontal.get()) + "x400")

# horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL, command = slide) 
# horizontal.pack()

# label = Label(root, text = horizontal.get()).pack()

# button = Button(root, text = "Click Me", command = slide).pack()

# mainloop()




from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")
root.geometry("400x400") # window size

vertical = Scale(root, from_ = 0, to = 200)
vertical.pack()

def slide():
    label = Label(root, text = horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL) 
horizontal.pack()

label = Label(root, text = horizontal.get()).pack()

button = Button(root, text = "Click Me", command = slide).pack()

mainloop()