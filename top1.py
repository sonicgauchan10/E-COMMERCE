from tkinter import*
from tkinter import messagebox
import tkinter.font as font
import sqlite3
from tkcalendar import DateEntry
import runpy

project=Tk()
project.configure(bg="white")
project.title("Check")
project.maxsize(width=359,height=300)
project.minsize(width=359,height=300)

buttonFont1 = font.Font(size=13)
buttonFont2=font.Font(size=26,weight="bold",family="Microsoft Yahei UI Light")

frame2=Frame(project,width=450,height=445,bg="white")
frame2.place(x=0,y=0)
heading2=Label(frame2,text='Check Result',fg="#57a1f8",bg="white",font=("Arial",25))
heading2.place(x=80,y=10)
def on_enter(w):
    name=user.get()
    if name=="StudentName":
        user.delete(0,"end")
def on_leave(w):
    name=user.get()
    if name=="":
        user.insert(0,"StudentName")
DOB = Label(frame2,text="DOB:",bg="white",font=("Microsoft Yahei UI Light",16))
DOB.place(x=30,y=88)
user = DateEntry(frame2,year=2003,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",14),width=13)
user.place(x=85,y=88)
user.delete(0,END)
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame2,width=300,height=2,bg="black").place(x=30,y=120)
def on_enter(w):
    name=code.get()
    if name=="StudentID":
        code.delete(0,"end")
def on_leave(w):
    name=code.get()
    if name=="":
        code.insert(0,"StudentID")  
code=Entry(frame2,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
code.place(x=30,y=175)
code.insert(0,"StudentID")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame2,width=300,height=2,bg="black").place(x=30,y=202)
def o_enter(a):
    c['background']='#7ab3f5'
def o_leave(a):
    c['background']='#57a1f8'





def result():

    check_dob = user.get()
    check_student_id = code.get()


    conn = sqlite3.connect("addressbook.db")
    cd = conn.cursor()
    cd.execute("SELECT * FROM details WHERE std_id =? AND dob =?", (check_student_id, check_dob))
    sleep = cd.fetchall()

    if sleep:
        
        project.destroy()
        top1=Tk()
        top1.title("Check")
        top1.maxsize(width=850,height=390)
        top1.minsize(width=850,height=390)
        screen_width=830
        screen_height=370
        
        tableframe1 = Frame(top1,width=826,height=370,bg="white",highlightthickness=2,highlightbackground="black")
        tableframe1.place(x=10,y=10)
        row1 = Frame(tableframe1,width=830,height=2,bg="black",highlightthickness=2,highlightbackground="black")
        row1.place(y=40)

        row2 = Frame(tableframe1,width=830,height=2,bg="black",highlightthickness=2,highlightbackground="black")
        row2.place(y=40)

        row3 = Frame(tableframe1,width=830,height=2,bg="black",highlightthickness=2,highlightbackground="black")
        row3.place(y=80)

        row4 = Frame(tableframe1,width=830,height=2,bg="black",highlightthickness=2,highlightbackground="black")
        row4.place(y=120)

        row5 = Frame(tableframe1,width=830,height=2,bg="black",highlightthickness=2,highlightbackground="black")
        row5.place(y=160)

        row6 = Frame(tableframe1,width=830,height=2,bg="black",highlightthickness=2,highlightbackground="black")
        row6.place(y=200)

        row7 = Frame(tableframe1,width=830,height=2,bg="black",highlightthickness=2,highlightbackground="black")
        row7.place(y=240)

        row8 = Frame(tableframe1,width=830,height=2,bg="black",highlightthickness=2,highlightbackground="black")
        row8.place(y=280)

        row9 = Frame(tableframe1,width=830,height=2,bg="black",highlightthickness=2,highlightbackground="black")
        row9.place(y=320)

        #NOW FOR THE COLUMNS
        col1 = Frame(tableframe1,width=2,height=280,bg="black",highlightthickness=2,highlightbackground="black")
        col1.place(x=100,y=40)

        col2 = Frame(tableframe1,width=2,height=280,bg="black",highlightthickness=2,highlightbackground="black")
        col2.place(x=333,y=40)

        col3 = Frame(tableframe1,width=2,height=280,bg="black",highlightthickness=2,highlightbackground="black")
        col3.place(x=490,y=40)

        col4 = Frame(tableframe1,width=2,height=280,bg="black",highlightthickness=2,highlightbackground="black")
        col4.place(x=647,y=40)


        # global name_label
        name = Label(tableframe1,text="Name:",bg="white",font=("Microsoft Yahei UI Light",14))
        name.place(x=10,y=screen_height/50-3)
        name_label = Entry(tableframe1,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16),width=25)
        name_label.place(x=75,y=screen_height/50-1)


        DOB = Label(tableframe1,text="Date Of Birth:",bg="white",font=("Microsoft Yahei UI Light",16))
        DOB.place(x=495,y=screen_height/50-3)
        DOB_label = Entry(tableframe1,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16),width=13)
        DOB_label.place(x=630,y=screen_height/50-1)



        #CREATING THE FORMAT FOR RESULT
        SN = Label(tableframe1,text="S.No",bg="white",font=("Microsoft Yahei UI Light",16))
        SN.place(x=15,y=45)

        subject = Label(tableframe1,text="Subject",bg="white",font=("Microsoft Yahei UI Light",16))
        subject.place(x=170,y=45)

        Fmark = Label(tableframe1,text="Full Marks",bg="white",font=("Microsoft Yahei UI Light",16))
        Fmark.place(x=365,y=45)

        Pmark = Label(tableframe1,text="Pass Marks",bg="white",font=("Microsoft Yahei UI Light",16))
        Pmark.place(x=515,y=45)

        Omark = Label(tableframe1,text="Obtained Marks",bg="white",font=("Microsoft Yahei UI Light",16))
        Omark.place(x=657 ,y=45)

        #adding sn
        one = Label(tableframe1,text="1",bg="white",font=("Microsoft Yahei UI Light",16))
        one.place(x=30,y=85)

        two = Label(tableframe1,text="2",bg="white",font=("Microsoft Yahei UI Light",16))
        two.place(x=30,y=125)

        three = Label(tableframe1,text="3",bg="white",font=("Microsoft Yahei UI Light",16))
        three.place(x=30,y=165)

        four = Label(tableframe1,text="4",bg="white",font=("Microsoft Yahei UI Light",16))
        four.place(x=30,y=205)

        five = Label(tableframe1,text="5",bg="white",font=("Microsoft Yahei UI Light",16))
        five.place(x=30,y=245)

        six = Label(tableframe1,text="6",bg="white",font=("Microsoft Yahei UI Light",16))
        six.place(x=30,y=285)


        #ENTRY FOR SUBJECTS(x-coordinate from SUBJECT column and y- coordinate from respective S.N)
        sub1=Label(tableframe1,text="English",bg="white",font=("Microsoft Yahei UI Light",16))
        sub1.place(x=120,y=85)

        sub2=Label(tableframe1,text="Nepali",bg="white",font=("Microsoft Yahei UI Light",16))
        sub2.place(x=120,y=125)

        sub3=Label(tableframe1,text="Physics",bg="white",font=("Microsoft Yahei UI Light",16))
        sub3.place(x=120,y=165)

        sub4=Label(tableframe1,text="Chemistry",bg="white",font=("Microsoft Yahei UI Light",16))
        sub4.place(x=120,y=205)

        sub5=Label(tableframe1,text="Maths",bg="white",font=("Microsoft Yahei UI Light",16))
        sub5.place(x=120,y=245)

        sub6=Label(tableframe1,text="Computer",bg="white",font=("Microsoft Yahei UI Light",16))
        sub6.place(x=120,y=285)

        #ENTRY FOR FULL MARKS(x-coordinate from FULL MARKS column and y- coordinate from respective S.N)
        FM1=Label(tableframe1,text="100",bg="white",font=("Microsoft Yahei UI Light",16))
        FM1.place(x=353,y=85)

        FM2=Label(tableframe1,text="100",bg="white",font=("Microsoft Yahei UI Light",16))
        FM2.place(x=353,y=125)

        FM3=Label(tableframe1,text="100",bg="white",font=("Microsoft Yahei UI Light",16))
        FM3.place(x=353,y=165)

        FM4=Label(tableframe1,text="100",bg="white",font=("Microsoft Yahei UI Light",16))
        FM4.place(x=353,y=205)

        FM5=Label(tableframe1,text="100",bg="white",font=("Microsoft Yahei UI Light",16))
        FM5.place(x=353,y=245)

        FM6=Label(tableframe1,text="100",bg="white",font=("Microsoft Yahei UI Light",16))
        FM6.place(x=353,y=285)

        #ENTRY FOR PASS MARKS(x-coordinate from PASS MARKS column and y- coordinate from respective S.N)
        PM1=Label(tableframe1,text="40",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        PM1.place(x=510,y=85)

        PM2=Label(tableframe1,text="40",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        PM2.place(x=510,y=125)

        PM3=Label(tableframe1,text="40",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        PM3.place(x=510,y=165)

        PM4=Label(tableframe1,text="40",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        PM4.place(x=510,y=205)

        PM5=Label(tableframe1,text="40",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        PM5.place(x=510,y=245)

        PM6=Label(tableframe1,text="40",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        PM6.place(x=510,y=285)


        #ENTRY FOR OBTAINED MARKS(x-coordinate from OBTAINED MARKS(+13 for bette look) column and y- coordinate from respective S.N)
        OM1=Entry(tableframe1,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        OM1.place(x=667,y=85)

        OM2=Entry(tableframe1,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        OM2.place(x=667,y=125)

        OM3=Entry(tableframe1,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        OM3.place(x=667,y=165)

        OM4=Entry(tableframe1,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        OM4.place(x=667,y=205)

        OM5=Entry(tableframe1,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        OM5.place(x=667,y=245)

        OM6=Entry(tableframe1,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        OM6.place(x=667,y=285)

        #result and percent label
        result=Label(tableframe1,text="Result:",bg="white",font=("Microsoft Yahei UI Light",16))
        result.place(x=30,y=325)
        resultEntry=Entry(tableframe1,width=20,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        resultEntry.place(x=100,y=328)

        percent=Label(tableframe1,text="Percentage:",bg="white",font=("Microsoft Yahei UI Light",16))
        percent.place(x=620,y=325)
        percentEntry=Entry(tableframe1,width=7,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
        percentEntry.place(x=735,y=328)

        counter=1
        for item in sleep:       
            for value in item:
                if counter==2:
                         
                    name_label.insert(0,value)
                    
                    name_label.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",15,"bold"))
                if counter==3:
                    
                    DOB_label.insert(0,value)
                    DOB_label.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",15,"bold"))

                if counter==4:
                    
                    percentEntry.insert(0,value)
                    percentEntry.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",15,"bold"))
                    
                if counter==6:
                    
                    resultEntry.insert(0,value)
                    resultEntry.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",15,"bold"))

                counter+=1

        try:
            cd.execute("SELECT * FROM obtainedmarks WHERE std_id =? ", [check_student_id])
            
            data=cd.fetchall()
            
        except Exception as s:
            messagebox.showerror("Error",s)
        
        counter = 0
        for item in data:       
            for value in item:
                
                if counter==1:
                    
                    OM1.insert(0,value)
                    OM1.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",16))

                
                    
                if counter==2:
                    
                    OM2.insert(0,value)
                    OM2.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",16))

                if counter==3:
                    
                    OM3.insert(0,value)
                    OM3.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",16))

                if counter==4:
                    
                    OM4.insert(0,value)
                    OM4.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",16))


                if counter==5:
                    
                    OM5.insert(0,value)
                    OM5.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",16))

                if counter==6:
                    
                    OM6.insert(0,value)
                    OM6.config(state=DISABLED,disabledbackground = "white", disabledforeground="black", font=("Microsoft Yahei UI Light",16))
                counter+=1
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Error","Invalid information")
    
c=Button(frame2,width=29,pady=7,text="Fetch Result",bg="#57a1f8",fg="white",border=0,font=buttonFont1,activebackground="#57a1f8",activeforeground="white",command=result)
c.place(x=18,y=235)
c.bind('<Enter>',o_enter)
c.bind('<Leave>',o_leave)

mainloop()