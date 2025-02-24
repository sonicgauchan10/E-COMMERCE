from tkinter import*
from tkinter import messagebox
import tkinter.font as font
from PIL import ImageTk,Image
import runpy
import sqlite3

project=Tk()
project.configure(bg="white")
project.attributes("-fullscreen",True)

screen_width = project.winfo_screenwidth()
screen_height= project.winfo_screenheight()

#creating title bar
a=Frame(project,width=screen_width,height=35,bg="#57a1f8").place(x=0,y=0)
title=Label(a, text="BSLR Mart",font=("Comic Sans MS",15,"bold"), bg="#57a1f8").place(x=36,y=0)
img=Image.open(r"logo.png") #image logo
img=img.resize((30,30))
new_logo=ImageTk.PhotoImage(img)
image=Label(image=new_logo,border=0,bg="#57a1f8").place(x=5,y=3)
label1=LabelFrame(project,height=35,fg="blue",bg="#57a1f8").place(x=0,y=0)
buttonFont = font.Font(size=14)
buttonFont1 = font.Font(size=13)

#making maximize and minimize button manually
def min():
    project.iconify()
def on_enter(i):
    btn2['background']="red"
def on_leave(i):
    btn2['background']="#57a1f8"
def max():
    msg_box =messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?',icon='warning')
    if msg_box == 'yes':
        project.destroy()

btn2=Button(a,text="✕", command=max,width=4,bg="#57a1f8",border=0,font=buttonFont)
btn2.pack(anchor="ne")
btn2.bind('<Enter>',on_enter)
btn2.bind('<Leave>',on_leave)
btn=Button(a,text="-", command=min,width=4,bg="#57a1f8",border=0,font=buttonFont)
btn.place(x=screen_width-100,y=0)
def enter(i):
    btn['background']="red"
def leave(i):
    btn['background']="#57a1f8"
btn.bind('<Enter>',enter)
btn.bind('<Leave>',leave)

#back_button
def back():
    project.destroy()
    runpy.run_path(
        "final_base.py")
btn4=Button(project,text="<<",width=4,bg="#57a1f8",border=0,font=buttonFont,command=back)
btn4.place(x=screen_width-150,y=0)
def enter(i):
    btn4['background']="red"
def leave(i):
    btn4['background']="#57a1f8"
btn4.bind('<Enter>',enter)
btn4.bind('<Leave>',leave)


#Inserting picture
img=ImageTk.PhotoImage(Image.open(r"logo.png"))
image=Label(image=img,bg="white").place(x=50,y=(screen_height/4)+25)

#creating frame for login
frame2=Frame(project,width=450,height=445,bg="white", highlightthickness=2,highlightbackground="black")
frame2.place(x=screen_width-550,y=screen_height/5)
heading=Label(frame2,text='Sign In',fg="#57a1f8",bg="white",font=("Arial",30))
heading.place(x=160,y=25)
def on_enter(w):
    name=user.get()
    if name=="Email":
        user.delete(0,"end")
def on_leave(w):
    name=user.get()
    if name=="":
        user.insert(0,"Email")
user=Entry(frame2,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
user.place(x=50,y=125)
user.insert(0,"Email")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame2,width=340,height=2,bg="black").place(x=50,y=152)

def on_enter(w):
    name=code.get()
    if name=="Password":
        code.delete(0,"end")
        code.config(show="●")
def on_leave(w):
    name=code.get()
    if name=="":
        code.config(show="")
        code.insert(0,"Password")  
code=Entry(frame2,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
code.place(x=50,y=225)
code.insert(0,"Password")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame2,width=340,height=2,bg="black").place(x=50,y=252)

def signin():
    username=user.get()
    password=code.get()
    ayu=sqlite3.connect("signup.db")
    a=ayu.cursor()
    if username == "admin" and password == "admin":
        runpy.run_path("5.py");
    else:
        a.execute("SELECT * FROM sign WHERE email=? AND password=?", (username, password))
        sleep= a.fetchone()
        if sleep:
            ayu.commit()
            ayu.close()
            project.destroy()
            runpy.run_path("4.py")
                
        else:
            messagebox.showerror("Error","Invalid information")

c=Button(frame2,width=38,pady=7,text="Login",bg="#57a1f8",fg="white",border=0,command=signin,font=buttonFont1,activebackground="#57a1f8",activeforeground="white")
c.place(x=45,y=300)
def o_enter(a):
    c['background']='#7ab3f5'
def o_leave(a):
    c['background']='#57a1f8'
c.bind('<Enter>',o_enter)
c.bind('<Leave>',o_leave)
label=Label(frame2,text="Don't have an account?",fg="black",bg="white",font=("Microsoft Yahei UI Light",14))
label.place(x=85,y=385)

def sign_up():
    project.destroy()
    runpy.run_path("signup.py")
    
sign_up=Button(frame2,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=sign_up,font=buttonFont,activebackground="white",activeforeground="#57a1f8")
sign_up.place(x=294,y=385)

def os_enter(a):
    sign_up['foreground']='#7ab3f5'
def os_leave(a):
    sign_up['foreground']='#57a1f8'
sign_up.bind('<Enter>',os_enter)
sign_up.bind('<Leave>',os_leave)

def hide():
    eyeclose.config(file="eyeclose1.png")
    code.config(show="●")
    eyebutton.config(command=show)
def show():
    eyeclose.config(file="eyeopen7.png")
    code.config(show="")
    eyebutton.config(command=hide)

eyeclose=PhotoImage(file="eyeclose1.png")
eyebutton=Button(frame2,image=eyeclose,bg="white",border=0,command=show,activebackground="white",cursor="hand2")
eyebutton.place(x=355,y=215)

project.mainloop()