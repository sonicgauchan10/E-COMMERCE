from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from datetime import datetime

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '@Rischal17',
    'database': 'pharmacy'
}

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x900")
        self.root.config(bg='crimson')
        self.root.title("Pharmacy Management System")
        self.root.resizable(height=False, width=False)

        # Initialize frames and widgets
        self.frames()
        self.med_info()
        self.addmed()
        self.addmed_button()
        self.options()
        self.sideframe_edit()
        self.downframe_edit()
        self.fetch_med_info()

        # Disable system until login
        self.disable()

    # ------------------------------------ Database Connection ------------------------------------
    def get_db_connection(self):
        """Create and return a database connection."""
        try:
            return mysql.connector.connect(**DB_CONFIG)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to database: {err}")
            return None

    # ------------------------------------ Frames ------------------------------------
    def frames(self):
        """Create and organize frames for the application."""
        # Main Page
        self.phar = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", font=("Segoe UI", 50, 'bold'),
                          bg='crimson', fg='white', relief='raised', bd=10, width=100)
        self.phar.pack()

        # Medicine Details Frame
        self.med = Frame(self.root, height=400, width=1500, bd=10, relief='raised', bg='crimson')
        self.med.place(x=0, y=110)

        # Options Frame (Buttons)
        self.opt = Frame(self.root, height=100, width=1500, bd=10, relief='raised', bg='crimson')
        self.opt.place(x=0, y=510)

        # Show Details Frame
        self.show = Frame(self.root, height=290, width=1500, bd=10, relief='raised', bg='crimson')
        self.show.place(x=0, y=610)

        # Medicine Information Frame
        self.med_frame = Frame(self.med, height=360, width=900, bd=5, relief='raised', bg='crimson')
        self.med_frame.place(x=10, y=10)

        # Add Medicine Frame
        self.med_add = Frame(self.med, height=360, width=550, bd=5, relief='raised', bg='crimson')
        self.med_add.place(x=920, y=10)

        # Side Frame (for reference numbers and medicine names)
        self.side_frame = Frame(self.med_add)
        self.side_frame.place(x=20, y=110, height=150, width=500)

        # Down Frame (for detailed medicine information)
        self.down_frame = Frame(self.show)
        self.down_frame.place(x=15, y=10, height=250, width=1450)

    # ------------------------------------ Medicine Information ------------------------------------
    def med_info(self):
        """Create labels and entry fields for medicine information."""
        labels = [
            ("Reference Number", 30, 30), ("Company Name", 30, 80),
            ("Type Of Medicine", 30, 130), ("Medicine Name", 30, 180),
            ("Issue Date", 30, 230), ("Exp Date", 30, 280),
            ("Uses", 490, 30), ("Side Effects", 490, 80),
            ("Price", 490, 130), ("Quantity", 490, 180)
        ]

        for text, x, y in labels:
            Label(self.med_frame, text=text, font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white').place(x=x, y=y)

        # Combobox for Reference Number
        self.comboboxref = ttk.Combobox(self.med_frame, state="readonly", font=("Segoe UI", 12, 'bold'))
        self.comboboxref.place(x=250, y=30, width=205, height=30)

        # Entry fields
        self.comp = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.comp.place(x=250, y=80)

        self.comboboxtom = ttk.Combobox(self.med_frame, state="readonly", font=("Segoe UI", 12, 'bold'),
                                        values=["Tablet", "Drops", "Injection"])
        self.comboboxtom.current(0)
        self.comboboxtom.place(x=250, y=130, width=205, height=30)

        self.comboboxname = ttk.Combobox(self.med_frame, state="readonly", font=("Segoe UI", 12, 'bold'))
        self.comboboxname.place(x=250, y=180, width=205, height=30)

        self.i_date = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.i_date.place(x=250, y=230)

        self.e_date = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.e_date.place(x=250, y=280)

        self.uses = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.uses.place(x=650, y=30)

        self.side_effect = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.side_effect.place(x=650, y=80)

        self.price = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.price.place(x=650, y=130)

        self.quantity = Entry(self.med_frame, font=("Segoe UI", 13, 'bold'))
        self.quantity.place(x=650, y=180)

    # ------------------------------------ Add Medicine ------------------------------------
    def addmed(self):
        """Create labels and entry fields for adding new medicine."""
        Label(self.med_add, text="Reference Number", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white').place(x=20, y=20)
        Label(self.med_add, text="Medicine Name", font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white').place(x=20, y=60)

        self.ref_add = Entry(self.med_add, font=("Segoe UI", 13, 'bold'))
        self.ref_add.place(x=250, y=20)

        self.med_name = Entry(self.med_add, font=("Segoe UI", 13, 'bold'))
        self.med_name.place(x=250, y=60)

    # ------------------------------------ Buttons ------------------------------------
    def addmed_button(self):
        """Create buttons for adding, updating, deleting, and clearing medicine records."""
        buttons = [
            ("Add", self.med_btn_add, 15, 290),
            ("Update", self.med_btn_update, 145, 290),
            ("Delete", self.med_btn_delete, 275, 290),
            ("Clear", self.med_btn_clear, 405, 290)
        ]

        for text, command, x, y in buttons:
            Button(self.med_add, text=text, font=("Segoe UI", 13, 'bold'), bg='crimson', fg='white',
                   activebackground='green', activeforeground='white', bd=5, command=command).place(x=x, y=y, width=120)

    # ------------------------------------ Main Execution ------------------------------------
if __name__ == "__main__":
    root = Tk()
    app = PharmacyManagementSystem(root)
    root.mainloop()