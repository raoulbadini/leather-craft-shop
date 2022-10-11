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


sbb = tk.Tk()
sbb.geometry("650x650")
sbb.title("ORDERING SYSTEM")
sbb.maxsize(650,650)
sbb.minsize(650,650)
sbb.configure()
def BACK():
    sbb.destroy()
    from main import window1
    
    
def AD1():
    if BG1:
        iname="AVERY LEATHER TOTE BAG"
        cost=250
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
        iname="AVERY LEATHER NOTE BAG"
        cost=255
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
        iname="HARRIS LEATHER BRIEFCASE"
        cost=525
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
    sbb.destroy()
    import cart

BG1 = tk.StringVar()
BG2 = tk.StringVar()
BG3 = tk.StringVar()
# keys = tk.StringVar()
main=tk.Label(sbb,text="SHOP-BAGS",font=("times new roman",26))
main.pack()
### USERID ##3
## KEYWORD  ##
image1 = Image.open("sb11.jpg")

test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test

# Position image
label1.place(x=30,y=100)
image2 = Image.open("sb12.jpg")

test = ImageTk.PhotoImage(image2)

label2 = tk.Label(image=test)
label2.image = test
label2.place(x=400,y=100)

###
image3 = Image.open("BRIEF.jpg")

test = ImageTk.PhotoImage(image3)

label3 = tk.Label(image=test)
label3.image = test
label3.place(x=220,y=400)
###

BG1 = tk.Entry(sbb, textvariable=BG1,width=8,font=("times new roman",16))
BG1.place(x=65,y=210)
BG2 = tk.Entry(sbb, textvariable=BG2,width=8,font=("times new roman",16))
BG2.place(x=430,y=210)
BG3 = tk.Entry(sbb, textvariable=BG3,width=8,font=("times new roman",16))
BG3.place(x=250,y=510)

# Position image
main2=tk.Label(sbb,text="AVERY LEATHER TOTE BAG",font=("times new roman",12))
main2.place(x=15,y=50)
main3=tk.Label(sbb,text="AVERY LEATHER NOTE BAG",font=("times new roman",12))
main3.place(x=370,y=50)
main44=tk.Label(sbb,text="HARRIS LEATHER BRIEFCASE",font=("times new roman",12))
main44.place(x=200,y=330)

main4=tk.Label(sbb,text="$250",font=("times new roman",12))
main4.place(x=115,y=70)
main5=tk.Label(sbb,text="$255",font=("times new roman",12))
main5.place(x=450,y=70)
main55=tk.Label(sbb,text="$525",font=("times new roman",12))
main55.place(x=280,y=360)
### BUTTON ##
subm=tk.Button(sbb,text="ADD-TO-CART",bg="red",font=("times new roman",13),command=AD1)
subm.place(x=40,y=250)
subm1=tk.Button(sbb,text="ADD-TO-CART",bg="red",font=("times new roman",13),command=AD2)
subm1.place(x=400,y=250)
subm2=tk.Button(sbb,text="ADD-TO-CART",bg="red",font=("times new roman",13),command=AD2)
subm2.place(x=230,y=550)
quitb=tk.Button(sbb,text="BACK",bg='red',font=("times new roman",13),command=BACK)
quitb.place(x=260,y=600)
quitb1=tk.Button(sbb,text='🛒'"CART",bg="red",font=("times new roman",13),command=QU)
quitb1.place(x=480,y=00)
sbb.mainloop()
