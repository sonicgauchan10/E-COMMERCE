from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as font
import runpy
import sqlite3

# Function to create a database connection
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("signup.db")  # Connect to the SQLite database
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create the sign-up table
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sign (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                teacher_id TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                confirm_password TEXT NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Function to insert data into the database
def insert_data(conn, data):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO sign (first_name, last_name, teacher_id, phone_number, email, password, confirm_password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error", e)
        return False

# Creating project after the teacher logs in
project = Tk()
project.configure(bg="white")
project.attributes("-fullscreen", True)

# Creating title bar
a = Frame(project, width=1550, height=35, bg="#57a1f8").place(x=0, y=0)
title = Label(a, text="BSLR Mart", font=("Comic Sans MS", 15, "bold"), bg="#57a1f8").place(x=36, y=0)
img = Image.open(r"logo.png")  # image logo
img = img.resize((30, 30))
new_logo = ImageTk.PhotoImage(img)
image = Label(image=new_logo, border=0, bg="#57a1f8").place(x=5, y=3)
screen_width = project.winfo_screenwidth()
screen_height = project.winfo_screenheight()

# Making maximize and minimize button manually
def min():
    project.iconify()

def on_enter(i):
    btn2['background'] = "red"

def on_leave(i):
    btn2['background'] = "#57a1f8"

def max():
    msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?', icon='warning')
    if msg_box == 'yes':
        project.destroy()

label1 = LabelFrame(project, height=35, fg="blue", bg="#57a1f8").place(x=0, y=0)
buttonFont = font.Font(size=14)
btn2 = Button(a, text="✕", command=max, width=4, bg="#57a1f8", border=0, font=buttonFont)
btn2.pack(anchor="ne")
btn2.bind('<Enter>', on_enter)
btn2.bind('<Leave>', on_leave)

btn = Button(a, text="-", command=min, width=4, bg="#57a1f8", border=0, font=buttonFont)
btn.place(x=screen_width - 100, y=0)

def enter(i):
    btn['background'] = "red"

def leave(i):
    btn['background'] = "#57a1f8"

btn.bind('<Enter>', enter)
btn.bind('<Leave>', leave)

img = ImageTk.PhotoImage(Image.open(r"logo.png"))
image = Label(image=img, bg="white").place(x=50, y=(screen_height / 4) + 25)

frame = Frame(project, width=450, height=550, bg="white", highlightthickness=2, highlightbackground="black")
frame.place(x=screen_width - 550, y=screen_height / 7)

heading = Label(frame, text='Sign Up', fg="#57a1f8", bg="white", font=("Arial", 30))
heading.place(x=160, y=1)

def on_enter(w):
    name = first_name.get()
    if name == "First  Name":
        first_name.delete(0, "end")

def on_leave(w):
    name = first_name.get()
    if name == "":
        first_name.insert(0, "First  Name")

first_name = Entry(frame, width=10, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 16))
first_name.place(x=42, y=85)
first_name.insert(0, "First  Name")
first_name.bind('<FocusIn>', on_enter)
first_name.bind('<FocusOut>', on_leave)
Frame(frame, width=170, height=2, bg="black").place(x=40, y=112)

def on1_enter(w):
    name = last_name.get()
    if name == "Last  Name":
        last_name.delete(0, "end")

def on1_leave(w):
    name = last_name.get()
    if name == "":
        last_name.insert(0, "Last  Name")

last_name = Entry(frame, width=10, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 16))
last_name.place(x=232, y=85)
last_name.insert(0, "Last  Name")
last_name.bind('<FocusIn>', on1_enter)
last_name.bind('<FocusOut>', on1_leave)
Frame(frame, width=170, height=2, bg="black").place(x=230, y=112)

def on2_enter(w):
    name = teacher_id.get()
    if name == "Teacher ID":
        teacher_id.delete(0, "end")

def on2_leave(w):
    name = teacher_id.get()
    if name == "":
        teacher_id.insert(0, "Teacher ID")

teacher_id = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 16))
teacher_id.place(x=42, y=150)
teacher_id.insert(0, "Teacher ID")
teacher_id.bind('<FocusIn>', on2_enter)
teacher_id.bind('<FocusOut>', on2_leave)
Frame(frame, width=360, height=2, bg="black").place(x=40, y=177)

def on3_enter(w):
    name = phone_number.get()
    if name == "Phone Number":
        phone_number.delete(0, "end")

def on3_leave(w):
    name = phone_number.get()
    if name == "":
        phone_number.insert(0, "Phone Number")

phone_number = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 16))
phone_number.place(x=40, y=215)
phone_number.insert(0, "Phone Number")
phone_number.bind('<FocusIn>', on3_enter)
phone_number.bind('<FocusOut>', on3_leave)
Frame(frame, width=360, height=2, bg="black").place(x=40, y=242)

def on4_enter(w):
    name = email.get()
    if name == "Enter Your Email":
        email.delete(0, "end")

def on4_leave(w):
    name = email.get()
    if name == "":
        email.insert(0, "Enter Your Email")

email = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 16))
email.place(x=42, y=280)
email.insert(0, "Enter Your Email")
email.bind('<FocusIn>', on4_enter)
email.bind('<FocusOut>', on4_leave)
Frame(frame, width=360, height=2, bg="black").place(x=40, y=307)

def on6_enter(w):
    name = code1.get()
    if name == "Create Password":
        code1.delete(0, "end")

def on6_leave(w):
    name = code1.get()
    if name == "":
        code1.insert(0, "Create Password")

code1 = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 16))
code1.place(x=42, y=345)
code1.insert(0, "Create Password")
code1.bind('<FocusIn>', on6_enter)
code1.bind('<FocusOut>', on6_leave)
Frame(frame, width=360, height=2, bg="black").place(x=40, y=372)

def hide1():
    eyeclose1.config(file="eyeopen8.png")
    code1.config(show="")
    eyebutton1.config(command=show1)

def show1():
    eyeclose1.config(file="eyeclose2.png")
    code1.config(show="●")
    eyebutton1.config(command=hide1)

eyeclose1 = PhotoImage(file="eyeopen8.png")
eyebutton1 = Button(frame, image=eyeclose1, bg="white", border=0, command=show1, activebackground="white", cursor="hand2")
eyebutton1.place(x=355, y=330)

def on_enter(w):
    name = code.get()
    if name == "Confirm Password":
        code.delete(0, "end")

def on_leave(w):
    name = code.get()
    if name == "":
        code.insert(0, "Confirm Password")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 16))
code.place(x=42, y=410)
code.insert(0, "Confirm Password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=360, height=2, bg="black").place(x=40, y=437)

def hide():
    eyeclose.config(file="eyeopen7.png")
    code.config(show="")
    eyebutton.config(command=show)

def show():
    eyeclose.config(file="eyeclose1.png")
    code.config(show="●")
    eyebutton.config(command=hide)

eyeclose = PhotoImage(file="eyeopen7.png")
eyebutton = Button(frame, image=eyeclose, bg="white", border=0, command=show, activebackground="white", cursor="hand2")
eyebutton.place(x=355, y=395)

buttonFont1 = font.Font(size=15)

def o_enter(a):
    c['background'] = '#7ab3f5'

def o_leave(a):
    c['background'] = '#57a1f8'

def login_page():
    project.destroy()
    runpy.run_path("final_login.py")

c = Button(frame, width=15, pady=3, text="Back(Login)", bg="#57a1f8", fg="white", border=0, font=buttonFont1, activebackground="#57a1f8", activeforeground="white", command=login_page)
c.place(x=40, y=475)
c.bind('<Enter>', o_enter)
c.bind('<Leave>', o_leave)

def o1_enter(a):
    d['background'] = '#7ab3f5'

def o1_leave(a):
    d['background'] = '#57a1f8'

def signin():
    Firstname = first_name.get()
    Lastname = last_name.get()
    teacherid = teacher_id.get()
    emails = email.get()
    phonenumber = phone_number.get()
    password = code1.get()
    confirmpassword = code.get()
    check = range(1, 20)

    if Firstname == "First  Name" or Lastname == "Last  Name" or teacherid == "Teacher Id" or phonenumber == "Phone Number" or emails == "Enter Your Email" or password == "Create Password" or confirmpassword == "Confirm Password":
        messagebox.showinfo("Error", "Please fill all the form")
    elif teacherid.isdigit() == False:
        messagebox.showerror("Error", "Enter a Number(Teacher ID)")
    elif int(teacherid) not in check:
        messagebox.showerror("Error", "Enter a Valid Teacher ID")
    elif phonenumber.isdigit() == False:
        messagebox.showerror("Error", "Enter a Number(Phone Number)")
    elif len(phonenumber) != 10:
        messagebox.showerror("Error", "Enter a Valid Phone Number")
    elif "@" not in emails or emails.endswith(".com") == False:
        messagebox.showerror("Error", "Enter a Valid Email")
    elif password != confirmpassword:
        messagebox.showerror("Error", "Password do not match")
    else:
        # Connect to the database
        conn = create_connection()
        if conn is not None:
            create_table(conn)  # Ensure the table exists
            data = (Firstname, Lastname, teacherid, phonenumber, emails, password, confirmpassword)
            if insert_data(conn, data):  # Insert data into the database
                messagebox.showinfo("Message", "Your ID has been created.")
                project.destroy()
                runpy.run_path("final_login.py")
            conn.close()
        else:
            messagebox.showerror("Error", "Failed to connect to the database.")

d = Button(frame, width=15, pady=3, text="Next  ➔", bg="#57a1f8", fg="white", border=0, font=buttonFont1, activebackground="#57a1f8", activeforeground="white", command=signin)
d.place(x=235, y=475)
d.bind('<Enter>', o1_enter)
d.bind('<Leave>', o1_leave)

project.mainloop()