from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import tkinter.font as font
import sqlite3
import runpy

# Creating root after the teacher logs in
account = Tk()
account.configure(bg="white")
account.attributes("-fullscreen", True)

screen_width = account.winfo_screenwidth()
screen_height = account.winfo_screenheight()

buttonFont1 = font.Font(size=13)
buttonFont2 = font.Font(size=26, weight="bold", family="Microsoft Yahei UI Light")

# Creating title bar
a = Frame(account, width=screen_width, height=35, bg="#57a1f8").place(x=0, y=0)

# Calculate the x position to center the title
title_text = "BSLR MART"
title_font = ("Comic Sans MS", 15, "bold")
title_width = font.Font(family="Comic Sans MS", size=15, weight="bold").measure(title_text)
title_x = (screen_width - title_width) // 2

title = Label(a, text=title_text, font=title_font, bg="#57a1f8")
title.place(x=title_x, y=0)

img = Image.open(r"logo.png")  # image logo
img = img.resize((30, 30))
new_logo = ImageTk.PhotoImage(img)
image = Label(image=new_logo, border=0, bg="#57a1f8").place(x=5, y=3)

# Making maximize and minimize button manually
def min():
    account.iconify()

def on_enter(i):
    btn2['background'] = "red"

def on_leave(i):
    btn2['background'] = "#57a1f8"

def max():
    msg_box = messagebox.askquestion('Exit Application', 'Are you sure you want to close the application?', icon='warning')
    if msg_box == 'yes':
        account.destroy()

label1 = LabelFrame(account, height=35, fg="blue", bg="#57a1f8").place(x=0, y=0)
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

# CREATING A OPTION BAR AT LEFT OF SCREEN
options_frame = Frame(height=screen_height - 35, width=250, bg='#fcf0d7').place(x=0, y=35)

def on_edit():
    global tableframe

    tableframe = Frame(account, width=screen_width / 1.55, height=(screen_height / 2) + 10, bg="white", highlightthickness=2, highlightbackground="black")
    tableframe.place(x=280, y=320)

    # Creating a var for position of the line in the table
    pos = ((screen_height / 2) + 10) / 8

    # TO SEARCH

    row1 = Frame(tableframe, width=screen_width / 1.55, height=3, bg="black", highlightthickness=2, highlightbackground="black")
    row1.place(y=pos)
    pos = pos + pos

    row2 = Frame(tableframe, width=screen_width / 1.55, height=3, bg="black", highlightthickness=2, highlightbackground="black")
    row2.place(y=pos)
    pos = pos + (pos * 0.5)

    row3 = Frame(tableframe, width=screen_width / 1.55, height=2, bg="black", highlightthickness=2, highlightbackground="black")
    row3.place(y=pos)
    pos = pos + pos * 0.34

    row4 = Frame(tableframe, width=screen_width / 1.55, height=2, bg="black", highlightthickness=2, highlightbackground="black")
    row4.place(y=pos)
    pos = pos + pos * 0.25

    row5 = Frame(tableframe, width=screen_width / 1.55, height=2, bg="black", highlightthickness=2, highlightbackground="black")
    row5.place(y=pos)
    pos = pos + pos * 0.18

    row6 = Frame(tableframe, width=screen_width / 1.55, height=2, bg="black", highlightthickness=2, highlightbackground="black")
    row6.place(y=pos)
    pos = pos + pos * 0.16

    row6 = Frame(tableframe, width=screen_width / 1.55, height=2, bg="black", highlightthickness=2, highlightbackground="black")
    row6.place(y=pos)

    # NOW FOR THE COLUMNS
    pos = (screen_width / 1.55) / 8

    col1 = Frame(tableframe, width=2, height=1500, bg="black", highlightthickness=2, highlightbackground="black")
    col1.place(x=pos, y=((screen_height / 2) + 10) / 8)
    pos = pos * 3.5

    col2 = Frame(tableframe, width=2, height=1500, bg="black", highlightthickness=2, highlightbackground="black")
    col2.place(x=pos - 25, y=((screen_height / 2) + 10) / 8)
    pos = pos + pos * 0.5

    col3 = Frame(tableframe, width=2, height=1500, bg="black", highlightthickness=2, highlightbackground="black")
    col3.place(x=pos - 55, y=((screen_height / 2) + 10) / 8)
    pos = pos + pos * 0.18

    col4 = Frame(tableframe, width=2, height=1500, bg="black", highlightthickness=2, highlightbackground="black")
    col4.place(x=pos * 1.09 - 53, y=((screen_height / 2) + 10) / 8)
    pos = pos + pos * 0.18

    name = Label(tableframe, text="Name:", bg="white", font=("Microsoft Yahei UI Light", 14))
    name.place(x=10, y=screen_height / 50 - 5)

    name_label = Entry(tableframe, fg="black", border=1, bg="white", font=("Microsoft Yahei UI Light", 14), width=25)
    name_label.place(x=75, y=screen_height / 50 - 4)

    DOB = Label(tableframe, text="Date Of Birth:", bg="white", font=("Microsoft Yahei UI Light", 16))
    DOB.place(x=490, y=screen_height / 50 - 5)
    DOB_label = DateEntry(tableframe, fg="black", border=1, bg="white", font=("Microsoft Yahei UI Light", 14), width=13)
    DOB_label.place(x=625, y=screen_height / 50 - 4)
    DOB_label.delete(0, END)

account.mainloop()