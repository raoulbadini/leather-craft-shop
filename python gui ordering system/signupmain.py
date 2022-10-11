#####   LIBARARIES IMPORTED ####
import tkinter as tk
from tkinter.constants import S
# from Tkinter import *
# import Tkinter

from tkinter.messagebox import askyesno
from tkinter.messagebox import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

#####   LIBARARIES IMPORTED ####


signupp = tk.Tk()
signupp.geometry("400x400")
signupp.title("ORDERING SYSTEM")
signupp.maxsize(400,400)
signupp.minsize(400,400)
signupp.configure()
def work():
    if (user.get()) and (passw.get()):
        conn = sqlite3.connect('mein.db')
        cursor = conn.cursor()
        sql = ('''INSERT INTO LOGIN(username,password) VALUES(?,?);''')
        cursor.execute(sql,(user.get(),passw.get()))
        messagebox.showinfo("showinfo", "SUCCESSFULL")
        conn.commit()
        conn.close()
    else:
        messagebox.showinfo("showinfo", "Field missing")
def QU():
    answer = askyesno("BYE", 'Are you sure that you want to quit?')
    if answer==True:
        signupp.quit()
def BACK():
    signupp.destroy()
    from main import window1

user = tk.StringVar()
passw = tk.StringVar()
# keys = tk.StringVar()
main=tk.Label(signupp,text="ORDERING SYSTEM",font=("times new roman",26))
main.pack()
### USERID ##3
userid=tk.Label(signupp,text="Username",font=("times new roman",16))
userid.place(x=50,y=150)
useride = tk.Entry(signupp, textvariable=user,width=20,font=("times new roman",16))
useride.place(x=150,y=150)
## PASSWORD ##
password=tk.Label(signupp,text="Password",font=("times new roman",16))
password.place(x=50,y=210)
passworde = tk.Entry(signupp, textvariable=passw,width=20,font=("times new roman",16),show="*")
passworde.place(x=150,y=210)
## KEYWORD  ##
# image1 = Image.open("NEW.png")
# test = ImageTk.PhotoImage(image1)

# label1 = tk.Label(image=test)
# label1.image = test

# # Position image
# label1.pack()
### BUTTON ##
subm=tk.Button(signupp,text="SIGNUP",bg="green",font=("times new roman",13),command=work)
subm.place(x=150,y=250)
quitb=tk.Button(signupp,text="QUIT",bg='red',font=("times new roman",13),command=QU)
quitb.place(x=150,y=300)
quitb=tk.Button(signupp,text="BACK",bg='red',font=("times new roman",13),command=BACK)
quitb.place(x=150,y=350)
signupp.mainloop()
