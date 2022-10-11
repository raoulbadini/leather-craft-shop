from tkinter import *
#####   LIBARARIES IMPORTED ####
import tkinter as tk
# from Tkinter import *
# import Tkinter
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter.messagebox import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
def CHECK():
    root.destroy()
    from checkout import window2

def View():

    con1 = sqlite3.connect("mein.db")

    cur1 = con1.cursor()

    cur1.execute("SELECT * FROM CART")

    rows = cur1.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row)        

    con1.close()


# connect to the database

root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="NAME")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="QUANTITY")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="COST")
tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="$TOTAL")

tree.pack()

button1 = tk.Button(text="Display CART",bg='red', command=View)

button1.pack(pady=10)
button1 = tk.Button(text="CHECK-OUT"'💳',bg='green',command=CHECK)

button1.pack(pady=15)

root.mainloop()
