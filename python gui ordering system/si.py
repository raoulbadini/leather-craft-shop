# #####   LIBARARIES IMPORTED ####

# from os import name
# import tkinter as tk
# # from Tkinter import *
# # import Tkinter
# from tkinter.messagebox import askyesno
# from tkinter.messagebox import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import sqlite3
# # from main import main
# #####   LIBARARIES IMPORTED ####


# si = tk.Tk()
# si.geometry("700x700")
# si.title("ORDERING SYSTEM")
# si.maxsize(600,600)
# si.minsize(600,600)
# si.configure()
# def BACK():
#     si.destroy()
#     import main
# def AD1():
#     if BG1:
#         iname="ACLASSIC HANDMADE LEATHER BELT"
#         cost=75
#         total=cost*int(BG1.get())
#         conn = sqlite3.connect('mein.db')
#         cursor = conn.cursor()
#         sql = ('''INSERT INTO CART(INAME,QUANTITY,COST,TOTAL) VALUES(?,?,?,?);''')
#         cursor.execute(sql,(iname,BG1.get(),cost,total))
#         messagebox.showinfo("showinfo", "SUCCESSFULL")
#         conn.commit()
#         conn.close()
#     else:
#         print("error")
# def AD2():
#     if BG2:
#         iname="STANDARD LEATHER WALLET"
#         cost=80
#         total=cost*int(BG2.get())
#         conn = sqlite3.connect('mein.db')
#         cursor = conn.cursor()
#         sql = ('''INSERT INTO CART(INAME,QUANTITY,COST,TOTAL) VALUES(?,?,?,?);''')
#         cursor.execute(sql,(iname,BG2.get(),cost,total))
#         messagebox.showinfo("showinfo", "SUCCESSFULL")
#         conn.commit()
#         conn.close()
#     else:
#         print("error")
# def AD3():
#     if BG3:
#         iname="STANDARD LEATHER WALLET"
#         cost=85
#         total=cost*int(BG3.get())
#         conn = sqlite3.connect('mein.db')
#         cursor = conn.cursor()
#         sql = ('''INSERT INTO CART(INAME,QUANTITY,COST,TOTAL) VALUES(?,?,?,?);''')
#         cursor.execute(sql,(iname,BG2.get(),cost,total))
#         messagebox.showinfo("showinfo", "SUCCESSFULL")
#         conn.commit()
#         conn.close()
#     else:
#         print("error")
# def QU():
#     si.destroy()
#     import cart
    
# BG1 = tk.StringVar()
# BG2 = tk.StringVar()
# BG3 = tk.StringVar()
# # keys = tk.StringVar()
# main=tk.Label(si,text="SPECIAL ITEMS",font=("times new roman",22))
# main.pack()
# ### USERID ##3
# ## KEYWORD  ##
# image1 = Image.open("belt.jpg")

# test = ImageTk.PhotoImage(image1)

# label1 = tk.Label(image=test)
# label1.image = test


# label1.place(x=60,y=100)
# #####  
# image2 = Image.open("purse1.jpg")

# test = ImageTk.PhotoImage(image2)

# label2 = tk.Label(image=test)
# label2.image = test
# label2.place(x=280,y=100)
# BG1 = tk.Entry(si, textvariable=BG1,width=8,font=("times new roman",16))
# BG1.place(x=65,y=210)
# BG2 = tk.Entry(si, textvariable=BG2,width=8,font=("times new roman",16))
# BG2.place(x=430,y=210)
# BG3 = tk.Entry(si, textvariable=BG3,width=8,font=("times new roman",16))
# BG3.place(x=250,y=450)

# # Position image
# main2=tk.Label(si,text="SPECIAL ITEM 1",font=("times new roman",12))
# main2.place(x=70,y=50)
# main3=tk.Label(si,text="SPECIAL ITEM 2",font=("times new roman",12))
# main3.place(x=390,y=50)
# main44=tk.Label(si,text="SPECIAL ITEM 3",font=("times new roman",12))
# main44.place(x=230,y=300)

# main4=tk.Label(si,text="$75",font=("times new roman",12))
# main4.place(x=115,y=70)
# main5=tk.Label(si,text="$80",font=("times new roman",12))
# main5.place(x=450,y=70)
# main55=tk.Label(si,text="$85",font=("times new roman",12))
# main55.place(x=280,y=320)
# ### BUTTON ##
# subm=tk.Button(si,text="ADD-TO-CART",bg="red",font=("times new roman",13),command=AD1)
# subm.place(x=40,y=250)
# subm1=tk.Button(si,text="ADD-TO-CART",bg="red",font=("times new roman",13),command=AD2)
# subm1.place(x=420,y=250)
# subm2=tk.Button(si,text="ADD-TO-CART",bg="red",font=("times new roman",13),command=AD2)
# subm2.place(x=230,y=490)
# quitb=tk.Button(si,text="BACK",bg='red',font=("times new roman",13),command=BACK)
# quitb.place(x=260,y=530)
# quitb1=tk.Button(si,text="CART",bg='red',font=("times new roman",13),command=QU)
# quitb1.place(x=420,y=00)
# si.mainloop()


A=''
B=['Raoul,Badini']
for i in range(len(B)):
    if i==0:
        A=A+B[i]
    else:
        A=A+','+B[i]
print(A)
