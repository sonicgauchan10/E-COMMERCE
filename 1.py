from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as font
import runpy

# Global variable to keep track of the current detail window
current_detail_window = None

# Function to open a new window with detailed description
def open_details_window(item_name, description, price, features):
    global current_detail_window

    # Close the previous detail window if it exists
    if current_detail_window is not None:
        current_detail_window.destroy()

    # Create a new detail window
    current_detail_window = Toplevel(account)
    current_detail_window.title(item_name)
    current_detail_window.geometry("400x300")
    current_detail_window.configure(bg="white")

    # Title
    title_label = Label(current_detail_window, text=item_name, font=("Microsoft Yahei UI Light", 18, "bold"), bg="white")
    title_label.pack(pady=10)

    # Description
    desc_label = Label(current_detail_window, text=description, font=("Microsoft Yahei UI Light", 12), bg="white", wraplength=350)
    desc_label.pack(pady=5)

    # Price
    price_label = Label(current_detail_window, text=f"Price: {price}", font=("Microsoft Yahei UI Light", 14, "bold"), bg="white")
    price_label.pack(pady=5)

    # Features
    features_label = Label(current_detail_window, text="Features:", font=("Microsoft Yahei UI Light", 14, "bold"), bg="white")
    features_label.pack(pady=5)

    for feature in features:
        feature_label = Label(current_detail_window, text=f"- {feature}", font=("Microsoft Yahei UI Light", 12), bg="white")
        feature_label.pack()

    # Close button
    close_button = Button(current_detail_window, text="Close", font=("Microsoft Yahei UI Light", 12), bg="#57a1f8", fg="white", command=current_detail_window.destroy)
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

# Function to handle the "Previous" button click
def previous_page():
    account.destroy()  # Close the current window
    runpy.run_path("Testing1.py")  # Run the Testing1.py file

# Function to handle the "Next" button click
def next_page():
    account.destroy()  # Close the current window
    runpy.run_path("Testing1.py")  # Run the Testing1.py file

# Function to perform search
def perform_search():
    search_query = search_entry.get().strip().lower()  # Get the search query and convert to lowercase
    if not search_query:
        messagebox.showinfo("Search", "Please enter a search term.")
        return

    # Clear the current product display
    for widget in recommended_frame.winfo_children():
        widget.destroy()
    for widget in top_rated_frame.winfo_children():
        widget.destroy()
    for widget in latest_frame.winfo_children():
        widget.destroy()

    # Filter products based on the search query
    matching_products = [product for product in all_products if search_query in product["name"].lower()]

    if not matching_products:
        messagebox.showinfo("Search", "No matching products found.")
        return

    # Display matching products in the Recommended section
    recommended_label = Label(recommended_frame, text="Search Results", bg="white", font=("Microsoft Yahei UI Light", 16, "bold"))
    recommended_label.pack(anchor="w", pady=10)

    for product in matching_products:
        create_product_card(
            recommended_frame,
            product["image_path"],
            product["name"],
            product["price"],
            product["discount"],
            product["rating"],
            product["description"],
            product["features"]
        )

# List of all products
all_products = [
    {
        "image_path": "item3.png",
        "name": "Washing Machine",
        "price": "Rs. 475",
        "discount": "53% off",
        "rating": "★★★★★ (26)",
        "description": "This is a high-quality laundry capsule for washing machines.",
        "features": ["30 capsules per pack", "Suitable for all washing machines", "Long-lasting freshness"]
    },
    {
        "image_path": "item2.png",
        "name": "Smartphone",
        "price": "Rs. 699",
        "discount": "20% off",
        "rating": "★★★★☆ (15)",
        "description": "This is a high-end smartphone with advanced features.",
        "features": ["6.5-inch OLED Display", "128GB Storage", "48MP Triple Camera"]
    },
    {
        "image_path": "item.png",
        "name": "Laptop",
        "price": "Rs. 999",
        "discount": "40% off",
        "rating": "★★★★★ (30)",
        "description": "This laptop features a high-performance processor and a sleek design.",
        "features": ["Intel Core i7", "16GB RAM", "512GB SSD"]
    },
    {
        "image_path": "item.png",
        "name": "Refrigerator",
        "price": "Rs. 899",
        "discount": "35% off",
        "rating": "★★★★☆ (22)",
        "description": "This refrigerator offers ample storage and energy efficiency.",
        "features": ["20 Cu. Ft. Capacity", "Energy Star Certified", "Frost-Free"]
    },
    {
        "image_path": "item.png",
        "name": "Headphones",
        "price": "Rs. 199",
        "discount": "30% off",
        "rating": "★★★★★ (26)",
        "description": "These are noise-cancelling headphones with 20-hour battery life.",
        "features": ["Noise-Cancelling", "20-Hour Battery Life", "Bluetooth 5.0"]
    },
    {
        "image_path": "item.png",
        "name": "Smartwatch",
        "price": "Rs. 299",
        "discount": "25% off",
        "rating": "★★★★☆ (18)",
        "description": "This smartwatch features a heart rate monitor and GPS.",
        "features": ["Heart Rate Monitor", "GPS Tracking", "7-Day Battery Life"]
    },
    {
        "image_path": "item.png",
        "name": "Bluetooth Speaker",
        "price": "Rs. 149",
        "discount": "25% off",
        "rating": "★★★★★ (28)",
        "description": "This Bluetooth speaker delivers high-quality sound with deep bass.",
        "features": ["20W Output", "IPX7 Waterproof", "12-Hour Battery Life"]
    },
    {
        "image_path": "item.png",
        "name": "Gaming Console",
        "price": "Rs. 599",
        "discount": "30% off",
        "rating": "★★★★☆ (25)",
        "description": "This gaming console offers immersive gaming experiences.",
        "features": ["4K Gaming", "1TB Storage", "VR Ready"]
    },
    {
        "image_path": "item.png",
        "name": "Tablet",
        "price": "Rs. 499",
        "discount": "15% off",
        "rating": "★★★★☆ (12)",
        "description": "This tablet has a 10-inch display and supports 4G LTE.",
        "features": ["10-inch Display", "64GB Storage", "4G LTE Support"]
    },
    {
        "image_path": "item.png",
        "name": "Camera",
        "price": "Rs. 799",
        "discount": "10% off",
        "rating": "★★★★★ (20)",
        "description": "This camera features a 24MP sensor and 4K video recording.",
        "features": ["24MP Sensor", "4K Video Recording", "Wi-Fi Connectivity"]
    },
    {
        "image_path": "item.png",
        "name": "Drone",
        "price": "Rs. 399",
        "discount": "20% off",
        "rating": "★★★★☆ (18)",
        "description": "This drone features a 4K camera and stable flight controls.",
        "features": ["4K Camera", "GPS Navigation", "25-Minute Flight Time"]
    },
    {
        "image_path": "item.png",
        "name": "Fitness Tracker",
        "price": "Rs. 249",
        "discount": "15% off",
        "rating": "★★★★★ (21)",
        "description": "This fitness tracker monitors your health and activity levels.",
        "features": ["Heart Rate Monitor", "Sleep Tracking", "Water Resistant"]
    }
]

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

# SEARCH BAR
search_frame = Frame(account, bg="white")
search_frame.place(x=280, y=100)

search_label = Label(search_frame, text="Search:", bg="white", font=("Microsoft Yahei UI Light", 14))
search_label.grid(row=0, column=0, padx=5, pady=5)

search_entry = Entry(search_frame, fg="black", border=1, bg="white", font=("Microsoft Yahei UI Light", 14), width=30)
search_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = Button(search_frame, text="Search", bg="#57a1f8", fg="white", font=("Microsoft Yahei UI Light", 12), command=perform_search)
search_button.grid(row=0, column=2, padx=0, pady=0)

# SECTION: RECOMMENDED
recommended_frame = Frame(account, bg="white")
recommended_frame.place(x=280, y=150)

recommended_label = Label(recommended_frame, text="Recommended", bg="white", font=("Microsoft Yahei UI Light", 16, "bold"))
recommended_label.pack(anchor="w", pady=10)

# Add product cards to Recommended section
for product in all_products[:4]:  # Display first 4 products in Recommended section
    create_product_card(
        recommended_frame,
        product["image_path"],
        product["name"],
        product["price"],
        product["discount"],
        product["rating"],
        product["description"],
        product["features"]
    )

# SECTION: TOP RATED
top_rated_frame = Frame(account, bg="white")
top_rated_frame.place(x=660, y=150)  # Adjusted y position to avoid overlap

top_rated_label = Label(top_rated_frame, text="Top Rated", bg="white", font=("Microsoft Yahei UI Light", 16, "bold"))
top_rated_label.pack(anchor="w", pady=10)

# Add product cards to Top Rated section
for product in all_products[4:8]:  # Display next 4 products in Top Rated section
    create_product_card(
        top_rated_frame,
        product["image_path"],
        product["name"],
        product["price"],
        product["discount"],
        product["rating"],
        product["description"],
        product["features"]
    )

# SECTION: LATEST
latest_frame = Frame(account, bg="white")
latest_frame.place(x=1000, y=150)  # Adjusted y position to avoid overlap

latest_label = Label(latest_frame, text="Latest", bg="white", font=("Microsoft Yahei UI Light", 16, "bold"))
latest_label.pack(anchor="w", pady=10)

# Add product cards to Latest section
for product in all_products[8:]:  # Display remaining products in Latest section
    create_product_card(
        latest_frame,
        product["image_path"],
        product["name"],
        product["price"],
        product["discount"],
        product["rating"],
        product["description"],
        product["features"]
    )

# Create a frame for the navigation buttons at the bottom of the page
navigation_frame = Frame(account, bg="white")
navigation_frame.place(x=0, y=screen_height - 50, width=screen_width, height=50)

# Add "Previous" button
previous_button = Button(navigation_frame, text="Previous", bg="#57a1f8", fg="white", font=("Microsoft Yahei UI Light", 14), command=previous_page)
previous_button.pack(side=LEFT, padx=20, pady=10)

# Add "Next" button
next_button = Button(navigation_frame, text="Next", bg="#57a1f8", fg="white", font=("Microsoft Yahei UI Light", 14), command=next_page)
next_button.pack(side=RIGHT, padx=20, pady=10)

account.mainloop()