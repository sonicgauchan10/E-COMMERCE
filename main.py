from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk


    # ------------------------------------ Creating the window for the system  ---------------------------------------------------


root = Tk()
root.geometry("1500x900")
root.config(bg='crimson')
root.title("Pharmacy Management System")
root.resizable(height=False, width=False)



    # ------------------------------------ Creating the class of the system  ---------------------------------------------------


class PharmacyManagementSystem:


    # ------------------------------------ function for creating a new user ---------------------------------------------------


    def signup(self):
        self.username = StringVar()
        self.password = StringVar()

        self.username = self.e1.get()
        self.password = self.e2.get() 
    
        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')

        create = '''create table if not exists login_details (username varchar(255), password varchar(255))'''

        insert = 'insert into login_details (username, password) values (%s, %s)'
        values= (self.username, self.password)

        cur = connection.cursor()
        cur.execute(create)
        cur.execute(insert,values)
        
        connection.commit()

        messagebox.showinfo('Signed Up',"Signed Up Successful")


    # ------------------------------------ function to check whether user exist or not  ---------------------------------------------------


    def Login_check(self):
        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
        self.user = StringVar()
        self.pas = StringVar()

        self.user = self.e1.get()
        self.pas = self.e2.get()

        
        if self.user=="" or self.pas=="":
            messagebox.showerror('Invalid',"Please Provide username and password")
        else :
            cursor = connection.cursor()
            cursor.execute("select * from login_details where username = %s and password = %s",(self.user, self.pas))
            a = cursor.fetchone()

            if a == None :
                messagebox.showerror('Invalid',"Invalid Credentials")
            else :
                messagebox.showinfo('Login successful',"Logged In")
                self.enable()
                self.login.destroy()


    # ------------------------------------ function to login the System ---------------------------------------------------


    def logins(self):
        
        self.login = Tk()
        self.login.config(bg='crimson')
        self.login.title('Login')
        self.login.resizable(height=True, width=True)
        self.login.geometry("400x400")

        # Labels

        l1 = Label(self.login, text="LOGIN", font=("Algerian", 22, 'bold'),bg= 'crimson' , fg = 'white')
        l1.pack()

        l2 = Label(self.login, text="Username", font=("Segoe UI", 20,'bold'),bg= 'crimson' , fg = 'white')
        l2.place(x= 132, y =60)

        l3 = Label(self.login, text="Password", font=("Segoe UI", 20,'bold'),bg= 'crimson' , fg = 'white')
        l3.place(x = 132, y =160)

        # Entry

        self.e1 = Entry(self.login, font=("Segoe UI", 20,'bold'))
        self.e1.place(x= 40, y= 110)
    
        self.e2 = Entry(self.login, font=("Segoe UI", 20,'bold'), show="*")
        self.e2.place(x = 40, y = 210)

        # buttons 

        loginbtn = Button(self.login,text="Login", font=("Segoe UI",15, 'bold'), bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5, command=self.Login_check)
        loginbtn.place(x=200, y = 320, width=150)

        signupbtn = Button(self.login,text="Sign Up", font=("Segoe UI",15, 'bold'), bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5, command=self.signup)
        signupbtn.place(x=50, y = 320, width=150)


    # ------------------------------------ function to call the system ---------------------------------------------------


    def main(self):
        self.frames()
        self.med_info()
        self.addmed()
        self.addmed_button()
        self.options()
        self.sideframe_edit()
        self.downframe_edit()
        self.fetch_med_info()


    # ------------------------------------ defining all the frames of the function ---------------------------------------------------


    def frames(self):

        # Main Page 

        self.phar =Label(root, text="PHARMACY MANAGEMENT SYSTEM", font=("Segoe UI",50, 'bold'),bg='crimson', fg='white', relief='raised', bd=10, width=100)
        self.phar.pack()

        # Place the add medicine and medicine details window here

        self.med = Frame(root, height=400, width=1500, bd=10, relief='raised', bg ='crimson')
        self.med.place(x=0, y=110)

        # Place the buttons inside this frame 

        self.opt = Frame(root, height=100, width=1500, bd=10, relief='raised', bg ='crimson')
        self.opt.place(x=0, y=510)

        # print the details from the server to the python window 

        self.show = Frame(root, height=290, width=1500, bd=10, relief='raised', bg ='crimson')
        self.show.place(x=0, y=610)

        # Add the medicine deatils window

        self.med_frame = Frame(self.med, height=360, width= 900, bd=5, relief='raised', bg ='crimson')
        self.med_frame.place(x=10, y=10)

        # add medicine window

        self.med_add = Frame(self.med, height=360, width= 550, bd=5, relief='raised', bg ='crimson')
        self.med_add.place(x=920, y=10)

        # creatting the side frame 

        self.side_frame = Frame(self.med_add)
        self.side_frame.place(x=20, y=110, height=150, width=500)

        # creating the down frame 

        self.down_frame = Frame(self.show)
        self.down_frame.place(x=15,y=10, height=250, width= 1450)

        # scrolling bar for the side frame
    

    # ------------------------------------ Desiging the side frame  ---------------------------------------------------


    def sideframe_edit(self):

        sidex = ttk.Scrollbar(self.side_frame,orient=HORIZONTAL)
        sidex.pack(side=BOTTOM, fill=X)

        sidey = ttk.Scrollbar(self.side_frame,orient=VERTICAL)
        sidey.pack(side=RIGHT, fill=Y)

        # creating the tree for the details to show on and fetch from the database

        self.tree = ttk.Treeview(self.side_frame, columns=("ref", "medicine"),xscrollcommand=sidex.set, yscrollcommand=sidey.set)

        # configuring the side panel 

        sidex.config(command=self.tree.xview)
        sidey.config(command=self.tree.yview)

        # assigning the heading to the columns in the frame 

        self.tree.heading("ref", text="Reference No.")
        self.tree.heading("medicine", text="Medicine")

        self.tree["show"] = "headings"
        self.tree.pack(fill=BOTH, expand=1)

        # assigning the width 

        self.tree.column("ref", width=100)
        self.tree.column("medicine", width=100)


    # ------------------------------------ Designing the down frame ---------------------------------------------------


    def downframe_edit(self):

        dsidex = ttk.Scrollbar(self.down_frame, orient=HORIZONTAL)
        dsidex.pack(side=BOTTOM, fill=X)

        dsidey = ttk.Scrollbar(self.down_frame, orient=VERTICAL)
        dsidey.pack(side=RIGHT, fill=Y)

        # creating the tree

        self.dtree = ttk.Treeview(self.down_frame, columns=("Reference No.","Company Name", "Type of Medicine", "Medicine Name", "Issue Date","Expiry Date", "Uses","Side Effects","Price","Quantity"), xscrollcommand=dsidex, yscrollcommand=dsidey)

        # configure the tree

        dsidex.config(command=self.dtree.xview)
        dsidey.config(command=self.dtree.xview)

        # headings

        self.dtree.heading("Reference No.", text="Reference No.")
        self.dtree.heading("Company Name", text="Company Name")
        self.dtree.heading("Type of Medicine", text="Type of Medicine")
        self.dtree.heading("Medicine Name", text="Medicine Name")
        self.dtree.heading("Issue Date", text="Issue Date")
        self.dtree.heading("Expiry Date", text="Expiry Date")
        self.dtree.heading("Uses", text="Uses")
        self.dtree.heading("Side Effects", text="Side Effects")
        self.dtree.heading("Price", text="Price")
        self.dtree.heading("Quantity", text="Quantity")

        self.dtree["show"] = "headings"
        self.dtree.pack(fill=BOTH, expand=1)

        # assigning the width 

        self.dtree.column("Reference No.",width=100)
        self.dtree.column("Company Name",width=100)
        self.dtree.column("Type of Medicine",width=100)
        self.dtree.column("Medicine Name",width=100)
        self.dtree.column("Issue Date",width=100)
        self.dtree.column("Expiry Date",width=100)
        self.dtree.column("Uses",width=100)
        self.dtree.column("Side Effects",width=100)
        self.dtree.column("Price",width=100)
        self.dtree.column("Quantity",width=100)


    # ------------------------------------ Designing the main window  ---------------------------------------------------

    
    def med_info(self):

        # medicine Additon 

        med_info = Label(self.med, text="Medicine Information", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        med_info.place(x=30,y=0)

        # reference numeber
        # company name
        # types of medicine 
        # medicine name 
        # issue date 
        # exp date
        # uses: 
        # side effects
        # price 
        # quantity

        l1 = Label(self.med_frame, text="Reference Number", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l1.place(x= 30, y=30)

        l2 = Label(self.med_frame, text="Company Name :", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l2.place(x= 30, y=80)

        l3 = Label(self.med_frame, text="Type Of Medicine", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l3.place(x= 30, y=130)

        l4 = Label(self.med_frame, text="Medicine Name", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l4.place(x= 30, y=180)

        l5 = Label(self.med_frame, text="Issue Date :", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l5.place(x= 30, y=230)

        l6 = Label(self.med_frame, text="Exp Date :", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l6.place(x= 30, y=280)

        l7 = Label(self.med_frame, text="Uses :", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l7.place(x= 490, y=30)

        l8 = Label(self.med_frame, text="Side Effects :", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l8.place(x= 490, y=80)

        l9 = Label(self.med_frame, text="Price :", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l9.place(x= 490, y=130)

        l10 = Label(self.med_frame, text="Quantity :", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l10.place(x= 490, y=180)

        # refernece entry 
        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
        cursor = connection.cursor()
        cursor.execute("Select Reference_Number from med_info")
        a = cursor.fetchall()

        # comobo box

        self.comboboxref = ttk.Combobox(self.med_frame,state="readonly", font=("Segoe UI", 12, 'bold'))
        self.comboboxref['value']=a
        if len(a) > 0:
            self.comboboxref['values'] = a
            self.comboboxref.current(0)  # Select first item
        else:
            self.comboboxref['values'] = ["No Data"]  # Placeholder to prevent error

        self.comboboxref.place(x = 250, y=30, width=205, height=30)

        # company name 

        self.comp = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.comp.place(x=250, y= 80)

        # type of medicine

        self.comboboxtom = ttk.Combobox(self.med_frame, state="readonly", font=("Segoe UI", 12, 'bold'))
        self.comboboxtom['values']=["Tablet","Drops","Injection"]
        self.comboboxtom.current(0)
        self.comboboxtom.place(x=250, y=130, width=205, height=30)

        # medicine name 
        
        cursor.execute("Select Medicine_Name from med_info")
        b = cursor.fetchall()

        self.comboboxname = ttk.Combobox(self.med_frame, state="readonly", font=("Segoe UI", 12, 'bold'))
        self.comboboxname['values'] = b
        self.comboboxname.current(0)
        self.comboboxname.place(x=250, y=180, width=205, height=30)

        # issue date 

        self.i_date = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.i_date.place(x=250, y=230)

        # expiry date

        self.e_date = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.e_date.place(x=250, y=280)

        # uses

        self.uses = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.uses.place(x= 650, y=30)

        # side effects

        self.side_effect = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.side_effect.place(x= 650, y=80)

        # price

        self.price = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.price.place(x= 650, y=130)

        # quantity 

        self.quantity = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.quantity.place(x= 650, y=180)

        connection.commit()
        connection.close()


    # ------------------------------------ Designing the Add Medicine Departmaent  ---------------------------------------------------


    def addmed(self):

        self.add_new = Label(self.med, text="Add New Medicine", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        self.add_new.place(x=940,y=0)

        # labels

        l11 = Label(self.med_add, text="Reference Number", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l11.place(x = 20, y = 20)

        l12 = Label(self.med_add, text="Medicine Name", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white')
        l12.place(x = 20, y = 60)

        # entries

        # Refernece Number

        self.ref_add = Entry(self.med_add, font=("Segoe UI", 13, 'bold'))
        self.ref_add.place(x= 250, y=20)

        self.med_name = Entry(self.med_add, font=("Segoe UI", 13, 'bold'))
        self.med_name.place(x= 250, y=60)


    # ------------------------------------ Designing the Add Medicine Departmaent (Buttons)  ---------------------------------------------------


    def addmed_button(self):

        # add

        self.add_btn = Button(self.med_add,text="Add", font=("Segoe UI",13, 'bold'), command=self.med_btn_add, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.add_btn.place(x =15, y = 290, width=120)

        # update 

        self.update_btn = Button(self.med_add,text="Update", font=("Segoe UI",13, 'bold'), command=self.med_btn_update, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.update_btn.place(x =145, y = 290, width=120)

        # delete
        self.delete_btn = Button(self.med_add,text="Delete", font=("Segoe UI",13, 'bold'), command=self.med_btn_delete, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.delete_btn.place(x =275, y = 290, width=120)

        # clear

        self.clear_btn = Button(self.med_add,text="Clear", font=("Segoe UI",13, 'bold'), command=self.med_btn_clear, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.clear_btn.place(x =405, y = 290, width=120)


    # ------------------------------------ Designing Options Menu To Perform the Function  ---------------------------------------------------


    def options(self):

        # add

        self.addbtn = Button(self.opt,text="Add", font=("Segoe UI",15, 'bold'), command=self.add, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.addbtn.place(x =10, y = 0, width=150, height=80)

        # update 

        self.updatebtn = Button(self.opt,text="Update", font=("Segoe UI",15, 'bold'), command=self.update, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.updatebtn.place(x =160, y = 0, width=150, height=80)

        # delete

        self.deletebtn = Button(self.opt,text="Delete", font=("Segoe UI",15, 'bold'), command=self.delete, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.deletebtn.place(x =310, y = 0, width=150, height=80)

        # reset

        self.resetbtn = Button(self.opt,text="Reset", font=("Segoe UI",15, 'bold'), command=self.reset, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.resetbtn.place(x =460, y = 0, width=150, height=80)

        # search 

        self.searchbtn = Button(self.opt,text="Search", font=("Segoe UI",15, 'bold'), command=self.search, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.searchbtn.place(x =610, y = 0, width=150, height=80)

        # show all 

        self.showbtn = Button(self.opt,text="Show All", font=("Segoe UI",15, 'bold'), command=self.showall, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.showbtn.place(x =760, y = 0, width=150, height=80)

        # exit

        self.exitbtn = Button(self.opt,text="Exit", font=("Segoe UI",15, 'bold'), command=self.exit, bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5)
        self.exitbtn.place(x =1320, y = 0, width=150, height=80)

        # login 

        self.login = Button(self.opt,text="Login", font=("Segoe UI",15, 'bold'), bg='crimson', fg='white', activebackground='green', activeforeground='white', bd=5, command=self.logins)
        self.login.place(x =1170, y = 0, width=150, height=80)


    # ------------------------------------ Function to add new medicine in add medicine department  ---------------------------------------------------


    def med_btn_add(self):
        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
        ref_no = StringVar()
        medi = StringVar()

        ref_no = self.ref_add.get()
        medi = self.med_name.get()
        if ref_no == "" or medi == "":
            messagebox.showwarning('Invalid',"Please Provide Proper Information.")
        else:
            create = '''create table if not exists med_info(Reference_Number varchar(255), Medicine_Name varchar(255))'''

            cur = connection.cursor()
            cur.execute(create)
            cur.execute('insert into med_info(Reference_Number, Medicine_Name) values (%s,%s)',(ref_no,medi))
            A = messagebox.askyesno('Question',"Have You Entered All The Values?")
            if A > 0:
                connection.commit()
                messagebox.showinfo('Data',"Data Added Successfully")
                connection.close()
                self.fetch_med_info()
                self.main()
            else:
                pass
        

    # ------------------------------------ Function to clear fields in add medicine department  ---------------------------------------------------


    def med_btn_clear(self):  
        self.ref_add.delete(0,END)
        self.med_name.delete(0,END)


    # ------------------------------------ Function to update fields in add medicine department  ---------------------------------------------------


    def med_btn_update(self):
        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
        ref_no = self.ref_add.get()
        medi = self.med_name.get()
        
        if ref_no == "":
            messagebox.showwarning('Data',"Please Provide The Reference Number")
        elif medi == "":
            messagebox.showwarning('Data',"Medicine Name Cannot Be Empty")
        else: 
            A = messagebox.askyesno('Question',"Are you sure you want to Update?")
            if A > 0:
                cursor = connection.cursor()
                cursor.execute("Update med_info set medicine_name = %s where reference_number = %s", (medi, ref_no))
                connection.commit()
                connection.close()
                messagebox.showinfo('Updation',"Data Has been Updated")
                self.main()
            else:
                pass


    # ------------------------------------ Function to delete medicine from add medicine department  ---------------------------------------------------


    def med_btn_delete(self):
        if self.ref_add.get() == "":
            messagebox.showwarning('Invalid',"Please Provide The Reference No")
        else:
            A = messagebox.askyesno('Question',"Are you sure you want to Delete?")
            if A > 0:
                connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
                cursor = connection.cursor()

                ref=self.ref_add.get()
                cursor.execute("delete from med_info where reference_number=%s",(ref,))
                connection.commit()
                connection.close()

                messagebox.showinfo('Deleted',"Data Deleted")
                self.fetch_med_info()  
            else:
                pass
    

    # ------------------------------------ Function to fetch medicine information from add medicine department  ---------------------------------------------------


    def fetch_med_info(self):
        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
        cursor = connection.cursor()
        cursor.execute("select reference_number, Medicine_Name from med_info")
        rows = cursor.fetchall()
        if len(rows)!=0:
            self.tree.delete(*self.tree.get_children())
            for i in rows: 
                self.tree.insert("", END, values=i)
            connection.commit()
        connection.close()

    
    # ------------------------------------ Function to add main record  ---------------------------------------------------


    def add(self):
        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')

        refno = self.comboboxref.get()
        TypeOfmed= self.comboboxtom.get()
        compname = self.comp.get()
        IssueDate = self.i_date.get()
        ExpiryDate = self.e_date.get()
        Uses = self.uses.get()
        SideEffects = self.side_effect.get()
        Price= self.price.get()
        Qty = self.quantity.get()

        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
        if refno == "" or TypeOfmed == "" or compname=="" or IssueDate == "" or ExpiryDate == "" or Uses == "" or SideEffects == "" or Price =="" or Qty=="":
            messagebox.showwarning('Invalid',"Please Provide All Information.")
        else:
            cursor=connection.cursor()
            A = messagebox.askyesno('Question',"Have You Enter All The Information?")
            if A > 0:
                cursor.execute("update med_info set IssueDate=%s,company_name=%s,TypeOfMedicine=%s,ExpiryDate=%s,Uses=%s,SideEffects=%s,Price=%s, Quantity=%s where reference_number=%s",(IssueDate,compname,TypeOfmed,ExpiryDate,Uses,SideEffects,Price,Qty, refno))
                connection.commit()
                connection.close()
                messagebox.showinfo('Added',"Data Added Successfully")
                self.fetch_down()
            else:
                pass


    # ------------------------------------ Function to reset the window  ---------------------------------------------------


    def reset(self):   
        A = messagebox.askyesno('Question',"Are you sure you want to Reset?")
        if A > 0:
            self.main()
            self.comboboxtom.set('Choose Medicine Type')
            self.comboboxname.set('Choose Medicine Name')
            self.comboboxref.set(self.comboboxref.current())
        else:
            pass
        

    # ------------------------------------ Function to fetch the main record  ---------------------------------------------------


    def update_fetch(self):
        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
        refno = self.comboboxref.get()
        cursor = connection.cursor()
        cursor.execute("select * from med_info where reference_number=%s",(refno,))
        a = cursor.fetchone()  
        if a == None: 
            messagebox.showerror('Error', "Please Select Reference No.")
        elif a[1] == None or a[2] == None or a[3] == None or a[4] == None or a[5] == None or a[6] == None or a[7] == None or a[8] == None or a[9] == None:
            messagebox.showwarning('Invalid',"Record Doesn't Exist, Please Add it first.")
            self.main()
        elif self.comp.get() == "" or self.comboboxtom.get() == "" or self.comboboxname.get() == "" or self.i_date.get() == "" or self.e_date.get() == "" or self.uses.get() == "" or self.side_effect.get()=="" or self.price.get()=="" or self.quantity.get()=="":
            self.comp.insert(0,a[1])
            self.comboboxtom.set(a[2])
            self.comboboxname.set(a[3])
            self.i_date.insert(0,a[4])
            self.e_date.insert(0,a[5])
            self.uses.insert(0,a[6])
            self.side_effect.insert(0,a[7])
            self.price.insert(0,a[8])
            self.quantity.insert(0,a[9])
            connection.commit()
            connection.close()
        else:
            self.add()

    
    # ------------------------------------ Function to update main record  ---------------------------------------------------


    def update(self):
        A = messagebox.askyesno('Question',"Have You Selected the Reference No?")
        if A > 0:
            self.update_fetch()
        else:
            pass
    

    # ------------------------------------ Function to delete the main record  ---------------------------------------------------


    def delete(self):
        A = messagebox.askyesno('Question',"Have You Selected the Reference No?")
        if A > 0:
            connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
            refno = self.comboboxref.get()
            cursor = connection.cursor()

            cursor.execute("delete from med_info where reference_number=%s",(refno,))
            connection.commit()
            connection.close()
            messagebox.showinfo('Deleted',"Data Has Been Deleted")
            self.main()
        else:
            pass
        

    # ------------------------------------ Function to search from the main record  ---------------------------------------------------


    def search(self):
        A = messagebox.askyesno('Question',"Have You Selected the Reference No?")
        if A > 0:
            refsno = self.comboboxref.get()
        
            connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
            
            cursor = connection.cursor()
            
            cursor.execute("select * from med_info where reference_number=%s",(refsno,))
            rows = cursor.fetchall()
            for i in rows: 
                self.dtree.insert("", END, values=i)
            connection.commit()
            connection.close()
        else:
            pass


    # ------------------------------------ Function to show all the record  ---------------------------------------------------


    def showall(self):
        self.fetch_down()


    # ------------------------------------ Function to fetch all the record  ---------------------------------------------------


    def fetch_down(self):
        self.main()
        connection = mysql.connector.connect(host='localhost', user='root', password='@Rischal17', database='pharmacy')
        cursor = connection.cursor()
        cursor.execute("select * from med_info")
        rows = cursor.fetchall()
        for i in rows: 
            self.dtree.insert("", END, values=i)
        connection.commit()
        connection.close()


    # ------------------------------------ Function to exit the system  ---------------------------------------------------


    def exit(self):
        a = messagebox.askokcancel('Exit', "Are you sure you want to exit?")
        if a == 0: 
            pass
        else:
            root.destroy()
    

    # ------------------------------------ Function to disable the system unless user logins  ---------------------------------------------------


    def disable(self):
        self.comboboxref.config(state="disabled")
        self.comp.config(state="disabled")
        self.comboboxtom.config(state="disabled")
        self.comboboxname.config(state="disabled")
        self.i_date.config(state="disabled")
        self.e_date.config(state="disabled")
        self.uses.config(state="disabled")
        self.side_effect.config(state="disabled")
        self.price.config(state="disabled")
        self.quantity.config(state="disabled")
        self.ref_add.config(state="disabled")
        self.med_name.config(state="disabled")
        self.add_btn.config(state="disabled")
        self.clear_btn.config(state="disabled")
        self.delete_btn.config(state="disabled")
        self.update_btn.config(state="disabled")
        self.addbtn.config(state="disabled")
        self.resetbtn.config(state="disabled")
        self.deletebtn.config(state="disabled")
        self.updatebtn.config(state="disabled")
        self.showbtn.config(state="disabled")
        self.searchbtn.config(state="disabled")


        # ------------------------------------ Function to enable the system when user logins  ---------------------------------------------------


   # ------------------------------------ Function to enable the system unless user logins  ---------------------------------------------------


    def enable(self):
        self.comboboxref.config(state="normal")
        self.comp.config(state="normal")
        self.comboboxtom.config(state="normal")
        self.comboboxname.config(state="normal")
        self.i_date.config(state="normal")
        self.e_date.config(state="normal")
        self.uses.config(state="normal")
        self.side_effect.config(state="normal")
        self.price.config(state="normal")
        self.quantity.config(state="normal")
        self.ref_add.config(state="normal")
        self.med_name.config(state="normal")
        self.add_btn.config(state="normal")
        self.clear_btn.config(state="normal")
        self.delete_btn.config(state="normal")
        self.update_btn.config(state="normal")
        self.addbtn.config(state="normal")
        self.resetbtn.config(state="normal")
        self.deletebtn.config(state="normal")
        self.updatebtn.config(state="normal")
        self.showbtn.config(state="normal")
        self.searchbtn.config(state="normal")


    # ------------------------------------ Creating the class object to execute the system  ---------------------------------------------------


a = PharmacyManagementSystem()
a.main()
a.disable()
root.mainloop() 