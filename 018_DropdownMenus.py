### Dropdown Menus

# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# clicked = StringVar()
# drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# drop.pack()

# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# clicked = StringVar()
# clicked.set("Monday") # default
# drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# drop.pack()

# def show():
#     label = Label(root, text = clicked.get()).pack()

# button = Button(root, text = "Show Selection", command = show).pack()


# mainloop()



from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")
root.geometry("400x400")

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
clicked = StringVar()
clicked.set(options[0]) # default
drop = OptionMenu(root, clicked, *options)
drop.pack()

def show():
    label = Label(root, text = clicked.get()).pack()

button = Button(root, text = "Show Selection", command = show).pack()


mainloop()