#####   LIBARARIES IMPORTED ####
from tkinter import *
import tkinter as tk
import tkinter
# from Tkinter import *
# import Tkinter
from tkinter.messagebox import askyesno
from tkinter.messagebox import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

#####   LIBARARIES IMPORTED ####


window1 = tk.Tk()
window1.geometry("600x600")
window1.title("ORDERING SYSTEM")
window1.maxsize(600,600)
window1.minsize(600,600)
window1.configure()
def cartt():
    window1.destroy()
    import cart
def sb():
    window1.destroy()
    import sb
def sa():
    window1.destroy()
    import sa
def up():
    window1.destroy()
    import signupmain
def about():
    showinfo("ABOUT-US","VERSION 1.0 MADE by B. Raoul cyber-security student at IvyTech school of IT for SEDV140 final project due on 10/10/2022 (PYTHON GUI app)")
def QU():
    answer = askyesno("BYE", 'Are you sure that you want to quit?')
    if answer==True:
        window1.destroy()
        import loginmain

user = tk.StringVar()
passw = tk.StringVar()
# keys = tk.StringVar()

main1=tk.Label(window1,text="MADE IN THE US | LIFETIME WARANTY | BEST PRODUCTS",font=("times new roman",16))
main1.pack()
main2=tk.Label(window1,text=" THE LEATHER CRAFT COMPANY 💼",fg="red",font=("times new roman",16))
main2.pack()
# image1 = Image.open("NEW.png")
# test = ImageTk.PhotoImage(image1)
# label1 = tk.Label(image=test)
# label1.image = test

# # Position image
# label1.pack()
### USERID ##3
# userid=tk.Label(window1,text="Username",font=("times new roman",16))
# userid.place(x=50,y=150)
# useride = tk.Entry(window1, textvariable=user,width=20,font=("times new roman",16))
# useride.place(x=150,y=150)
# ## PASSWORD ##
# password=tk.Label(window1,text="Password",font=("times new roman",16))
# password.place(x=50,y=210)
# passworde = tk.Entry(window1, textvariable=passw,width=20,font=("times new roman",16),show="*")
# passworde.place(x=150,y=210)
### BUTTON ##


main3=tk.Label(window1,text="MENU",width=18,font=("times new roman",16))
main3.pack()
subm1=tk.Button(window1,text="SIGNUP",bg="lightblue",width=18,font=("times new roman",13),command=up)
subm1.pack()
subm2=tk.Button(window1,text="ABOUT US",bg="yellow",width=18,font=("times new roman",13),command=about)
subm2.pack()
subm3=tk.Button(window1,text="SHOPS-BAGS",bg="blue",width=18,font=("times new roman",13),command=sb)
subm3.pack()
subm4=tk.Button(window1,text="SHOP-ACCESSORIES",bg="yellow",width=18,font=("times new roman",13),command=sa)
subm4.pack()

# subm5.pack()
# subm6=tk.Button(window1,text="DISCOUNTS",bg="lightblue",font=("times new roman",13),command=sa)
# subm6.pack()
cart=tk.Button(window1,text="CART",bg='lightgreen',width=18,font=("times new roman",13),command=cartt)
cart.pack()

quitb=tk.Button(window1,text="LOGOUT",bg='red',width=18,font=("times new roman",13),command=QU)
quitb.pack()

window1.mainloop()
