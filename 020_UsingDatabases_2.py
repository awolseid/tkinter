### Using Databases: Building GUI for the database app

# from tkinter import *
# from PIL import ImageTk, Image 
# import sqlite3

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# # create a database or connect to one
# con = sqlite3.connect("address_book.db")

# # create cursor -> a cursor sends the result to the db
# c = con.cursor()

# ### We already created the table
# ### create table 
# # c.execute("""
# # CREATE TABLE addresses(
# #           first_name text,
# #           last_name text,
# #           address text,
# #           city text,
# #           state text, 
# #           zipcode integer
# # )""")

# # Create text boxes
# f_name = Entry(root, width = 30)
# f_name.grid(row = 0, column = 1, padx = 20)

# l_name = Entry(root, width = 30)
# l_name.grid(row = 1, column = 1, padx = 20)

# address = Entry(root, width = 30)
# address.grid(row = 2, column = 1, padx = 20)

# city = Entry(root, width = 30)
# city.grid(row = 3, column = 1, padx = 20)

# state = Entry(root, width = 30)
# state.grid(row = 4, column = 1, padx = 20)

# zipcode = Entry(root, width = 30)
# zipcode.grid(row = 5, column = 1, padx = 20)

# # Create text box labels
# f_name_label = Label(root, text = "First Name")
# f_name_label.grid(row = 0, column = 0)

# l_name_label = Label(root, text = "Last Name")
# l_name_label.grid(row = 1, column = 0)

# address_label = Label(root, text = "Address")
# address_label.grid(row = 2, column = 0)

# city_label = Label(root, text = "City")
# city_label.grid(row = 3, column = 0)

# state_label = Label(root, text = "State")
# state_label.grid(row = 4, column = 0)

# zipcode_label = Label(root, text = "Zipcode")
# zipcode_label.grid(row = 5, column = 0)

# # create Submit button
# def submit():
#     # clear text boxes
#     f_name.delete(0, END)
#     l_name.delete(0, END)
#     address.delete(0, END)
#     city.delete(0, END)
#     state.delete(0, END)
#     zipcode.delete(0, END)

# submit_button = Button(root, text = "Add Record to Database", command = submit)
# submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


# # Commit changes -> commiting changes to the db
# con.commit()

# #close connection
# con.close()

# mainloop()


# from tkinter import *
# from PIL import ImageTk, Image 
# import sqlite3

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# # create a database or connect to one
# con = sqlite3.connect("address_book.db")

# # create cursor -> a cursor sends the result to the db
# c = con.cursor()

# ### We already created the table
# ### create table 
# # c.execute("""
# # CREATE TABLE addresses(
# #           first_name text,
# #           last_name text,
# #           address text,
# #           city text,
# #           state text, 
# #           zipcode integer
# # )""")

# # Create text boxes
# f_name = Entry(root, width = 30)
# f_name.grid(row = 0, column = 1, padx = 20)

# l_name = Entry(root, width = 30)
# l_name.grid(row = 1, column = 1, padx = 20)

# address = Entry(root, width = 30)
# address.grid(row = 2, column = 1, padx = 20)

# city = Entry(root, width = 30)
# city.grid(row = 3, column = 1, padx = 20)

# state = Entry(root, width = 30)
# state.grid(row = 4, column = 1, padx = 20)

# zipcode = Entry(root, width = 30)
# zipcode.grid(row = 5, column = 1, padx = 20)

# # Create text box labels
# f_name_label = Label(root, text = "First Name")
# f_name_label.grid(row = 0, column = 0)

# l_name_label = Label(root, text = "Last Name")
# l_name_label.grid(row = 1, column = 0)

# address_label = Label(root, text = "Address")
# address_label.grid(row = 2, column = 0)

# city_label = Label(root, text = "City")
# city_label.grid(row = 3, column = 0)

# state_label = Label(root, text = "State")
# state_label.grid(row = 4, column = 0)

# zipcode_label = Label(root, text = "Zipcode")
# zipcode_label.grid(row = 5, column = 0)

# # create Submit button
# def submit():
#     # create a database or connect to one
#     con = sqlite3.connect("address_book.db")
#     # create cursor -> a cursor sends the result to the db
#     c = con.cursor()
#     # Insert into table
#     c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", # can me like (:a,...:f), same should be used in the dict below
#              {
#                 "f_name": f_name.get(), 
#                 "l_name":l_name.get(),
#                 "address": address.get(),
#                 "city": city.get(),
#                 "state": state.get(),
#                 "zipcode": zipcode.get()
#              })

#     # Commit changes -> commiting changes to the db
#     con.commit()
#     #close connection
#     con.close()

#     # clear text boxes
#     f_name.delete(0, END)
#     l_name.delete(0, END)
#     address.delete(0, END)
#     city.delete(0, END)
#     state.delete(0, END)
#     zipcode.delete(0, END)

# submit_button = Button(root, text = "Add Record to Database", command = submit)
# submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


# # Commit changes -> commiting changes to the db
# con.commit()

# #close connection
# con.close()

# mainloop()
### In the above code, run, enter data and click the submit record to database button, if no error, that is ok.




# from tkinter import *
# from PIL import ImageTk, Image 
# import sqlite3

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# # create a database or connect to one
# con = sqlite3.connect("address_book.db")

# # create cursor -> a cursor sends the result to the db
# c = con.cursor()

# ### We already created the table
# ### create table 
# # c.execute("""
# # CREATE TABLE addresses(
# #           first_name text,
# #           last_name text,
# #           address text,
# #           city text,
# #           state text, 
# #           zipcode integer
# # )""")

# # Create text boxes
# f_name = Entry(root, width = 30)
# f_name.grid(row = 0, column = 1, padx = 20)

# l_name = Entry(root, width = 30)
# l_name.grid(row = 1, column = 1, padx = 20)

# address = Entry(root, width = 30)
# address.grid(row = 2, column = 1, padx = 20)

# city = Entry(root, width = 30)
# city.grid(row = 3, column = 1, padx = 20)

# state = Entry(root, width = 30)
# state.grid(row = 4, column = 1, padx = 20)

# zipcode = Entry(root, width = 30)
# zipcode.grid(row = 5, column = 1, padx = 20)

# # Create text box labels
# f_name_label = Label(root, text = "First Name")
# f_name_label.grid(row = 0, column = 0)

# l_name_label = Label(root, text = "Last Name")
# l_name_label.grid(row = 1, column = 0)

# address_label = Label(root, text = "Address")
# address_label.grid(row = 2, column = 0)

# city_label = Label(root, text = "City")
# city_label.grid(row = 3, column = 0)

# state_label = Label(root, text = "State")
# state_label.grid(row = 4, column = 0)

# zipcode_label = Label(root, text = "Zipcode")
# zipcode_label.grid(row = 5, column = 0)

# # create Submit button
# def submit():
#     # create a database or connect to one
#     con = sqlite3.connect("address_book.db")
#     # create cursor -> a cursor sends the result to the db
#     c = con.cursor()
#     # Insert into table
#     c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", # can me like (:a,...:f), same should be used in the dict below
#              {
#                 "f_name": f_name.get(), 
#                 "l_name":l_name.get(),
#                 "address": address.get(),
#                 "city": city.get(),
#                 "state": state.get(),
#                 "zipcode": zipcode.get()
#              })

#     # Commit changes -> commiting changes to the db
#     con.commit()
#     #close connection
#     con.close()

#     # clear text boxes
#     f_name.delete(0, END)
#     l_name.delete(0, END)
#     address.delete(0, END)
#     city.delete(0, END)
#     state.delete(0, END)
#     zipcode.delete(0, END)

# submit_button = Button(root, text = "Add Record to Database", command = submit)
# submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# # Create Query button
# def query():
#     pass

# query_button = Button(root, text = "Show Records", command =  query)
# query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# # Commit changes -> commiting changes to the db
# con.commit()

# #close connection
# con.close()

# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 
# import sqlite3

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# # create a database or connect to one
# con = sqlite3.connect("address_book.db")

# # create cursor -> a cursor sends the result to the db
# c = con.cursor()

# ### We already created the table
# ### create table 
# # c.execute("""
# # CREATE TABLE addresses(
# #           first_name text,
# #           last_name text,
# #           address text,
# #           city text,
# #           state text, 
# #           zipcode integer
# # )""")

# # Create text boxes
# f_name = Entry(root, width = 30)
# f_name.grid(row = 0, column = 1, padx = 20)

# l_name = Entry(root, width = 30)
# l_name.grid(row = 1, column = 1, padx = 20)

# address = Entry(root, width = 30)
# address.grid(row = 2, column = 1, padx = 20)

# city = Entry(root, width = 30)
# city.grid(row = 3, column = 1, padx = 20)

# state = Entry(root, width = 30)
# state.grid(row = 4, column = 1, padx = 20)

# zipcode = Entry(root, width = 30)
# zipcode.grid(row = 5, column = 1, padx = 20)

# # Create text box labels
# f_name_label = Label(root, text = "First Name")
# f_name_label.grid(row = 0, column = 0)

# l_name_label = Label(root, text = "Last Name")
# l_name_label.grid(row = 1, column = 0)

# address_label = Label(root, text = "Address")
# address_label.grid(row = 2, column = 0)

# city_label = Label(root, text = "City")
# city_label.grid(row = 3, column = 0)

# state_label = Label(root, text = "State")
# state_label.grid(row = 4, column = 0)

# zipcode_label = Label(root, text = "Zipcode")
# zipcode_label.grid(row = 5, column = 0)

# # create Submit button
# def submit():
#     # create a database or connect to one
#     con = sqlite3.connect("address_book.db")
#     # create cursor -> a cursor sends the result to the db
#     c = con.cursor()
#     # Insert into table
#     c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", # can me like (:a,...:f), same should be used in the dict below
#              {
#                 "f_name": f_name.get(), 
#                 "l_name":l_name.get(),
#                 "address": address.get(),
#                 "city": city.get(),
#                 "state": state.get(),
#                 "zipcode": zipcode.get()
#              })

#     # Commit changes -> commiting changes to the db
#     con.commit()
#     #close connection
#     con.close()

#     # clear text boxes
#     f_name.delete(0, END)
#     l_name.delete(0, END)
#     address.delete(0, END)
#     city.delete(0, END)
#     state.delete(0, END)
#     zipcode.delete(0, END)

# submit_button = Button(root, text = "Add Record to Database", command = submit)
# submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# # Create Query button
# def query():
#     # create a database or connect to one
#     con = sqlite3.connect("address_book.db")
#     # create cursor -> a cursor sends the result to the db
#     c = con.cursor()
#     c.execute("SELECT *, oid FROM addresses") #oid is the primary key
#     records = c.fetchall()
#     print(records) # print does not work in TKinter but it prints in the terminal when the Show Records button is clicked.


#     # Commit changes -> commiting changes to the db
#     con.commit()
#     #close connection
#     con.close()

# query_button = Button(root, text = "Show Records", command =  query)
# query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# # Commit changes -> commiting changes to the db
# con.commit()

# #close connection
# con.close()

# mainloop()




# from tkinter import *
# from PIL import ImageTk, Image 
# import sqlite3

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# # create a database or connect to one
# con = sqlite3.connect("address_book.db")

# # create cursor -> a cursor sends the result to the db
# c = con.cursor()

# ### We already created the table
# ### create table 
# # c.execute("""
# # CREATE TABLE addresses(
# #           first_name text,
# #           last_name text,
# #           address text,
# #           city text,
# #           state text, 
# #           zipcode integer
# # )""")

# # Create text boxes
# f_name = Entry(root, width = 30)
# f_name.grid(row = 0, column = 1, padx = 20)

# l_name = Entry(root, width = 30)
# l_name.grid(row = 1, column = 1, padx = 20)

# address = Entry(root, width = 30)
# address.grid(row = 2, column = 1, padx = 20)

# city = Entry(root, width = 30)
# city.grid(row = 3, column = 1, padx = 20)

# state = Entry(root, width = 30)
# state.grid(row = 4, column = 1, padx = 20)

# zipcode = Entry(root, width = 30)
# zipcode.grid(row = 5, column = 1, padx = 20)

# # Create text box labels
# f_name_label = Label(root, text = "First Name")
# f_name_label.grid(row = 0, column = 0)

# l_name_label = Label(root, text = "Last Name")
# l_name_label.grid(row = 1, column = 0)

# address_label = Label(root, text = "Address")
# address_label.grid(row = 2, column = 0)

# city_label = Label(root, text = "City")
# city_label.grid(row = 3, column = 0)

# state_label = Label(root, text = "State")
# state_label.grid(row = 4, column = 0)

# zipcode_label = Label(root, text = "Zipcode")
# zipcode_label.grid(row = 5, column = 0)

# # create Submit button
# def submit():
#     # create a database or connect to one
#     con = sqlite3.connect("address_book.db")
#     # create cursor -> a cursor sends the result to the db
#     c = con.cursor()
#     # Insert into table
#     c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", # can me like (:a,...:f), same should be used in the dict below
#              {
#                 "f_name": f_name.get(), 
#                 "l_name":l_name.get(),
#                 "address": address.get(),
#                 "city": city.get(),
#                 "state": state.get(),
#                 "zipcode": zipcode.get()
#              })

#     # Commit changes -> commiting changes to the db
#     con.commit()
#     #close connection
#     con.close()

#     # clear text boxes
#     f_name.delete(0, END)
#     l_name.delete(0, END)
#     address.delete(0, END)
#     city.delete(0, END)
#     state.delete(0, END)
#     zipcode.delete(0, END)

# submit_button = Button(root, text = "Add Record to Database", command = submit)
# submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# # Create Query button
# def query():
#     # create a database or connect to one
#     con = sqlite3.connect("address_book.db")
#     # create cursor -> a cursor sends the result to the db
#     c = con.cursor()
#     c.execute("SELECT *, oid FROM addresses") #oid is the primary key
#     records = c.fetchall()
#     print(records) # print does not work in TKinter but it prints in the terminal when the Show Records button is clicked.

#     # Loop through results
#     print_records = ""
#     for record in records[0]:
#         print_records += str(record) + "\n"

#     query_label = Label(root, text = print_records)
#     query_label.grid(row = 8, column = 0, columnspan = 2)

#     # Commit changes -> commiting changes to the db
#     con.commit()
#     #close connection
#     con.close()

# query_button = Button(root, text = "Show Records", command =  query)
# query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# # Commit changes -> commiting changes to the db
# con.commit()

# #close connection
# con.close()

# mainloop()



# from tkinter import *
# from PIL import ImageTk, Image 
# import sqlite3

# root = Tk()
# root.title("Learn To Code")
# root.iconbitmap("logo_image.ico")
# root.geometry("400x400")

# # create a database or connect to one
# con = sqlite3.connect("address_book.db")

# # create cursor -> a cursor sends the result to the db
# c = con.cursor()

# ### We already created the table
# ### create table 
# # c.execute("""
# # CREATE TABLE addresses(
# #           first_name text,
# #           last_name text,
# #           address text,
# #           city text,
# #           state text, 
# #           zipcode integer
# # )""")

# # Create text boxes
# f_name = Entry(root, width = 30)
# f_name.grid(row = 0, column = 1, padx = 20)

# l_name = Entry(root, width = 30)
# l_name.grid(row = 1, column = 1, padx = 20)

# address = Entry(root, width = 30)
# address.grid(row = 2, column = 1, padx = 20)

# city = Entry(root, width = 30)
# city.grid(row = 3, column = 1, padx = 20)

# state = Entry(root, width = 30)
# state.grid(row = 4, column = 1, padx = 20)

# zipcode = Entry(root, width = 30)
# zipcode.grid(row = 5, column = 1, padx = 20)

# # Create text box labels
# f_name_label = Label(root, text = "First Name")
# f_name_label.grid(row = 0, column = 0)

# l_name_label = Label(root, text = "Last Name")
# l_name_label.grid(row = 1, column = 0)

# address_label = Label(root, text = "Address")
# address_label.grid(row = 2, column = 0)

# city_label = Label(root, text = "City")
# city_label.grid(row = 3, column = 0)

# state_label = Label(root, text = "State")
# state_label.grid(row = 4, column = 0)

# zipcode_label = Label(root, text = "Zipcode")
# zipcode_label.grid(row = 5, column = 0)

# # create Submit button
# def submit():
#     # create a database or connect to one
#     con = sqlite3.connect("address_book.db")
#     # create cursor -> a cursor sends the result to the db
#     c = con.cursor()
#     # Insert into table
#     c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", # can me like (:a,...:f), same should be used in the dict below
#              {
#                 "f_name": f_name.get(), 
#                 "l_name":l_name.get(),
#                 "address": address.get(),
#                 "city": city.get(),
#                 "state": state.get(),
#                 "zipcode": zipcode.get()
#              })

#     # Commit changes -> commiting changes to the db
#     con.commit()
#     #close connection
#     con.close()

#     # clear text boxes
#     f_name.delete(0, END)
#     l_name.delete(0, END)
#     address.delete(0, END)
#     city.delete(0, END)
#     state.delete(0, END)
#     zipcode.delete(0, END)

# submit_button = Button(root, text = "Add Record to Database", command = submit)
# submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# # Create Query button
# def query():
#     # create a database or connect to one
#     con = sqlite3.connect("address_book.db")
#     # create cursor -> a cursor sends the result to the db
#     c = con.cursor()
#     c.execute("SELECT *, oid FROM addresses") #oid is the primary key
#     records = c.fetchall()
#     # print(records) # print does not work in TKinter but it prints in the terminal when the Show Records button is clicked.

#     # Loop through results
#     print_records = ""
#     for record in records:
#         print_records += str(record) + "\n"

#     query_label = Label(root, text = print_records)
#     query_label.grid(row = 8, column = 0, columnspan = 2)

#     # Commit changes -> commiting changes to the db
#     con.commit()
#     #close connection
#     con.close()

# query_button = Button(root, text = "Show Records", command =  query)
# query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# # Commit changes -> commiting changes to the db
# con.commit()

# #close connection
# con.close()

# mainloop()



from tkinter import *
from PIL import ImageTk, Image 
import sqlite3

root = Tk()
root.title("Learn To Code")
root.iconbitmap("logo_image.ico")
root.geometry("400x400")

# create a database or connect to one
con = sqlite3.connect("address_book.db")

# create cursor -> a cursor sends the result to the db
c = con.cursor()

### We already created the table
### create table 
# c.execute("""
# CREATE TABLE addresses(
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text, 
#           zipcode integer
# )""")

# Create text boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)

l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1, padx = 20)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 20)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 20)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 20)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 20)

# Create text box labels
f_name_label = Label(root, text = "First Name")
f_name_label.grid(row = 0, column = 0)

l_name_label = Label(root, text = "Last Name")
l_name_label.grid(row = 1, column = 0)

address_label = Label(root, text = "Address")
address_label.grid(row = 2, column = 0)

city_label = Label(root, text = "City")
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = "State")
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text = "Zipcode")
zipcode_label.grid(row = 5, column = 0)

# create Submit button
def submit():
    # create a database or connect to one
    con = sqlite3.connect("address_book.db")
    # create cursor -> a cursor sends the result to the db
    c = con.cursor()
    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", # can me like (:a,...:f), same should be used in the dict below
             {
                "f_name": f_name.get(), 
                "l_name":l_name.get(),
                "address": address.get(),
                "city": city.get(),
                "state": state.get(),
                "zipcode": zipcode.get()
             })

    # Commit changes -> commiting changes to the db
    con.commit()
    #close connection
    con.close()

    # clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

submit_button = Button(root, text = "Add Record to Database", command = submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Create Query button
def query():
    # create a database or connect to one
    con = sqlite3.connect("address_book.db")
    # create cursor -> a cursor sends the result to the db
    c = con.cursor()
    c.execute("SELECT *, oid FROM addresses") #oid is the primary key
    records = c.fetchall()
    # print(records) # print does not work in TKinter but it prints in the terminal when the Show Records button is clicked.

    # Loop through results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1])  + "\n"

    query_label = Label(root, text = print_records)
    query_label.grid(row = 8, column = 0, columnspan = 2)

    # Commit changes -> commiting changes to the db
    con.commit()
    #close connection
    con.close()

query_button = Button(root, text = "Show Records", command =  query)
query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

# Commit changes -> commiting changes to the db
con.commit()

#close connection
con.close()

mainloop()
