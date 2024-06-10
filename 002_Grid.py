### Positioning With the Grid System

# from tkinter import *
# root = Tk()

# myLabel1 = Label(root, text = "Hello World!")
# myLabel2 = Label(root, text = "My Name is Awol Seid")

# myLabel1.grid(row = 0, column = 0)
# # myLabel2.grid(row = 1, column = 0)
# # myLabel2.grid(row = 1, column = 1)
# myLabel2.grid(row = 1, column = 5)              # same as (row = 1, column =1)                                               

# root.mainloop()




# from tkinter import *
# root = Tk()

# myLabel1 = Label(root, text = "Hello World!")
# myLabel2 = Label(root, text = "My Name is Awol Seid")
# # myLabel3 = Label(root, text = " ")
# myLabel3 = Label(root, text = "               ")

# myLabel1.grid(row = 0, column = 0)
# # myLabel2.grid(row = 1, column = 0)
# # myLabel2.grid(row = 1, column = 1)
# myLabel2.grid(row = 1, column = 5)              # same as (row = 1, column =1)
# myLabel3.grid(row = 1, column = 1)                                               

# root.mainloop()



from tkinter import *
root = Tk()

myLabel1 = Label(root, text = "Hello World!").grid(row = 0, column = 0)
myLabel2 = Label(root, text = "My Name is Awol Seid").grid(row = 1, column = 5)

# myLabel1.grid(row = 0, column = 0)
# myLabel2.grid(row = 1, column = 5)                                                   

root.mainloop()