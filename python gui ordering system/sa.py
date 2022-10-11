#####   LIBARARIES IMPORTED ####

from os import name
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



sa = tk.Tk()
sa.geometry("650x650")
sa.title("ORDERING SYSTEM")
sa.maxsize(650,650)
sa.minsize(650,650)
sa.configure()
def BACK():
    sa.destroy()
    import main
def AD1():
    if BG1:
        iname="CLASSIC HANDMADE LEATHER BELT"
        cost=75
        total=cost*int(BG1.get())
        conn = sqlite3.connect('mein.db')
        cursor = conn.cursor()
        sql = ('''INSERT INTO CART(INAME,QUANTITY,COST,TOTAL) VALUES(?,?,?,?);''')
        cursor.execute(sql,(iname,BG1.get(),cost,total))
        messagebox.showinfo("showinfo", "SUCCESSFULL")
        conn.commit()
        conn.close()
    else:
        print("error")
def AD2():
    if BG2:
        iname="STANDARD LEATHER WALLET"
        cost=80
        total=cost*int(BG2.get())
        conn = sqlite3.connect('mein.db')
        cursor = conn.cursor()
        sql = ('''INSERT INTO CART(INAME,QUANTITY,COST,TOTAL) VALUES(?,?,?,?);''')
        cursor.execute(sql,(iname,BG2.get(),cost,total))
        messagebox.showinfo("showinfo", "SUCCESSFULL")
        conn.commit()
        conn.close()
    else:
        print("error")
def AD3():
    if BG3:
        iname="SCRIPT LOGO T-SHIRT"
        cost=25
        total=cost*int(BG3.get())
        conn = sqlite3.connect('mein.db')
        cursor = conn.cursor()
        sql = ('''INSERT INTO CART(INAME,QUANTITY,COST,TOTAL) VALUES(?,?,?,?);''')
        cursor.execute(sql,(iname,BG3.get(),cost,total))
        messagebox.showinfo("showinfo", "SUCCESSFULL")
        conn.commit()
        conn.close()
    else:
        print("error")
def QU():
    sa.destroy()
    import cart
    
BG1 = tk.StringVar()
BG2 = tk.StringVar()
BG3 = tk.StringVar()
# keys = tk.StringVar()
main=tk.Label(sa,text="SHOP-ACCESSORIES",font=("times new roman",22))
main.pack()
### USERID ##3
## KEYWORD  ##
image1 = Image.open("belt.jpg")

test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test


label1.place(x=60,y=100)
#####  
image2 = Image.open("purse1.jpg")

test = ImageTk.PhotoImage(image2)

label2 = tk.Label(image=test)
label2.image = test
label2.place(x=400,y=100)

image3 = Image.open("shirt.png")

test = ImageTk.PhotoImage(image3)

label3 = tk.Label(image=test)
label3.image = test
label3.place(x=170,y=340)




BG1 = tk.Entry(sa, textvariable=BG1,width=8,font=("times new roman",16))
BG1.place(x=65,y=210)
BG2 = tk.Entry(sa, textvariable=BG2,width=8,font=("times new roman",16))
BG2.place(x=430,y=210)
BG3 = tk.Entry(sa, textvariable=BG3,width=8,font=("times new roman",16))
BG3.place(x=250,y=510)

# Posation image
main2=tk.Label(sa,text="CLASSIC HANDMADE LEATHER BELT",font=("times new roman",12))
main2.place(x=15,y=50)
main3=tk.Label(sa,text="STANDARD LEATHER WALLET",font=("times new roman",12))
main3.place(x=370,y=50)
main44=tk.Label(sa,text="SCRIPT LOGO T-SHIRT",font=("times new roman",12))
main44.place(x=210,y=300)

main4=tk.Label(sa,text="$65",font=("times new roman",12))
main4.place(x=115,y=70)
main5=tk.Label(sa,text="$75",font=("times new roman",12))
main5.place(x=450,y=70)
main55=tk.Label(sa,text="$25",font=("times new roman",12))
main55.place(x=280,y=320)
### BUTTON ##
subm=tk.Button(sa,text="ADD-TO-CART",bg="red",font=("times new roman",13),command=AD1)
subm.place(x=40,y=250)
subm1=tk.Button(sa,text="ADD-TO-CART",bg="red",font=("times new roman",13),command=AD2)
subm1.place(x=420,y=250)
subm2=tk.Button(sa,text="ADD-TO-CART",bg="red",font=("times new roman",13),command=AD3)
subm2.place(x=230,y=550)
quitb=tk.Button(sa,text="BACK",bg='red',font=("times new roman",13),command=BACK)
quitb.place(x=260,y=600)
quitb1=tk.Button(sa,text='🛒'"CART",bg='red',font=("times new roman",13),command=QU)
quitb1.place(x=480,y=00)
sa.mainloop()
