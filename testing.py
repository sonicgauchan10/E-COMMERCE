import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()

# Function to validate login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Success", "Login successful!")
        # Proceed to the main application (you can replace this with your main app logic)
        root.destroy()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Function to toggle password visibility
def toggle_password():
    if entry_password.cget('show') == '*':
        entry_password.config(show='')
        btn_show_hide.config(text="Hide Password")
    else:
        entry_password.config(show='*')
        btn_show_hide.config(text="Show Password")

# Function to open registration page
def open_registration():
    registration_window = tk.Toplevel(root)
    registration_window.title("Register")
    registration_window.geometry("300x200")

    tk.Label(registration_window, text="Username:").pack(pady=5)
    entry_new_username = tk.Entry(registration_window)
    entry_new_username.pack(pady=5)

    tk.Label(registration_window, text="Password:").pack(pady=5)
    entry_new_password = tk.Entry(registration_window, show="*")
    entry_new_password.pack(pady=5)

    def register_user():
        new_username = entry_new_username.get()
        new_password = entry_new_password.get()

        if not new_username or not new_password:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            registration_window.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

    tk.Button(registration_window, text="Register", command=register_user).pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")

# Username Label and Entry
tk.Label(root, text="Username:").place(x=50, y=50)
entry_username = tk.Entry(root)
entry_username.place(x=150, y=50)

# Password Label and Entry
tk.Label(root, text="Password:").place(x=50, y=100)
entry_password = tk.Entry(root, show="*")
entry_password.place(x=150, y=100)

# Show/Hide Password Button
btn_show_hide = tk.Button(root, text="Show Password", command=toggle_password)
btn_show_hide.place(x=150, y=130)

# Login Button
btn_login = tk.Button(root, text="Login", command=validate_login)
btn_login.place(x=150, y=170)

# Registration Link
tk.Label(root, text="Don't have an account?").place(x=50, y=220)
btn_register = tk.Button(root, text="Register", command=open_registration)
btn_register.place(x=200, y=215)

# Run the application
root.mainloop()

# Close the database connection when the app is closed
conn.close()