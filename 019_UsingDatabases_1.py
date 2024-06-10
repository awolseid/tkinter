### Using Databases

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

# create table
c.execute("""
CREATE TABLE addresses(
          first_name text,
          last_name text,
          address text,
          city text,
          state text, 
          zipcode integer
)""")



# Commit changes -> commiting changes to the db
con.commit()

#close connection
con.close()

mainloop()