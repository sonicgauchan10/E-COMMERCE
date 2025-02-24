from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
from tkcalendar import DateEntry
import tkinter.font as font
import sqlite3
import runpy

#creating root after the teacher logs in
account=Tk()
account.configure(bg="white")
account.attributes("-fullscreen",True)

screen_width = account.winfo_screenwidth()
screen_height= account.winfo_screenheight()

buttonFont1 = font.Font(size=13)
buttonFont2 = font.Font(size=26,weight="bold",family="Microsoft Yahei UI Light")

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


def on_edit():
    global tableframe

    tableframe = Frame(account,width=screen_width/1.55,height=(screen_height/2)+10,bg="white",highlightthickness=2,highlightbackground="black")
    tableframe.place(x=280,y=320)
    
    #creating a var for position of the line in the table
    pos = ((screen_height/2)+10)/8

    #TO SEARCH


    row1 = Frame(tableframe,width=screen_width/1.55,height=3,bg="black",highlightthickness=2,highlightbackground="black")
    row1.place(y=pos)
    pos=pos+pos

    row2 = Frame(tableframe,width=screen_width/1.55,height=3,bg="black",highlightthickness=2,highlightbackground="black")
    row2.place(y=pos)
    pos=pos+(pos*0.5)

    row3 = Frame(tableframe,width=screen_width/1.55,height=2,bg="black",highlightthickness=2,highlightbackground="black")
    row3.place(y=pos)
    pos=pos+pos*0.34

    row4 = Frame(tableframe,width=screen_width/1.55,height=2,bg="black",highlightthickness=2,highlightbackground="black")
    row4.place(y=pos)
    pos=pos+pos*0.25

    row5 = Frame(tableframe,width=screen_width/1.55,height=2,bg="black",highlightthickness=2,highlightbackground="black")
    row5.place(y=pos)
    pos=pos+pos*0.18

    row6 = Frame(tableframe,width=screen_width/1.55,height=2,bg="black",highlightthickness=2,highlightbackground="black")
    row6.place(y=pos)
    pos=pos+pos*0.16

    row6 = Frame(tableframe,width=screen_width/1.55,height=2,bg="black",highlightthickness=2,highlightbackground="black")
    row6.place(y=pos)

    #NOW FOR THE COLUMNS
    pos = (screen_width/1.55)/8

    col1 = Frame(tableframe,width=2,height=1500,bg="black",highlightthickness=2,highlightbackground="black")
    col1.place(x=pos,y=((screen_height/2)+10)/8)
    pos=pos*3.5

    col2 = Frame(tableframe,width=2,height=1500,bg="black",highlightthickness=2,highlightbackground="black")
    col2.place(x=pos-25,y=((screen_height/2)+10)/8)
    pos=pos+pos*0.5

    col3 = Frame(tableframe,width=2,height=1500,bg="black",highlightthickness=2,highlightbackground="black")
    col3.place(x=pos-55,y=((screen_height/2)+10)/8)
    pos=pos+pos*0.18

    col4 = Frame(tableframe,width=2,height=1500,bg="black",highlightthickness=2,highlightbackground="black")
    col4.place(x=pos*1.09-53,y=((screen_height/2)+10)/8)
    pos=pos+pos*0.18



    name = Label(tableframe,text="Name:",bg="white",font=("Microsoft Yahei UI Light",14))
    name.place(x=10,y=screen_height/50-5)

    name_label = Entry(tableframe,fg="black",border=1,bg="white",font=("Microsoft Yahei UI Light",14),width=25)
    name_label.place(x=75,y=screen_height/50-4)
    
    DOB = Label(tableframe,text="Date Of Birth:",bg="white",font=("Microsoft Yahei UI Light",16))
    DOB.place(x=490,y=screen_height/50-5)
    DOB_label = DateEntry(tableframe,fg="black",border=1,bg="white",font=("Microsoft Yahei UI Light",14),width=13)
    DOB_label.place(x=625,y=screen_height/50-4)
    DOB_label.delete(0,END)


    #CREATING THE FORMAT FOR RESULT
    SN = Label(tableframe,text="S.No",bg="white",font=("Microsoft Yahei UI Light",16))
    SN.place(x=screen_width/60-0,y=screen_height/15+5)

    subject = Label(tableframe,text="Subject",bg="white",font=("Microsoft Yahei UI Light",16))
    subject.place(x=screen_width/10+40,y=screen_height/15+5)

    Fmark = Label(tableframe,text="Full Marks",bg="white",font=("Microsoft Yahei UI Light",16))
    Fmark.place(x=screen_width/3.5-8,y=screen_height/15+5)

    Pmark = Label(tableframe,text="Pass Marks",bg="white",font=("Microsoft Yahei UI Light",16))
    Pmark.place(x=screen_width/2.4-25,y=screen_height/15+5)

    Omark = Label(tableframe,text="Obtained Marks",bg="white",font=("Microsoft Yahei UI Light",16))
    Omark.place(x=screen_width/2+17,y=screen_height/15+5)

    #adding sn
    one = Label(tableframe,text="1",bg="white",font=("Microsoft Yahei UI Light",16))
    one.place(x=screen_width/60 + 15,y=screen_height/7)

    two = Label(tableframe,text="2",bg="white",font=("Microsoft Yahei UI Light",16))
    two.place(x=screen_width/60 + 15,y=screen_height/5)

    three = Label(tableframe,text="3",bg="white",font=("Microsoft Yahei UI Light",16))
    three.place(x=screen_width/60 + 15,y=screen_height/3.8+5)

    four = Label(tableframe,text="4",bg="white",font=("Microsoft Yahei UI Light",16))
    four.place(x=screen_width/60 + 15,y=screen_height/3.07)

    five = Label(tableframe,text="5",bg="white",font=("Microsoft Yahei UI Light",16))
    five.place(x=screen_width/60 + 15,y=screen_height/2.6)

    six = Label(tableframe,text="6",bg="white",font=("Microsoft Yahei UI Light",16))
    six.place(x=screen_width/60 + 15,y=screen_height/2.2)


    #ENTRY FOR SUBJECTS(x-coordinate from SUBJECT column and y- coordinate from respective S.N)
    sub1=Entry(tableframe,width=17,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    sub1.place(x=screen_width/10-10,y=screen_height/7-2)

    sub2=Entry(tableframe,width=17,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    sub2.place(x=screen_width/10-10,y=screen_height/5+4)

    sub3=Entry(tableframe,width=17,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    sub3.place(x=screen_width/10-10,y=screen_height/3.8+5)

    sub4=Entry(tableframe,width=17,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    sub4.place(x=screen_width/10-10,y=screen_height/3.07+4)

    sub5=Entry(tableframe,width=17,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    sub5.place(x=screen_width/10-10,y=screen_height/2.6+5)

    sub6=Entry(tableframe,width=17,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    sub6.place(x=screen_width/10-10,y=screen_height/2.2)

    #ENTRY FOR FULL MARKS(x-coordinate from FULL MARKS column and y- coordinate from respective S.N)
    FM1=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    FM1.place(x=screen_width/3.5-8,y=screen_height/7-2)

    FM2=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    FM2.place(x=screen_width/3.5-8,y=screen_height/5+4)

    FM3=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    FM3.place(x=screen_width/3.5-8,y=screen_height/3.8+5)

    FM4=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    FM4.place(x=screen_width/3.5-8,y=screen_height/3.07+4)

    FM5=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    FM5.place(x=screen_width/3.5-8,y=screen_height/2.6+5)

    FM6=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    FM6.place(x=screen_width/3.5-8,y=screen_height/2.2)


    #ENTRY FOR PASS MARKS(x-coordinate from PASS MARKS column and y- coordinate from respective S.N)
    PM1=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    PM1.place(x=screen_width/2.4-25,y=screen_height/7-2)

    PM2=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    PM2.place(x=screen_width/2.4-25,y=screen_height/5+4)

    PM3=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    PM3.place(x=screen_width/2.4-25,y=screen_height/3.8+5)

    PM4=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    PM4.place(x=screen_width/2.4-25,y=screen_height/3.07+4)

    PM5=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    PM5.place(x=screen_width/2.4-25,y=screen_height/2.6+5)

    PM6=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    PM6.place(x=screen_width/2.4-25,y=screen_height/2.2)


    #ENTRY FOR OBTAINED MARKS(x-coordinate from OBTAINED MARKS(+13 for bette look) column and y- coordinate from respective S.N)
    OM1=Entry(tableframe,width=5,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    OM1.place(x=screen_width/2+30,y=screen_height/7-2)

    OM2=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    OM2.place(x=screen_width/2+30,y=screen_height/5+4)

    OM3=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    OM3.place(x=screen_width/2+30,y=screen_height/3.8+5)

    OM4=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    OM4.place(x=screen_width/2+30,y=screen_height/3.07+4)

    OM5=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    OM5.place(x=screen_width/2+30,y=screen_height/2.6+5)

    OM6=Entry(tableframe,width=10,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",16))
    OM6.place(x=screen_width/2+30,y=screen_height/2.2)

    search = Label(account,text="Search By:",fg="black",border=1,bg="white",font=("Microsoft Yahei UI Light",14,"bold"))
    search.place(x=255,y=243)
        

    def srch_leave1(w): 
            search_label.delete(0,"end")
            box = OptionMenu(account,clicked,"Student_ID","Name",command=srch_leave3)
            box.place(x=355,y=243) 
            


    def srch_leave3(a):    
            search_label.delete(0,"end")
            search_label.insert(0,"Student_ID")
            box = OptionMenu(account,clicked,"Student_ID","Name",command=srch_leave1)
            box.place(x=355,y=243)
            

# else:
#             search_label.delete(0,"end")
#             search_label.insert(0,"Name")


    def srch_enter(w):
        search_label.delete(0,"end")

    def srch_leave(w):
            if search_label =="":  
              search_label.insert(0,"Student_ID")

    clicked = StringVar()
    clicked.set("Student_ID")

    box = OptionMenu(account,clicked,"Student_ID","Name",command=srch_leave1)
    box.place(x=355,y=243)



    search_label = Entry(account,fg="black",border=1,bg="white",font=("Microsoft Yahei UI Light",12),width=25)
    search_label.place(x=255,y=280)
    search_label.insert(0,"Student_ID")
    search_label.bind('<FocusIn>',srch_enter)
    search_label.bind('<FocusOut>',srch_leave)

    def search_data():
        conn = sqlite3.connect("addressbook.db")
        c = conn.cursor()

        #when searched via student id       
        if(clicked.get()=="Student_ID"):
            c.execute("SELECT std_id FROM details")
            records = c.fetchall()
            
            flag = ""
            for record in records:
                for value in record:
                    if (value == search_label.get()):
                        flag = "true"
                        
            if (flag == "true"):
                #to fetch the subject details
                c.execute("SELECT * FROM subject")
                records = c.fetchall()
                flag = "" #to gain details of targated student 
                counter = 0
                for record in records: #picking one students detail at a time
                    for item in record: #individual data od that student
                        if item==search_label.get():
                            flag = "true"#target student's details verified
                    if flag=="true":#now that the targeted student is found inserting his details
                        # print(record)
                        for item in record:
                            if counter ==1:
                                sub1.delete(0,"end")#we delete first because if a data is fetched before it clears the label
                                sub1.insert(0,item)
                            elif counter ==2:
                                sub2.delete(0,"end")
                                sub2.insert(0,item)
                            elif counter ==3:
                                sub3.delete(0,"end")
                                sub3.insert(0,item)
                            elif counter ==4:
                                sub4.delete(0,"end")
                                sub4.insert(0,item)
                            elif counter ==5:
                                sub5.delete(0,"end")
                                sub5.insert(0,item)
                            elif counter ==6:
                                sub6.delete(0,"end")
                                sub6.insert(0,item)
                            counter +=1


                c.execute("SELECT * FROM fullmarks")
                records = c.fetchall()
                flag = ""
                counter = 0
                for record in records:
                    for item in record:
                        if item==search_label.get():
                            flag = "true"
                    if flag=="true":
                        # print(record)
                        for item in record:
                            if counter ==1:
                                FM1.delete(0,"end")
                                FM1.insert(0,item)
                            elif counter ==2:
                                FM2.delete(0,"end")
                                FM2.insert(0,item)
                            elif counter ==3:
                                FM3.delete(0,"end")
                                FM3.insert(0,item)
                            elif counter ==4:
                                FM4.delete(0,"end")
                                FM4.insert(0,item)
                            elif counter ==5:
                                FM5.delete(0,"end")
                                FM5.insert(0,item)
                            elif counter ==6:
                                FM6.delete(0,"end")
                                FM6.insert(0,item)
                            counter +=1


                c.execute("SELECT * FROM passmarks")
                records = c.fetchall()
                flag = ""
                counter = 0
                for record in records:
                    for item in record:
                        if item==search_label.get():
                            flag = "true"
                    if flag=="true":
                        # print(record)
                        for item in record:
                            if counter ==1:
                                PM1.delete(0,"end")
                                PM1.insert(0,item)
                            elif counter ==2:
                                PM2.delete(0,"end")
                                PM2.insert(0,item)
                            elif counter ==3:
                                PM3.delete(0,"end")
                                PM3.insert(0,item)
                            elif counter ==4:
                                PM4.delete(0,"end")
                                PM4.insert(0,item)
                            elif counter ==5:
                                PM5.delete(0,"end")
                                PM5.insert(0,item)
                            elif counter ==6:
                                PM6.delete(0,"end")
                                PM6.insert(0,item)
                            counter +=1


                c.execute("SELECT * FROM obtainedmarks")
                records = c.fetchall()
                flag = ""
                counter = 0
                for record in records:
                    for item in record:
                        if item==search_label.get():
                            flag = "true"
                    if flag=="true":
                        # print(record)
                        for item in record:
                            if counter ==1:
                                OM1.delete(0,"end")
                                OM1.insert(0,item)
                            elif counter ==2:
                                OM2.delete(0,"end")
                                OM2.insert(0,item)
                            elif counter ==3:
                                OM3.delete(0,"end")
                                OM3.insert(0,item)
                            elif counter ==4:
                                OM4.delete(0,"end")
                                OM4.insert(0,item)
                            elif counter ==5:
                                OM5.delete(0,"end")
                                OM5.insert(0,item)
                            elif counter ==6:
                                OM6.delete(0,"end")
                                OM6.insert(0,item)
                            counter +=1

                
                c.execute("SELECT * FROM details")
                records = c.fetchall()
                flag = ""
                counter = 0
                for record in records:
                    for item in record:
                        if item==search_label.get():
                            flag = "true"
                    if flag=="true":
                        # print(record)
                        for item in record:
                            if counter ==1:
                                name_label.delete(0,"end")
                                name_label.insert(0,item)
                            elif counter ==2:
                                DOB_label.delete(0,"end")
                                DOB_label.insert(0,item)
                            counter +=1
            else:
                messagebox.showerror("NOT FOUND","Please enter a valid Student ID")

        
  
        #when searched via student name            
        elif(clicked.get()=="Name"):
            c.execute("SELECT name FROM details")
            records = c.fetchall()
            
            flag = ""
            for record in records:
                for value in record:
                    if (value == search_label.get()):
                        flag = "true"
                    
            if(flag == "true"):
                #first we find the student id of the provided name
                c.execute("SELECT name,std_id from details")
                records = c.fetchall()
                # print(records)
                flag = ""
                container = ""
                vessel = search_label.get()
                for record in records:
                    for value in record:                   
                        if(vessel == value):
                            flag="true"
                            continue
                        if(flag=="true"):
                            container = value
                            flag = "" #we again change value for flag because it will stay true and always give the last students details

                
                #to fetch the subject details
                c.execute("SELECT * FROM subject")
                records = c.fetchall()
                flag = "" #to gain details of targated student 
                counter = 0
                for record in records: #picking one students detail at a time
                    for item in record: #individual data od that student
                        if item==container:
                            flag = "true"#target student's details verified
                    if flag=="true":#now that the targeted student is found inserting his details
                        # print(record)
                        for item in record:
                            if counter ==1:
                                sub1.delete(0,"end")#we delete first because if a data is fetched before it clears the label
                                sub1.insert(0,item)
                            elif counter ==2:
                                sub2.delete(0,"end")
                                sub2.insert(0,item)
                            elif counter ==3:
                                sub3.delete(0,"end")
                                sub3.insert(0,item)
                            elif counter ==4:
                                sub4.delete(0,"end")
                                sub4.insert(0,item)
                            elif counter ==5:
                                sub5.delete(0,"end")
                                sub5.insert(0,item)
                            elif counter ==6:
                                sub6.delete(0,"end")
                                sub6.insert(0,item)
                            counter +=1


                c.execute("SELECT * FROM fullmarks")
                records = c.fetchall()
                flag = ""
                counter = 0
                for record in records:
                    for item in record:
                        if item==container:
                            flag = "true"
                    if flag=="true":
                        # print(record)
                        for item in record:
                            if counter ==1:
                                FM1.delete(0,"end")
                                FM1.insert(0,item)
                            elif counter ==2:
                                FM2.delete(0,"end")
                                FM2.insert(0,item)
                            elif counter ==3:
                                FM3.delete(0,"end")
                                FM3.insert(0,item)
                            elif counter ==4:
                                FM4.delete(0,"end")
                                FM4.insert(0,item)
                            elif counter ==5:
                                FM5.delete(0,"end")
                                FM5.insert(0,item)
                            elif counter ==6:
                                FM6.delete(0,"end")
                                FM6.insert(0,item)
                            counter +=1


                c.execute("SELECT * FROM passmarks")
                records = c.fetchall()
                flag = ""
                counter = 0
                for record in records:
                    for item in record:
                        if item==container:
                            flag = "true"
                    if flag=="true":
                        # print(record)
                        for item in record:
                            if counter ==1:
                                PM1.delete(0,"end")
                                PM1.insert(0,item)
                            elif counter ==2:
                                PM2.delete(0,"end")
                                PM2.insert(0,item)
                            elif counter ==3:
                                PM3.delete(0,"end")
                                PM3.insert(0,item)
                            elif counter ==4:
                                PM4.delete(0,"end")
                                PM4.insert(0,item)
                            elif counter ==5:
                                PM5.delete(0,"end")
                                PM5.insert(0,item)
                            elif counter ==6:
                                PM6.delete(0,"end")
                                PM6.insert(0,item)
                            counter +=1


                c.execute("SELECT * FROM obtainedmarks")
                records = c.fetchall()
                flag = ""
                counter = 0
                for record in records:
                    for item in record:
                        if item==container:
                            flag = "true"
                    if flag=="true":
                        # print(record)
                        for item in record:
                            if counter ==1:
                                OM1.delete(0,"end")
                                OM1.insert(0,item)
                            elif counter ==2:
                                OM2.delete(0,"end")
                                OM2.insert(0,item)
                            elif counter ==3:
                                OM3.delete(0,"end")
                                OM3.insert(0,item)
                            elif counter ==4:
                                OM4.delete(0,"end")
                                OM4.insert(0,item)
                            elif counter ==5:
                                OM5.delete(0,"end")
                                OM5.insert(0,item)
                            elif counter ==6:
                                OM6.delete(0,"end")
                                OM6.insert(0,item)
                            counter +=1

                
                c.execute("SELECT * FROM details")
                records = c.fetchall()
                flag = ""
                counter = 0
                for record in records:
                    for item in record:
                        if item==container:
                            flag = "true"
                    if flag=="true":
                        # print(record)
                        for item in record:
                            if counter ==1:
                                name_label.delete(0,"end")
                                name_label.insert(0,item)
                            elif counter ==2:
                                DOB_label.delete(0,"end")
                                DOB_label.insert(0,item)
                            counter +=1
            else:
                messagebox.showerror("NOT FOUND","Please enter a valid Name")
        # print(clicked.get()) 
            
            
            
            
            


    
    search_btn = Button(account,text="Search",width=15,bg="#57a1f8",command=search_data)
    search_btn.place(x=490,y=280)
    
    # if(clicked.get()=="Name"):
    #     search_label = Entry(account,fg="black",border=1,bg="white",font=("Microsoft Yahei UI Light",12),width=25)
    #     search_label.place(x=350,y=295)
    #     search_label.insert(0,"Name")


    #SUBMIT THE DATA
    def entry():
        M1=(FM1.get())    
        M2=(FM2.get())
        M3=(FM3.get())
        M4=(FM4.get())
        M5=(FM5.get())
        M6=(FM6.get())  
        N1=(PM1.get())    
        N2=(PM2.get())
        N3=(PM3.get())
        N4=(PM4.get())
        N5=(PM5.get())
        N6=(PM6.get())  
        Mark1=(OM1.get())    
        Mark2=(OM2.get())
        Mark3=(OM3.get())
        Mark4=(OM4.get())
        Mark5=(OM5.get())
        Mark6=(OM6.get())
        name=name_label.get()
        for i in name:
            if i.isdigit()==True:
                messagebox.showerror("Error","Enter Correct Name")
                return
            else:
                pass 
        
        if M1.isdigit()==False or M2.isdigit()==False or M3.isdigit()==False or M4.isdigit()==False or M5.isdigit()==False or M6.isdigit()==False:
            messagebox.showerror("Error","Enter Marks in Number.")
            return

        
        if N1.isdigit()==False or N2.isdigit()==False or N3.isdigit()==False or N4.isdigit()==False or N5.isdigit()==False or N6.isdigit()==False:
            messagebox.showerror("Error","Enter Marks in Number.")
            return
        elif Mark1.isdigit()==False or Mark2.isdigit()==False or Mark3.isdigit()==False or Mark4.isdigit()==False or Mark5.isdigit()==False or Mark6.isdigit()==False:
            messagebox.showerror("Error","Enter Marks in Number.")
            return
        if 0<int(Mark1)<=int(M1) and 0<int(Mark2)<=int(M2) and 0<int(Mark3)<=int(M3) and 0<int(Mark4)<=int(M4) and 0<int(Mark5)<=int(M5) and 0<int(Mark6)<=int(M6):
            pass
        else:
            messagebox.showerror("Error","Enter Marks within Range.")
            return
        #to check weather the student has passed the the subjects
        def passorfail():
            if OM1.get()>=PM1.get() and OM2.get()>=PM2.get() and OM3.get()>=PM3.get() and OM4.get()>=PM4.get() and OM5.get()>=PM5.get() and OM6.get()>=PM6.get():
                return("Pass")
            else:
                return("Fail")

        #to calculate percentage of student
        def perc():
            if passorfail()=="Pass":
                total = int(FM1.get())+int(FM2.get())+int(FM3.get())+int(FM4.get())+int(FM5.get())+int(FM6.get())
                total_obtained = int(OM1.get())+int(OM2.get())+int(OM3.get())+int(OM4.get())+int(OM5.get())+int(OM6.get())
                percn = round(total_obtained/total*100,2)
                return(percn)
            else:
                return("-*-*-*-")

        #to know the division
        def div():
            if passorfail()=="Pass":
                if perc()>=80:
                    return("Distinction")
                elif perc()>=70:
                    return("First Division")
                elif perc()>=60:
                    return("Second Division")
                elif perc()>=40:
                    return("Third Division")
                else:
                    return("Not Graded")
            else:
                return("-*-*-*-")     

        

        # conn=sqlite3.connect(":memory:")
        conn = sqlite3.connect("addressbook.db")
        c = conn.cursor()

        if(clicked.get()=="Name"):
            c.execute("SELECT name FROM details")
            records = c.fetchall()
            
            flag = ""
            for record in records:
                for value in record:
                    if (value == search_label.get()):
                        flag = "true"
                    
            if(flag == "true"):
                #first we find the student id of the provided name
                c.execute("SELECT name,std_id from details")
                records = c.fetchall()
                # print(records)
                flag = ""
                container = ""
                vessel = search_label.get()
                for record in records:
                    for value in record:                   
                        if(vessel == value):
                            flag="true"
                            continue
                        if(flag=="true"):
                            container = value
                            flag = ""
        
        else:
            container = search_label.get()#The student id is there
        
        c.execute('''UPDATE subject SET               
                sub1 = :f1,
                sub2 = :f2,
                sub3 = :f3,
                sub4 = :f4,
                sub5 = :f5,
                sub6 = :f6
                WHERE std_id = :oid''',
                {
                "f1" : sub1.get(),
                "f2" : sub2.get(),
                "f3" : sub3.get(),
                "f4" : sub4.get(),
                "f5" : sub5.get(),
                "f6" : sub6.get(),
                "oid": container                       
                                                 
            })

       
        c.execute('''UPDATE fullmarks SET               
                full1 = :f1,
                full2 = :f2,
                full3 = :f3,
                full4 = :f4,
                full5 = :f5,
                full6 = :f6
                WHERE std_id = :oid''',
                {
                "f1" : FM1.get(),
                "f2" : FM2.get(),
                "f3" : FM3.get(),
                "f4" : FM4.get(),
                "f5" : FM5.get(),
                "f6" : FM6.get(),
                "oid": container                     
                                                 
            })

       
        c.execute('''UPDATE passmarks SET               
                pass1 = :f1,
                pass2 = :f2,
                pass3 = :f3,
                pass4 = :f4,
                pass5 = :f5,
                pass6 = :f6
                WHERE std_id = :oid''',
                {
                "f1" : PM1.get(),
                "f2" : PM2.get(),
                "f3" : PM3.get(),
                "f4" : PM4.get(),
                "f5" : PM5.get(),
                "f6" : PM6.get(),
                "oid": container                     
                                                 
            })

                                     

        c.execute('''UPDATE obtainedmarks SET               
                got1 = :f1,
                got2 = :f2,
                got3 = :f3,
                got4 = :f4,
                got5 = :f5,
                got6 = :f6
                WHERE std_id = :oid''',
                {
                "f1" : OM1.get(),
                "f2" : OM2.get(),
                "f3" : OM3.get(),
                "f4" : OM4.get(),
                "f5" : OM5.get(),
                "f6" : OM6.get(),
                "oid": container                       
                                                 
            })
            
       
        c.execute('''UPDATE details SET               
                name = :f1,
                dob = :f2,
                percentage = :f3,
                reasult = :f4,
                division = :f5                
                WHERE std_id = :oid''',
                {                                             
                "f1" : name_label.get(),
                "f2" : DOB_label.get(),
                "f3" : perc(),
                "f4" : passorfail(),
                "f5" : div(),
                "oid": container        
                })
                                     
        #show that the details has been updated        
        
        student = "The details of student '"+name_label.get()+"' Has been updated "
        answer = messagebox.showinfo("UPDATED",student)

        if (answer=="ok"):
            search_label.delete(0,"end")
            name_label.delete(0,"end")
            DOB_label.delete(0,"end")

            sub1.delete(0,"end")
            sub2.delete(0,"end")
            sub3.delete(0,"end")
            sub4.delete(0,"end")
            sub5.delete(0,"end")
            sub6.delete(0,"end")

            FM1.delete(0,"end")
            FM2.delete(0,"end")
            FM3.delete(0,"end")
            FM4.delete(0,"end")
            FM5.delete(0,"end")
            FM6.delete(0,"end")

            PM1.delete(0,"end")
            PM2.delete(0,"end")
            PM3.delete(0,"end")
            PM4.delete(0,"end")
            PM5.delete(0,"end")
            PM6.delete(0,"end")

            OM1.delete(0,"end")
            OM2.delete(0,"end")
            OM3.delete(0,"end")
            OM4.delete(0,"end")
            OM5.delete(0,"end")
            OM6.delete(0,"end")

        conn.commit()
        conn.close()

    
    global submit
    submit = Button(account,width=9,pady=1,text="Submit",bg="#57a1f8",fg="white",border=2,font=("Microsoft Yahei UI Light",16,"bold"),activebackground="#57a1f8",activeforeground="white",command=entry)
    submit.place(x=screen_width-140,y=screen_height/1.13+30)

#making the button work

def create():
    account.destroy()
    runpy.run_path(
        "final_create.py")

def edit():
    title_create=Label(display_frame,text="Edit",font=buttonFont,bg="#7ab3f5",width=94)
    title_create.place(x=250,y=215)
    on_edit()

def details():
    account.destroy()
    runpy.run_path(
        "final_detail.py")

def logout():
    msg_box =messagebox.askquestion('Confirm Logout', 'Are you sure you want to logout?',icon='warning')
    if msg_box == 'yes':
        account.destroy()
        runpy.run_path(
            "final_base.py")



#creating button in option bar
btn_create=Button(options_frame, text="CREATE", font= buttonFont,padx=78,pady=9,bg="#fcf0d7",relief=GROOVE,command=create)
btn_create.place(x=0,y=35)
btn_edit=Button(options_frame, text="EDIT", font= buttonFont,padx=95,pady=9,bg="white",relief=GROOVE,command=edit)
btn_edit.place(x=0,y=88)
btn_detail=Button(options_frame, text="DETAIL", font= buttonFont,padx=83,pady=9,bg="#fcf0d7",relief=GROOVE,command=details)
btn_detail.place(x=0,y=141)
btn_logout=Button(options_frame, text="LOGOUT", font= buttonFont,padx=77,pady=9,bg="#fcf0d7",relief=GROOVE,command=logout)
btn_logout.place(x=0,y=194)


#creating workspace
display_frame=Frame(width=screen_width-250,bg="#ffffff").pack(fill=BOTH,expand=TRUE,padx=(250,0),pady=(0,0))

#view function
def view():
    runpy.run_path(
        "top1.py")
#to view the result
btn_result=Button(display_frame,width=10,padx=55,text="View Result",bg="#57a1f8",fg="white",border=2,font=("Microsoft Yahei UI Light",16,"bold"),activebackground="#57a1f8",activeforeground="white",command=view)
btn_result.place(x=0,y=screen_height-49)

#for edit highlight
edit()




#creating template
img2=Image.open(r"eye1.png") #image logo
new_logo2=ImageTk.PhotoImage(img2)
image2=Label(display_frame,image=new_logo2,border=0).place(x=250,y=35)
account.mainloop()