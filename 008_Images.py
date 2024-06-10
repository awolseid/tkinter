### Icons, Images, ExitButtons

# from tkinter import *

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("C://Users//Administrator//Desktop//GUI_TKinter//logo_image.ico")

# root.mainloop()



# from tkinter import *

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("C://Users//Administrator//Desktop//GUI_TKinter//logo_image.ico")
# button_quit = Button(root, text = "Exit Program", command = root.quit)
# button_quit.pack()

# root.mainloop()


from tkinter import *
from PIL import ImageTk, Image 
### install 'pillow' in command line using 'pip install pillow'
### Check if successfully installed using pip freeze


root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")
my_img = ImageTk.PhotoImage(Image.open("ds_cycle.png"))
my_label = Label(image = my_img)
my_label.pack()


button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()

root.mainloop()
