from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter.font as font
import sqlite3
from tkcalendar import DateEntry
import runpy
import sqlite3

ruj = sqlite3.connect("signup.db")
r = ruj.cursor()

# Create details table if it doesn't exist
r.execute("""
    CREATE TABLE IF NOT EXISTS details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
""")

ruj.commit()
ruj.close()

#creating root after the teacher logs in
account=Tk()
account.configure(bg="white")
account.attributes("-fullscreen",True)
screen_width = account.winfo_screenwidth()
screen_height= account.winfo_screenheight()
buttonFont1 = font.Font(size=13)
#creating title bar
a=Frame(account,width=screen_width,height=35,bg="#57a1f8").place(x=0,y=0)
title=Label(a, text="AccuResult",font=("Comic Sans MS",15,"bold"), bg="#57a1f8").place(x=36,y=0)
img=Image.open(r"logo.png") #image logo
img=img.resize((30,30))
new_logo=ImageTk.PhotoImage(img)
image=Label(image=new_logo,border=0,bg="#57a1f8").place(x=5,y=3)


#making maximize and minimize button manually
def min():
    account.iconify()
def on_enter(i):
    btn2['background']="red"
def on_leave(i):
    btn2['background']="#57a1f8"
def max():
    msg_box =messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?',icon='warning')
    if msg_box == 'yes':
        account.destroy()
label1=LabelFrame(account,height=35,fg="blue",bg="#57a1f8").place(x=0,y=0)
buttonFont = font.Font(size=14)

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


#CREATING A OPTION BAR AT LEFT OF SCREEN
options_frame=Frame(height=screen_height-35,width=250,bg='#fcf0d7').place(x=0,y=35)

#creating workspace
display_frame=Frame(width=screen_width-250,bg="#ffffff").pack(fill=BOTH,expand=TRUE,padx=(250,0),pady=(0,0))

#creating template
img2=Image.open(r"eye1.png") #image logo
new_logo2=ImageTk.PhotoImage(img2)
image2=Label(display_frame,image=new_logo2,border=0).place(x=250,y=35)





#THE EXTERIOR FRAME OF THE TABLE
def on_details():
    title_details=Label(display_frame,text="DETAILS",font=buttonFont,bg="#7ab3f5",width=94)
    title_details.place(x=250,y=215)

    ruj=sqlite3.connect("signup.db")
    r=ruj.cursor()

    def save():
        Firstname=first_name.get()
        Lastname=last_name.get()
        emails=email.get()
        phonenumber=phone_number.get()
        password=code1.get()
        confirmpassword=code.get()
        global img
        
        if  Firstname=="" or Lastname=="" or phone_number=="" or emails=="" or password=="" or confirmpassword==""   :
            messagebox.showerror("Error","Please fill all the form")
        elif password!=confirmpassword:
            messagebox.showerror("Error","Password do not match")
        elif phonenumber.isdigit()==False:
            messagebox.showerror("Error","Enter a Number(Phone Number)")
        else:
            messagebox.showinfo("Message","Your detail has been updated.")
            try:
                r.execute("""
                        UPDATE sign SET first_name=?, last_name=?, email=?, phone_number=?, password=?, confirm_password=? WHERE email=?       
                        """, (Firstname, Lastname, emails, phonenumber, password, confirmpassword, emails))
                
                r.execute("SELECT * FROM sign")
                data=r.fetchall()
                counter = 0
                flag=""

                for item in data:       
                    for value in item:
                        if counter==1:
                            first_name.delete(0,"end")     
                            first_name.insert(0,value)
                        if counter==2:
                            last_name.delete(0,"end")
                            last_name.insert(0,value)

                        if counter==4:
                            phone_number.delete(0,"end")
                            phone_number.insert(0,value)

                        if counter==5:
                            email.delete(0,"end")
                            email.insert(0,value)

                        if counter==6:
                            code1.delete(0,"end")
                            code1.insert(0,value)

                        if counter==7:
                            code.delete(0,"end")
                            code.insert(0,value)
                        counter+=1
                ruj.commit()
            except Exception as c:
                messagebox.showerror("Error",c)
 



    global tableframe
    tableframe = Frame(account,width=700,height=(screen_height/2)+55,bg="white",highlightthickness=2,highlightbackground="black")
    tableframe.place(x=430,y=265)
    
   
    c=Label(tableframe,text="First Name",fg="black",bg="white",font=("Arial",15)).place(x=42,y=25)
    c=Label(tableframe,text="Last Name",fg="black",bg="white",font=("Arial",15)).place(x=360,y=25)
    c=Label(tableframe,text="Phone No.",fg="black",bg="white",font=("Arial",15)).place(x=42,y=105)
    c=Label(tableframe,text="Email",fg="black",bg="white",font=("Arial",15)).place(x=42,y=180)
    c=Label(tableframe,text="Choose Password",fg="black",bg="white",font=("Arial",15)).place(x=42,y=255)
    c=Label(tableframe,text="Confirm Password",fg="black",bg="white",font=("Arial",15)).place(x=360,y=255)

     #creating first name

    first_name=Entry(tableframe,width=25,fg="black",bg="white",font=("Microsoft Yahei UI Light",16))
    first_name.place(x=42,y=60)

    #creating last name
    last_name=Entry(tableframe,width=25,fg="black",bg="white",font=("Microsoft Yahei UI Light",16))
    last_name.place(x=360,y=60)


    #for phone number
    phone_number=Entry(tableframe,width=25,fg="black",bg="white",font=("Microsoft Yahei UI Light",16))
    phone_number.place(x=42,y=140)


    
    email=Entry(tableframe,width=25,fg="black",bg="white",font=("Microsoft Yahei UI Light",16))
    email.place(x=40,y=215)


    #for create password

    code1=Entry(tableframe,width=25,fg="black",bg="white",font=("Microsoft Yahei UI Light",16),show="●")
    code1.place(x=42,y=290)

    def hide1():
        eyeclose1.config(file="eye1.png")
        code1.config(show="●")
        eyebutton1.config(command=show1)

    def show1():
        eyeclose1.config(file="eye3.png")
        code1.config(show="")
        eyebutton1.config(command=hide1)

    eyeclose1=PhotoImage(file="eye1.png")
    eyebutton1=Button(tableframe,image=eyeclose1,bg="white",border=0,command=show1,activebackground="white",cursor="hand2")
    eyebutton1.place(x=315,y=293)

    #for confirm password
        
    code=Entry(tableframe,width=25,fg="black",bg="white",font=("Microsoft Yahei UI Light",16),show="●")
    code.place(x=360,y=290)
    # code.insert(0,"Confirm Password")

   # r.execute("SELECT * FROM sign")
    data=r.fetchall()
    counter = 0
        

    for item in data:       
            for value in item:
                if counter==1:
                    first_name.delete(0,"end")     
                    first_name.insert(0,value)
                if counter==2:
                    last_name.delete(0,"end")
                    last_name.insert(0,value)

                if counter==4:
                    phone_number.delete(0,"end")
                    phone_number.insert(0,value)

                if counter==5:
                    email.delete(0,"end")
                    email.insert(0,value)


                if counter==6:
                    code1.delete(0,"end")
                    code1.insert(0,value)

                if counter==7:
                    code.delete(0,"end")
                    code.insert(0,value)
                counter+=1
    


    def hide():
        eyeclose.config(file="eye2.png")
        code.config(show="●")
        eyebutton.config(command=show)

    def show():
        eyeclose.config(file="eye4.png")
        code.config(show="")
        eyebutton.config(command=hide)

    eyeclose=PhotoImage(file="eye2.png")
    eyebutton=Button(tableframe,image=eyeclose,bg="white",border=0,command=show,activebackground="white",cursor="hand2")
    eyebutton.place(x=630,y=293)
    

    def o1_enter(a):
        d['background']='#7ab3f5'

    def o1_leave(a):
        d['background']='#57a1f8'
    buttonFont1 = font.Font(size=15)
    d=Button(tableframe,width=15,pady=3,text="Save Update",bg="#57a1f8",fg="white",border=0,font=buttonFont1,activebackground="#57a1f8",activeforeground="white",command=save)
    d.place(x=252,y=360)
    d.bind('<Enter>',o1_enter)
    d.bind('<Leave>',o1_leave)



def create():
    account.destroy()
    runpy.run_path(
            "final_create.py")
    
def edit():
    account.destroy()
    runpy.run_path(
            "final_edit.py")


def details():
    on_details()

def logout():
    msg_box =messagebox.askquestion('Confirm Logout', 'Are you sure you want to logout?',icon='warning')
    if msg_box == 'yes':
        account.destroy()
        runpy.run_path(
            "final_base.py")


btn_create=Button(options_frame, text="CREATE", font= buttonFont,padx=78,pady=9,bg="#fcf0d7",relief=GROOVE,command=create)
btn_create.place(x=0,y=35)
btn_edit=Button(options_frame, text="EDIT", font= buttonFont,padx=95,pady=9,bg="#fcf0d7",relief=GROOVE,command=edit)
btn_edit.place(x=0,y=88)
btn_detail=Button(options_frame, text="DETAIL", font= buttonFont,padx=83,pady=9,bg="white",relief=GROOVE,command=details)
btn_detail.place(x=0,y=141)
btn_logout=Button(options_frame, text="LOGOUT", font= buttonFont,padx=77,pady=9,bg="#fcf0d7",relief=GROOVE,command=logout)
btn_logout.place(x=0,y=194)

#view
def view():
    runpy.run_path(
        "top1.py")
    
#to view the result
btn_result=Button(display_frame,width=10,padx=55,text="View Result",bg="#57a1f8",fg="white",border=2,font=("Microsoft Yahei UI Light",16,"bold"),activebackground="#57a1f8",activeforeground="white",command=view)
btn_result.place(x=0,y=screen_height-49)
on_details()
account.mainloop()