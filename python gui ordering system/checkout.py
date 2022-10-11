#####   LIBARARIES IMPORTED ####
from tkinter import *
import tkinter as tk
# from Tkinter import *
# import Tkinter
from tkinter.messagebox import askyesno
from tkinter.messagebox import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

#####   LIBARARIES IMPORTED ####


window2 = tk.Tk()
window2.geometry("600x600")
window2.title("ORDERING SYSTEM")
window2.maxsize(600,600)
window2.minsize(600,600)
window2.configure()
def che():
    main3e.configure(state="normal")
def work():
    if emails.get() and finame.get() and laname.get() and addresss.get() and cityi.get() and count.get() and states.get() and zipc.get() and phones.get():
        conn = sqlite3.connect('mein.db')
        cursor = conn.cursor()
        sql = ('''SELECT * FROM CART''')
        cursor.execute(sql,)
        b=cursor.fetchall()
        a=[]
        c=[]
        d=[]
        for i in range(len(b)):
            a.append(b[i][0])
            c.append(b[i][1])
            d.append(b[i][3])
        print(a)
        print(c)
        print(d)
        conn.commit()
        conn.close()
        A=''
        C=''
        D=''
        for i in range(len(a)):
            if i==0:
                A=A+a[i]
            else:
                A=A+','+a[i]
        
        for i in range(len(c)):
            if i==0:
                C=C+c[i]
            else:
                C=C+','+c[i]
        for i in range(len(d)):
            if i==0:
                D=D+d[i]
            else:
                D=D+','+d[i]
        total=0
        for i in range(len(d)):
            total=total+int(d[i])
        try:
            conn = sqlite3.connect('mein.db')
            cursor = conn.cursor()
            sql = ('''INSERT INTO CHECKOUT(FNAME,LNAME,ADDRESS,APARTMENT,CITY,COUNTRY,STATE,ZIPCODE,PHONE,EMAIL,ITEMNAMES,QUANTITY,TOTAL) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);''')
            cursor.execute(sql,(finame.get(),laname.get(),addresss.get(),apartment.get(),cityi.get(),count.get(),states.get(),zipc.get(),phones.get(),emails.get(),A,C,str(total)))
            messagebox.showinfo("showinfo", "SUCCESSFULL")
            conn.commit()
            conn.close()
            con1 = sqlite3.connect("mein.db")

            cur1 = con1.cursor()
            cur1.execute("DELETE FROM CART")
            con1.commit()
            con1.close()
            window2.destroy()
            from main import window1
        except Exception as error:
            print(error)
    else:
        showwarning("ERROR","MISSING FIELD ERROR")
finame = tk.StringVar()
laname = tk.StringVar()
addresss = tk.StringVar()
cityi = tk.StringVar()
count = tk.StringVar()
states = tk.StringVar()
zipc = tk.StringVar()
phones = tk.StringVar()
emails = tk.StringVar()
apartment = tk.StringVar()
var1=tk.IntVar()
####3
ch= Checkbutton(window2, text = "IF WANT UPDATES", variable = var1,onvalue = 1, offvalue = 0,width = 20,command=che)
ch.place(x=380,y=30)
main1=tk.Label(window2,text="CHECKOUT",font=("times new roman",22))
main1.pack()
main3=tk.Label(window2,text="CONTACT-EMAIL",font=("times new roman",16))
main3.place(x=0,y=30)
main3e = tk.Entry(window2, textvariable=emails,width=20,state='disabled',font=("times new roman",12))
main3e.place(x=190,y=30)

button1 = tk.Button(text="CHECK-OUT"'💳',bg='red',command=work)

button1.place(x=420,y=220)

main2=tk.Label(window2,text="SHIPPING-INFORMATION",fg="red",font=("times new roman",22))
main2.place(x=30,y=60)
# # Position image
# label1.pack()
### USERID ##3
fname=tk.Label(window2,text="FISRT-NAME",font=("times new roman",16))
fname.place(x=30,y=100)
fnamee = tk.Entry(window2, textvariable=finame,width=20,font=("times new roman",16))
fnamee.place(x=160,y=100)
lname=tk.Label(window2,text="LAST-NAME",font=("times new roman",16))
lname.place(x=30,y=160)
lnamee = tk.Entry(window2, textvariable=laname,width=20,font=("times new roman",16))
lnamee.place(x=160,y=160)
address=tk.Label(window2,text="ADDRESS",font=("times new roman",16))
address.place(x=30,y=220)
addresse = tk.Entry(window2, textvariable=addresss,width=20,font=("times new roman",16))
addresse.place(x=160,y=220)
apart=tk.Label(window2,text="APARTMENT",font=("times new roman",16))
apart.place(x=30,y=280)
aparte = tk.Entry(window2, textvariable=apartment,width=20,font=("times new roman",16))
aparte.place(x=160,y=280)
city=tk.Label(window2,text="CITY",font=("times new roman",16))
city.place(x=30,y=340)
citye = tk.Entry(window2, textvariable=cityi,width=20,font=("times new roman",16))
citye.place(x=160,y=340)
country=tk.Label(window2,text="COUNTRY",font=("times new roman",16))
country.place(x=30,y=400)
countrye = tk.Entry(window2, textvariable=count,width=20,font=("times new roman",16))
countrye.place(x=160,y=400)
state=tk.Label(window2,text="STATE",font=("times new roman",16))
state.place(x=30,y=460)
statee = tk.Entry(window2, textvariable=states,width=20,font=("times new roman",16))
statee.place(x=160,y=460)
zipl=tk.Label(window2,text="ZIP-CODE",font=("times new roman",16))
zipl.place(x=30,y=510)
zipe = tk.Entry(window2, textvariable=zipc,width=20,font=("times new roman",16))
zipe.place(x=160,y=510)
phone=tk.Label(window2,text="PHONE",font=("times new roman",16))
phone.place(x=30,y=560)
phonee = tk.Entry(window2, textvariable=phones,width=20,font=("times new roman",16))
phonee.place(x=160,y=560)






window2.mainloop()
