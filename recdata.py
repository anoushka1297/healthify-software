import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess as sub
import sys
import sqlite3 as sq
from datetime import datetime

root = tk.Tk()
root.title("Healthify - Daily Health Checkups")
root.attributes('-fullscreen', True)
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

image = Image.open('background.jpg')
image = image.resize((window_width, window_height))
background_image = ImageTk.PhotoImage(image)

background_label = ttk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(root, text="Daily Health Checkups", font=("Helvetica", 20, "bold"), bg="#f0f7fa", fg="#00796b")
title_label.pack(pady=20)

# Get current date
current_date = datetime.today().date()

# Display current date
current_date_label = tk.Label(root, text=f"You are entering records for: {current_date}", font=("Helvetica", 14), bg="#f0f7fa", fg="#004d40")
current_date_label.pack(pady=10)

instruction_label = tk.Label(root, text="Please enter your daily health data:", font=("Helvetica", 12), bg="#f0f7fa", fg="#004d40")
instruction_label.pack(pady=10)

# Frame for holding input fields
checkup_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge", padx=15, pady=15)
checkup_frame.pack(padx=10, pady=20, fill="x")

# Aesthetic separators
def add_separator(frame):
    separator = tk.Frame(frame, height=1, bd=1, relief="sunken", bg="#b2dfdb")
    separator.pack(fill="x", pady=10)

health_data = {}

def create_checkup_input(parent, label_text, unit):
    frame = tk.Frame(parent, bg="#ffffff", padx=5, pady=5)
    frame.pack(fill="x", pady=5)
    label = tk.Label(frame, text=label_text, bg="#ffffff", font=("Helvetica", 12), fg="#004d40")
    label.pack(side="left", padx=10)
    entry = tk.Entry(frame, font=("Helvetica", 12), width=10)
    entry.pack(side="left", padx=10)
    unit_label = tk.Label(frame, text=unit, bg="#ffffff", font=("Helvetica", 12), fg="#004d40")
    unit_label.pack(side="left")
    health_data[label_text] = entry

# Input fields for each health checkup
create_checkup_input(checkup_frame, "Body Temperature", "°C")
add_separator(checkup_frame)
create_checkup_input(checkup_frame, "Blood Pressure", "mmHg")
add_separator(checkup_frame)
create_checkup_input(checkup_frame, "Heart Rate", "bpm")
add_separator(checkup_frame)
create_checkup_input(checkup_frame, "Hydration Levels", "ml")
add_separator(checkup_frame)
create_checkup_input(checkup_frame, "Sleep Quality", "hours")

def submit_checkups():
    entered_data = {}
    for label, entry in health_data.items():
        value = entry.get()
        if not value:
            messagebox.showerror("Missing Data", f"Please enter data for {label}.")
            return
        entered_data[label] = value

    nric_signin = sys.argv[1] # Get NRIC from command line argument
    date = current_date # Use the current date
    connection = sq.connect('healthify.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS daily_data (nric CHAR(9),date DATE,body_temp FLOAT,blood_pressure INT,heart_rate INT,hydration_level FLOAT,sleep_quality FLOAT)")
    connection.commit()
    cursor.execute('INSERT INTO daily_data VALUES (?, ?, ?, ?, ?, ?, ?)', (nric_signin, date, entered_data["Body Temperature"], entered_data["Blood Pressure"], entered_data["Heart Rate"], entered_data["Hydration Levels"], entered_data["Sleep Quality"]))
    connection.commit()
    messagebox.showinfo("Success", "Data recorded successfully!")
    
    # Clear the input fields
    for entry in health_data.values():
        entry.delete(0, tk.END)
    cursor.close()
    connection.close()
    ''' #this part will be added later insted of above since right now it obstructs graphs
    cursor.execute("SELECT * FROM daily_data WHERE nric=? AND date=?", (nric_signin,
    date))
    if cursor.fetchone() is not None:
    messagebox.showerror("Duplicate Entry", "You have already entered data for
    today.")
    else:
    # Insert the new record
    cursor.execute('INSERT INTO daily_data (nric, date, body_temp, blood_pressure,
    heart_rate, hydration_level, sleep_quality) VALUES (?, ?, ?, ?, ?, ?, ?)',
    (nric_signin, date, entered_data["Body Temperature"],
    entered_data["Blood Pressure"], entered_data["Heart Rate"],
    entered_data["Hydration Levels"], entered_data["Sleep Quality"]))
    connection.commit()
    messagebox.showinfo("Success", "Data recorded successfully!")
    '''

def return_menu():
    nric_signin = sys.argv[1]
    root.destroy()
    sub.Popen([sys.executable, 'Menu_Signin.py', nric_signin])

submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), bg="#a5d6a7", relief="flat", command=submit_checkups)
submit_button.pack(pady=20)

menu_button = tk.Button(root, text='Go back to Menu', font=("Helvetica", 12, 'underline'), relief=tk.FLAT, cursor='hand2', fg='#0000FF', command=return_menu, bg='#FFFFFF')
menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
con = sq.connect('healthify.db')
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS daily_data (
        nric CHAR(9),
        date DATE,
        body_temp FLOAT,
        blood_pressure INT,
        heart_rate INT,
        hydration_level FLOAT,
        sleep_quality FLOAT
    )
""")
con.commit() # Save the table creation
cur.execute('select * from daily_data')
print(cur.fetchall())
con.commit()

root.mainloop()

