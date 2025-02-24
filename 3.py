from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
import tkinter.font as font
import sqlite3
import runpy

# Function to open a new window with detailed description
def open_details_window(item_name, description, price, features):
    details_window = Toplevel(account)
    details_window.title(item_name)
    details_window.geometry("400x300")
    details_window.configure(bg="white")

    # Title
    title_label = Label(details_window, text=item_name, font=("Microsoft Yahei UI Light", 18, "bold"), bg="white")
    title_label.pack(pady=10)

    # Description
    desc_label = Label(details_window, text=description, font=("Microsoft Yahei UI Light", 12), bg="white", wraplength=350)
    desc_label.pack(pady=5)

    # Price
    price_label = Label(details_window, text=f"Price: {price}", font=("Microsoft Yahei UI Light", 14, "bold"), bg="white")
    price_label.pack(pady=5)

    # Features
    features_label = Label(details_window, text="Features:", font=("Microsoft Yahei UI Light", 14, "bold"), bg="white")
    features_label.pack(pady=5)

    for feature in features:
        feature_label = Label(details_window, text=f"- {feature}", font=("Microsoft Yahei UI Light", 12), bg="white")
        feature_label.pack()

    # Close button
    close_button = Button(details_window, text="Close", font=("Microsoft Yahei UI Light", 12), bg="#57a1f8", fg="white", command=details_window.destroy)
    close_button.pack(pady=10)

# Function to create a product card
def create_product_card(parent, image_path, name, price, discount, rating, description, features):
    product_frame = Frame(parent, bg="white", bd=2, relief="solid")
    product_frame.pack(side=LEFT, padx=10, pady=10, fill="both", expand=True)

    # Load product image
    product_image = Image.open(image_path)
    product_image = product_image.resize((100, 100))
    product_image = ImageTk.PhotoImage(product_image)

    # Add product image
    image_label = Label(product_frame, image=product_image, bg="white")
    image_label.image = product_image  # Keep a reference to avoid garbage collection
    image_label.pack(pady=10)

    # Bind click event to open details window
    image_label.bind("<Button-1>", lambda event: open_details_window(name, description, price, features))

    # Add product name
    name_label = Label(product_frame, text=name, bg="white", font=("Microsoft Yahei UI Light", 12), justify="center")
    name_label.pack(pady=5)

    # Add price and discount
    price_frame = Frame(product_frame, bg="white")
    price_frame.pack(pady=5)

    price_label = Label(price_frame, text=price, bg="white", font=("Microsoft Yahei UI Light", 12, "bold"))
    price_label.pack(side=LEFT, padx=5)

    discount_label = Label(price_frame, text=discount, bg="white", font=("Microsoft Yahei UI Light", 10), fg="green")
    discount_label.pack(side=LEFT)

    # Add rating
    rating_label = Label(product_frame, text=rating, bg="white", font=("Microsoft Yahei UI Light", 10), fg="orange")
    rating_label.pack(pady=5)

    return product_frame

# Function to toggle full-screen mode
def toggle_fullscreen():
    if account.attributes("-fullscreen"):
        account.attributes("-fullscreen", False)
        restore_button.config(text="⬜")  # Change button text to indicate windowed mode
    else:
        account.attributes("-fullscreen", True)
        restore_button.config(text="❐")  # Change button text to indicate full-screen mode

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

# Making maximize, minimize, and restore buttons manually
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

# Cancel button (✕)
btn2 = Button(a, text="✕", command=max, width=4, bg="#57a1f8", border=0, font=buttonFont)
btn2.place(x=screen_width - 50, y=0)  # Place at the far right
btn2.bind('<Enter>', on_enter)
btn2.bind('<Leave>', on_leave)

# Restore button (❐)
restore_button = Button(a, text="❐", command=toggle_fullscreen, width=4, bg="#57a1f8", border=0, font=buttonFont)
restore_button.place(x=screen_width - 100, y=0)  # Place between minimize and cancel buttons

# Minimize button (-)
btn = Button(a, text="-", command=min, width=4, bg="#57a1f8", border=0, font=buttonFont)
btn.place(x=screen_width - 150, y=0)  # Place to the left of the restore button

def enter(i):
    btn['background'] = "red"

def leave(i):
    btn['background'] = "#57a1f8"

btn.bind('<Enter>', enter)
btn.bind('<Leave>', leave)

# CREATING A OPTION BAR AT LEFT OF SCREEN
options_frame = Frame(height=screen_height - 35, width=250, bg='#fcf0d7').place(x=0, y=35)

# SEARCH BAR
search_frame = Frame(account, bg="white")
search_frame.place(x=280, y=100)

search_label = Label(search_frame, text="Search:", bg="white", font=("Microsoft Yahei UI Light", 14))
search_label.grid(row=0, column=0, padx=5, pady=5)

search_entry = Entry(search_frame, fg="black", border=1, bg="white", font=("Microsoft Yahei UI Light", 14), width=30)
search_entry.grid(row=0, column=1, padx=5, pady=5)

def perform_search():
    search_query = search_entry.get()
    # Add your search logic here
    print(f"Searching for: {search_query}")
    messagebox.showinfo("Search", f"Searching for: {search_query}")

search_button = Button(search_frame, text="Search", bg="#57a1f8", fg="white", font=("Microsoft Yahei UI Light", 12), command=perform_search)
search_button.grid(row=0, column=2, padx=0, pady=0)

# SECTION: RECOMMENDED
recommended_frame = Frame(account, bg="white")
recommended_frame.place(x=280, y=150)

recommended_label = Label(recommended_frame, text="Recommended", bg="white", font=("Microsoft Yahei UI Light", 16, "bold"))
recommended_label.pack(anchor="w", pady=10)

# Add product cards to Recommended section
product1 = create_product_card(
    recommended_frame,
    "item3.png",  # Replace with actual image path
    " Washing Machine",
    "Rs. 475",
    "53% off",
    "★★★★★ (26)",
    "This is a high-quality laundry capsule for washing machines.",
    ["30 capsules per pack", "Suitable for all washing machines", "Long-lasting freshness"]
)

product2 = create_product_card(
    recommended_frame,
    "item2.png",  # Replace with actual image path
    "Smartphone",
    "Rs. 699",
    "20% off",
    "★★★★☆ (15)",
    "This is a high-end smartphone with advanced features.",
    ["6.5-inch OLED Display", "128GB Storage", "48MP Triple Camera"]
)

# SECTION: TOP RATED
top_rated_frame = Frame(account, bg="white")
top_rated_frame.place(x=660, y=150)  # Adjusted y position to avoid overlap

top_rated_label = Label(top_rated_frame, text="Top Rated", bg="white", font=("Microsoft Yahei UI Light", 16, "bold"))
top_rated_label.pack(anchor="w", pady=10)

# Add product cards to Top Rated section
product3 = create_product_card(
    top_rated_frame,
    "item.png",  # Replace with actual image path
    "Headphones",
    "Rs. 199",
    "30% off",
    "★★★★★ (26)",
    "These are noise-cancelling headphones with 20-hour battery life.",
    ["Noise-Cancelling", "20-Hour Battery Life", "Bluetooth 5.0"]
)

product4 = create_product_card(
    top_rated_frame,
    "item.png",  # Replace with actual image path
    "Smartwatch",
    "Rs. 299",
    "25% off",
    "★★★★☆ (18)",
    "This smartwatch features a heart rate monitor and GPS.",
    ["Heart Rate Monitor", "GPS Tracking", "7-Day Battery Life"]
)

# SECTION: LATEST
latest_frame = Frame(account, bg="white")
latest_frame.place(x=1000, y=150)  # Adjusted y position to avoid overlap

latest_label = Label(latest_frame, text="Latest", bg="white", font=("Microsoft Yahei UI Light", 16, "bold"))
latest_label.pack(anchor="w", pady=10)

# Add product cards to Latest section
product5 = create_product_card(
    latest_frame,
    "item.png",  # Replace with actual image path
    "Tablet",
    "Rs. 499",
    "15% off",
    "★★★★☆ (12)",
    "This tablet has a 10-inch display and supports 4G LTE.",
    ["10-inch Display", "64GB Storage", "4G LTE Support"]
)

product6 = create_product_card(
    latest_frame,
    "item2.png",  # Replace with actual image path
    "Camera",
    "Rs. 799",
    "10% off",
    "★★★★★ (20)",
    "This camera features a 24MP sensor and 4K video recording.",
    ["24MP Sensor", "4K Video Recording", "Wi-Fi Connectivity"]
)

account.mainloop()