from tkinter import *
import sqlite3
import datetime
t=Tk()
t.configure(background='white')
t.title("Library Management System")
t.geometry('700x700')
linkc=sqlite3.connect('lms.db')

def a(event=None):
    linkc=sqlite3.connect('lms.db')
    e1.delete(0,"end")
    e2.delete(0,"end")
    e3.delete(0,"end")
    l11.configure(text="")
    p=e.get()
    r=(p,)
    c=linkc.execute('SELECT name,id,phone,fine,book1_name,book2_name,last_date_of_return1,last_date_of_return2 from root WHERE id=?',r)
    data=c.fetchall()
    if data==[]:
        l1.configure(text="NO DATA!!")
        return
    ctr=len(data[0])
    f=data[0]
    sd=""
    for i in range(ctr):
        if i==0:
            sd=sd+"Name :  "+str(f[i])+"\n"
        elif i==1:
            sd=sd+"ID :  "+str(f[i])+"\n"
        elif i==2:
            sd=sd+"Phone :  "+str(f[i])+"\n"
        elif i==3 :
            sd=sd+"Fine :  "+str(f[i])+"\n"
        elif i==4 :
            sd=sd+"Book 1 name :  "+str(f[i])+"\n"
        elif i==5 :
            sd=sd+"Book 2 name :  "+str(f[i])+"\n"
        elif i==6 :
            sd=sd+"Last date of submittion for book 1 :  "+str(f[i])+"\n"
        else:
            sd=sd+"Last date of submittion for book 2:  "+str(f[i])+"\n"
    l1.configure(text=(sd))
    l13.configure(text="")
    linkc.close()

def sub():
    n=e1.get()
    i=e2.get()
    p=int(e3.get())
    d1=t=datetime.date.today() + datetime.timedelta(days=10)
    linkc=sqlite3.connect('lms.db')
    linkc.execute('insert into root VALUES(?,?,?,NULL,NULL,NULL,NULL,NULL)',(n,i,p))
    l11.configure(text="Submitted Successfully")
    l1.configure(text="")
    linkc.commit()
    linkc.close()

def issue1():
    book2=e5.get()
    ii=e7.get()
    linkc=sqlite3.connect('lms.db')
    d1=t=datetime.date.today() + datetime.timedelta(days=10)
    linkc.execute('update root SET book1_name=? where id=?',(book2,ii))
    linkc.execute('update root SET last_date_of_return1=? where id=?',(d1,ii))
    linkc.commit()
    linkc.close()
    l13.configure(text="BOOK1 ISSUED")

def issue2():
    book2=e6.get()
    ii=e7.get()
    linkc=sqlite3.connect('lms.db')
    d1=t=datetime.date.today() + datetime.timedelta(days=10)
    linkc.execute('update root SET book2_name=? where id=?',(book2,ii))
    linkc.execute('update root SET last_date_of_return2=? where id=?',(d1,ii))
    linkc.commit()
    linkc.close()
    l13.configure(text="BOOK2 ISSUED")

def ret1():
    ii=e7.get()
    linkc=sqlite3.connect('lms.db')
    linkc.execute('update root SET book1_name=NULL where id=?',(ii,))
    linkc.execute('update root SET last_date_of_return1=NULL where id=?',(ii,))
    linkc.commit()
    linkc.close()
    l13.configure(text="BOOK1 RETURNED")

def ret2():
    ii=e7.get()
    linkc=sqlite3.connect('lms.db')
    linkc.execute('update root SET book2_name=NULL where id=?',(ii,))
    linkc.execute('update root SET last_date_of_return2=NULL where id=?',(ii,))
    linkc.commit()
    linkc.close()
    l13.configure(text="BOOK2 RETURNED")

menu=Menu(t)
t.config(menu=menu)
fm=Menu(menu)
menu.add_cascade(label="File",menu=fm)
fm.add_command(label="Search ID",command=a)
fm.add_command(label="Submit New Entry",command=sub)
fm.add_separator()
fm.add_command(label="Exit", command=t.destroy)
hm=Menu(menu)
menu.add_cascade(label="Help",menu=hm)
hm.add_command(label="About")
t.bind('<Return>',a)

l8=Label(t,text="ENTER ID TO SEARCH",)
l8.place(x=20,y=20)

l=Label(t,text="Enter ID :",)
l.place(x=20,y=52)

e=Entry(t)
e.place(x=80,y=52)

b=Button(t,text="Search",command=a,bg="light green",activebackground="red",bd=5)
b.place(x=50,y=80)

l1=Label(t,text="")
l1.place(x=20,y=110)

l2=Label(t,text="CREATE NEW ENTRY",)
l2.place(x=350,y=20)

l3=Label(t,text="NAME :")
l3.place(x=350,y=45)

e1=Entry(t)
e1.place(x=450,y=45)

l4=Label(t,text="ID :")
l4.place(x=370,y=70)

e2=Entry(t)
e2.place(x=450,y=75)

l5=Label(t,text="Phone no:")
l5.place(x=350,y=100)

e3=Entry(t)
e3.place(x=450,y=100)

l7=Label(t,text="Book1 Name :")
l7.place(x=20,y=320)

e5=Entry(t)
e5.place(x=110,y=320)

l12=Label(t,text="Book2 Name :")
l12.place(x=20,y=340)

e6=Entry(t)
e6.place(x=100,y=350)

b1=Button(t,text="Submit",command=sub,bg="light green",activebackground="red",bd=5)
b1.place(x=350,y=180)

l11=Label(t,text="")
l11.place(x=400,y=200)

l9=Label(t,text="ENTER ID TO ISSUE OR SUBMIT BOOKS",font="Times 15 bold")
l9.place(x=20,y=245)

l12=Label(t,text="Enter ID :")
l12.place(x=20,y=290)

e7=Entry(t)
e7.place(x=90,y=300)

b2=Button(t,text="Issue",command=issue1,bg="light green",activebackground="red",bd=5)
b2.place(x=250,y=320)

b3=Button(t,text="Issue",command=issue2,bg="light green",activebackground="red",bd=5)
b3.place(x=250,y=350)

b4=Button(t,text="Return Book 1",command=ret1,bg="light green",activebackground="red",bd=5)
b4.place(x=120,y=380)

b5=Button(t,text="Return Book 2",command=ret2,bg="light green",activebackground="red",bd=5)
b5.place(x=320,y=380)

l13=Label(t,text="")
l13.place(x=60,y=395)

t.mainloop()
