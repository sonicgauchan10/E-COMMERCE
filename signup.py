from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter.font as font
import runpy
import sqlite3
import subprocess
 
#creating project after the logs in
project=Tk()
project.configure(bg="white")
project.attributes("-fullscreen",True)
img = Image.open("bg2.jpg")
bg_image = ImageTk.PhotoImage(img)
bg_label = Label(project, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
 
#creating title bar
a=Frame(project,width=1550,height=33,bg="#57a1f8").place(x=0,y=0)
title=Label(a, text="BSLR PHARMACY",font=("Microsoft Yahei UI Light",20,"bold"), bg="white").place(x=50,y=0)
img=Image.open(r"logo.png") #image logo
img=img.resize((30,30))
new_logo=ImageTk.PhotoImage(img)
image=Label(image=new_logo,border=0,bg="#57a1f8").place(x=5,y=3)
screen_width = project.winfo_screenwidth()
screen_height=project.winfo_screenheight()
 
#making maximize and minimize button manually
def min():
    project.iconify()
def on_enter(i):
    btn2['background']="red"
def on_leave(i):
    btn2['background']="grey"
def max():
    msg_box =messagebox.askquestion('Exit Application', 'Do you want to leave?',icon='warning')
    if msg_box == 'yes':
        project.destroy()

btn2=Button(a,text="✕", command=max,width=4,bg="#57a1f8",border=0,font=Button)
btn2.pack(anchor="ne")
btn2.bind('<Enter>',on_enter)
btn2.bind('<Leave>',on_leave)
btn=Button(a,text="-", command=min,width=4,bg="#57a1f8",border=0,font=Button)
btn.place(x=screen_width-100,y=0)
def enter(i):
    btn['background']="red"
def leave(i):
    btn['background']="grey"
btn.bind('<Enter>',enter)
btn.bind('<Leave>',leave)

#back_button
def back():
    project.destroy()
    runpy.run_path(
        "final_base.py")
btn4=Button(project,text="<<",width=4,bg="#57a1f8",border=0,font=Button,command=back)
btn4.place(x=screen_width-150,y=0)
def enter(i):
    btn4['background']="red"
def leave(i):
    btn4['background']="grey"
btn4.bind('<Enter>',enter)
btn4.bind('<Leave>',leave)

frame=Frame(project,width=450,height=550,bg="white",highlightthickness=2,highlightbackground="blue")
frame.place(x=screen_width-1000,y=screen_height/6)

heading=Label(frame,text='Sign Up',fg="black",bg="white",font=("Arial",30))
heading.place(x=160,y=1)

def on_enter(w):
    name=first_name.get()
    if name=="First  Name":
        first_name.delete(0,"end")

def on_leave(w):
    name=first_name.get()
    if name=="":
        first_name.insert(0,"First  Name")
first_name=Entry(frame,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
first_name.place(x=42,y=85)
first_name.insert(0,"First  Name")
first_name.bind('<FocusIn>',on_enter)
first_name.bind('<FocusOut>',on_leave)
Frame(frame,width=170,height=2,bg="black").place(x=40,y=112)

def on1_enter(w):
    name=last_name.get()
    if name=="Last  Name":
        last_name.delete(0,"end")

def on1_leave(w):
    name=last_name.get()
    if name=="":
        last_name.insert(0,"Last  Name")
last_name=Entry(frame,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
last_name.place(x=42,y=150)
last_name.insert(0,"Last  Name")
last_name.bind('<FocusIn>',on1_enter)
last_name.bind('<FocusOut>',on1_leave)
Frame(frame,width=170,height=2,bg="black").place(x=42,y=180)
def on3_enter(w):
    name=phone_number.get()
    if name=="Phone Number":
        phone_number.delete(0,"end")
def on3_leave(w):
    name=phone_number.get()
    if name=="":phone_number.insert(0,"Phone Number")
phone_number=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
phone_number.place(x=40,y=215)
phone_number.insert(0,"Phone Number")
phone_number.bind('<FocusIn>',on3_enter)
phone_number.bind('<FocusOut>',on3_leave)
Frame(frame,width=360,height=2,bg="black").place(x=40,y=242)
def on4_enter(w):
    name=email.get()
    if name=="Enter Your Email":
        email.delete(0,"end")
def on4_leave(w):
    name=email.get()
    if name=="":
        email.insert(0,"Enter Your Email")
email=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
email.place(x=42,y=280)
email.insert(0,"Enter Your Email")
email.bind('<FocusIn>',on4_enter)
email.bind('<FocusOut>',on4_leave)

Frame(frame,width=360,height=2,bg="black").place(x=40,y=307)


def on6_enter(w):
    name=code1.get()
    if name=="Create Password":
        code1.delete(0,"end")
    
def on6_leave(w):
    name=code1.get()
    if name=="":
        code1.insert(0,"Create Password")
     
code1=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
code1.place(x=42,y=345)
code1.insert(0,"Create Password")
code1.bind('<FocusIn>',on6_enter)
code1.bind('<FocusOut>',on6_leave)

Frame(frame,width=360,height=2,bg="black").place(x=40,y=372)

def hide1():
    eyeclose1.config(file="eyeopen8.png")
    code1.config(show="")
    eyebutton1.config(command=show1)

def show1():
    eyeclose1.config(file="eyeclose2.png")
    code1.config(show="●")
    eyebutton1.config(command=hide1)

eyeclose1=PhotoImage(file="eyeopen8.png")
eyebutton1=Button(frame,image=eyeclose1,bg="white",border=0,command=show1,activebackground="white",cursor="hand2")
eyebutton1.place(x=355,y=330)

def on_enter(w):
    name=code.get()
    if name=="Confirm Password":
        code.delete(0,"end")
    
def on_leave(w):
    name=code.get()
    if name=="":
        code.insert(0,"Confirm Password")
     
code=Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
code.place(x=42,y=410)
code.insert(0,"Confirm Password")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=360,height=2,bg="black").place(x=40,y=437)

def hide():
    eyeclose.config(file="eyeopen7.png")
    code.config(show="")
    eyebutton.config(command=show)

def show():
    eyeclose.config(file="eyeclose1.png")
    code.config(show="●")
    eyebutton.config(command=hide)

eyeclose=PhotoImage(file="eyeopen7.png")
eyebutton=Button(frame,image=eyeclose,bg="white",border=0,command=show,activebackground="white",cursor="hand2")
eyebutton.place(x=355,y=395)

buttonFont1 = font.Font(size=15)

def o_enter(a):
    c['background']='#7ab3f5'

def o_leave(a):
    c['background']='#57a1f8'

def login_page():
    project.destroy()
    runpy.run_path(
        "login.py")

c=Button(frame,width=15,pady=3,text="Back(Login)",bg="#57a1f8",fg="white",border=0,font=buttonFont1,activebackground="#57a1f8",activeforeground="white",command=login_page)
c.place(x=40,y=475)
c.bind('<Enter>',o_enter)
c.bind('<Leave>',o_leave)

def o1_enter(a):
    d['background']='#7ab3f5'

def o1_leave(a):
    d['background']='#57a1f8'


def signin():
    Firstname=first_name.get()
    Lastname=last_name.get()
    emails=email.get()
    phonenumber=phone_number.get()
    password=code1.get()
    confirmpassword=code.get()
    check=range(1,20)
    global img
    if  Firstname=="First  Name" or Lastname=="Last  Name" or phone_number=="Phone Number" or emails=="Enter Your Email" or password=="Create Password" or confirmpassword=="Confirm Password"   :
        messagebox.showinfo("Error","Please fill all the form")
    elif phonenumber.isdigit()==False:
        messagebox.showerror("Error","Enter a Number(Phone Number)")
    elif len(phonenumber)!=10:
        messagebox.showerror("Error","Enter a Valid Phone Number")
    elif "@" not in emails or emails.endswith(".com")==False:
        messagebox.showerror("Error","Enter a Valid Email")
    elif password!=confirmpassword:
        messagebox.showerror("Error","Password do not match")
    else:
        messagebox.showinfo("Message","Your ID has been created.")
        ruj=sqlite3.connect("signup.db")
        r=ruj.cursor()
        r.execute("""CREATE TABLE IF NOT EXISTS sign (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            confirm_password TEXT NOT NULL)""")
        try:
            r.execute("""
                    INSERT INTO sign (first_name, last_name, phone_number, email, password, confirm_password)
                    VALUES(?,?,?,?,?,?)
                    """, (Firstname, Lastname, phonenumber, emails, password, confirmpassword))
            ruj.commit()
            ruj.close()
        except Exception as e:
            messagebox.showerror("Error",e)
            
        project.destroy()
        runpy.run_path("login.py")
d=Button(frame,width=15,pady=3,text="Next  ➔",bg="#57a1f8",fg="white",border=0,font=buttonFont1,activebackground="#57a1f8",activeforeground="white",command=signin)
d.place(x=235,y=475)
d.bind('<Enter>',o1_enter)
d.bind('<Leave>',o1_leave)

project.mainloop()


