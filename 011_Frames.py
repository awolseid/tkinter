#### Adding Frames to Your Program

# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# frame = LabelFrame(root, text = "This is my frame ...", padx= 5, pady = 5)
# frame.pack(padx = 10, pady = 10)

# b = Button(frame, text = "Button on the frame") # now we need to put on the frame instead of the root
# b.pack()

# root.mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# frame = LabelFrame(root, text = "This is my frame ...", padx= 5, pady = 5)
# frame.pack(padx = 100, pady = 100)

# b = Button(frame, text = "Button on the frame") # now we need to put on the frame instead of the root
# b.pack()

# root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# frame = LabelFrame(root, text = "This is my frame ...", padx= 50, pady = 50)
# frame.pack(padx = 10, pady = 10)

# b = Button(frame, text = "Button on the frame") # now we need to put on the frame instead of the root
# b.pack()

# root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# frame = LabelFrame(root, text = "This is my frame ...", padx= 50, pady = 50)
# frame.pack(padx = 10, pady = 10)

# b = Button(frame, text = "Button on the frame") # now we need to put on the frame instead of the root
# b.grid(row = 0, column = 0)

# root.mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# frame = LabelFrame(root, text = "This is my frame ...", padx= 50, pady = 50)
# frame.pack(padx = 10, pady = 10)

# b = Button(frame, text = "Button on the frame") # now we need to put on the frame instead of the root
# b2 = Button(frame, text = "Second Button")
# b.grid(row = 0, column = 0)
# b2.grid(row = 1, column = 1)

# root.mainloop()



from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")

frame = LabelFrame(root, padx= 50, pady = 50)
frame.pack(padx = 10, pady = 10)

b = Button(frame, text = "Button on the frame") # now we need to put on the frame instead of the root
b2 = Button(frame, text = "Second Button")
b.grid(row = 0, column = 0)
b2.grid(row = 1, column = 1)

root.mainloop()