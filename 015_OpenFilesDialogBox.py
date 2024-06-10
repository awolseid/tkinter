### Open Files Dialog Box

# from tkinter import *
# from PIL import ImageTk, Image 
# from tkinter import messagebox
# from tkinter import filedialog

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# root.filename = filedialog.askopenfilename(initialdir = "/GUI_TKinter/images",
#                                            title = "Open a File", 
#                                            filetypes = (("png files", "*.png"), ("all files", "*.*"))) 
## return the name and location of a file:
## select a file and click ok, nothing will be shown.


# mainloop()




# from tkinter import *
# from PIL import ImageTk, Image 
# from tkinter import messagebox
# from tkinter import filedialog

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")

# root.filename = filedialog.askopenfilename(initialdir = "/GUI_TKinter/images",
#                                            title = "Open a File", 
#                                            filetypes = (("png files", "*.png"), ("all files", "*.*"))) 

# label = Label(root, text = root.filename).pack()
# ## Select a file and click ok shows the loaction in the window.
# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# image_label = Label(image = my_image).pack()

# mainloop()





from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "/GUI_TKinter/images",
                                            title = "Open a File", 
                                            filetypes = (("png files", "*.png"), ("all files", "*.*"))) 

    label = Label(root, text = root.filename).pack()
    ## Select a file and click ok shows the loaction in the window.
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    image_label = Label(image = my_image).pack()

button = Button(root, text = "Open File", command = open).pack()

mainloop()