### Image Viewer App: Status Bar
# from tkinter import *
# from PIL import ImageTk, Image 

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# my_img1 = ImageTk.PhotoImage(Image.open("images/food1.png"))
# my_img2 = ImageTk.PhotoImage(Image.open("images/food2.png"))
# my_img3 = ImageTk.PhotoImage(Image.open("images/food3.png"))

# image_list = [my_img1, my_img2, my_img3]

# # status = Label(root, text = f"Image 1 of {len(image_list)}")
# # status = Label(root, text = f"Image 1 of {len(image_list)}", bd = 1, relief = SUNKEN) # bd= boarder
# status = Label(root, text = f"Image 1 of {len(image_list)}", bd = 1, relief = SUNKEN, anchor = E) # put status to East (right)

# my_label = Label(image = my_img1)
# my_label.grid(row = 0, column = 0, columnspan = 3) # 3 below to have a forward, back and quit buttons

# def forward(image_number):
#     global my_label
#     global button_forward
#     global button_back

#     my_label.grid_forget()

#     my_label = Label(image = image_list[image_number - 1])
#     button_forward = Button(root, text = ">>", command = lambda: forward(image_number + 1))
#     button_back = Button(root, text = "<<", command = lambda: back(image_number - 1))

#     if image_number == 3:
#         button_forward = Button(root, text = ">>", state = DISABLED)

#     my_label.grid(row = 0, column = 0, columnspan = 3)
#     button_back.grid(row = 1, column = 0)
#     button_forward.grid(row = 1, column = 2)

# def back(image_number):
#     global my_label
#     global button_forward
#     global button_back

#     my_label.grid_forget()

#     my_label = Label(image = image_list[image_number - 1])
#     button_forward = Button(root, text = ">>", command = lambda: forward(image_number + 1))
#     button_back = Button(root, text = "<<", command = lambda: back(image_number - 1))

#     if image_number == 1:
#         button_back = Button(root, text = "<<", state = DISABLED)

#     my_label.grid(row = 0, column = 0, columnspan = 3)
#     button_back.grid(row = 1, column = 0)
#     button_forward.grid(row = 1, column = 2)

# ### This is when the program is run at first.
# button_back = Button(root, text = "<<", state = DISABLED, command = back) # for 1st image no backward argument
# button_exit = Button(root, text = "Exit Program", command = root.quit)
# button_forward = Button(root, text = ">>", command = lambda: forward(2)) # Go to 2nd picture, first image is on 1, next is 2


# button_back.grid(row = 1, column = 0)
# button_exit.grid(row = 1, column = 1)
# # button_forward.grid(row = 1, column = 2)
# button_forward.grid(row = 1, column = 2, pady = 10)
# # status.grid(row = 2, column = 0, columnspan = 3)
# status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E) # streaching status bar boarder West to East

# root.mainloop()


from tkinter import *
from PIL import ImageTk, Image 

root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")
my_img1 = ImageTk.PhotoImage(Image.open("images/food1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/food2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/food3.png"))

image_list = [my_img1, my_img2, my_img3]

# status = Label(root, text = f"Image 1 of {len(image_list)}")
# status = Label(root, text = f"Image 1 of {len(image_list)}", bd = 1, relief = SUNKEN) # bd= boarder
status = Label(root, text = f"Image 1 of {len(image_list)}", bd = 1, relief = SUNKEN, anchor = E) # put status to East (right)

my_label = Label(image = my_img1)
my_label.grid(row = 0, column = 0, columnspan = 3) # 3 below to have a forward, back and quit buttons

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()

    my_label = Label(image = image_list[image_number - 1])
    button_forward = Button(root, text = ">>", command = lambda: forward(image_number + 1))
    button_back = Button(root, text = "<<", command = lambda: back(image_number - 1))

    if image_number == 3:
        button_forward = Button(root, text = ">>", state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)
    status = Label(root, text = f"Image {image_number} of {len(image_list)}", bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()

    my_label = Label(image = image_list[image_number - 1])
    button_forward = Button(root, text = ">>", command = lambda: forward(image_number + 1))
    button_back = Button(root, text = "<<", command = lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text = "<<", state = DISABLED)

    my_label.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_forward.grid(row = 1, column = 2)
    status = Label(root, text = f"Image {image_number} of {len(image_list)}", bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

### This is when the program is run at first.
button_back = Button(root, text = "<<", state = DISABLED, command = back) # for 1st image no backward argument
button_exit = Button(root, text = "Exit Program", command = root.quit)
button_forward = Button(root, text = ">>", command = lambda: forward(2)) # Go to 2nd picture, first image is on 1, next is 2


button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
# button_forward.grid(row = 1, column = 2)
button_forward.grid(row = 1, column = 2, pady = 10)
# status.grid(row = 2, column = 0, columnspan = 3)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E) # streaching status bar boarder West to East

root.mainloop()



