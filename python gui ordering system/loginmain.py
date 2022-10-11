#####   LIBARARIES IMPORTED ####
import tkinter as tk
# from Tkinter import *
# import Tkinter
from tkinter.messagebox import askyesno
from tkinter.messagebox import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
# from main import main
#####   LIBARARIES IMPORTED ####


loggin = tk.Tk()
loggin.geometry("400x400")
loggin.title("ORDERING SYSTEM")
loggin.maxsize(400,400)
loggin.minsize(400,400)
loggin.configure()
def work():
    if (user.get()) and (passw.get()):
        conn = sqlite3.connect('mein.db')
        cursor = conn.cursor()
        sql = ('''SELECT * FROM LOGIN WHERE Username = ? and Password = ?;''')
        cursor.execute(sql,(user.get(),passw.get()))
        row=cursor.fetchone()
        if row==None:
            messagebox.showinfo("showinfo", "SORRY WRONG USERNAME PASSWORD")
        else:
            messagebox.showinfo("showinfo", "SUCCESSFULL")
            loggin.destroy()
            import main

        conn.commit()
        conn.close()
        
    else:
        messagebox.showinfo("showinfo", "Field missing")
def QU():
    answer = askyesno("BYE", 'Are you sure that you want to quit?')
    if answer==True:
        loggin.destroy()

user = tk.StringVar()
passw = tk.StringVar()
# keys = tk.StringVar()
main=tk.Label(loggin,text="ORDERING SYSTEM",font=("times new roman",26))
main.pack()
### USERID ##3
userid=tk.Label(loggin,text="Username",font=("times new roman",16))
userid.place(x=50,y=150)
useride = tk.Entry(loggin, textvariable=user,width=20,font=("times new roman",16))
useride.place(x=150,y=150)
## PASSWORD ##
password=tk.Label(loggin,text="Password",font=("times new roman",16))
password.place(x=50,y=210)
passworde = tk.Entry(loggin, textvariable=passw,width=20,font=("times new roman",16),show="*")
passworde.place(x=150,y=210)
## KEYWORD  ##
# image1 = Image.open("NEW.png")
# test = ImageTk.PhotoImage(image1)

# label1 = tk.Label(image=test)
# label1.image = test

# # Position image
# label1.pack()
### BUTTON ##
subm=tk.Button(loggin,text="LOGIN",bg="green",font=("times new roman",13),command=work)
subm.place(x=150,y=250)
quitb=tk.Button(loggin,text="QUIT",bg='red',font=("times new roman",13),command=QU)
quitb.place(x=150,y=300)
loggin.mainloop()
