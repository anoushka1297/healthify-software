import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess as sub
import sys
import sqlite3 as sq
import matplotlib.pyplot as plt
import os

#initialise to avoid error potentially 

def init_db():
    connection = sq.connect('healthify.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_data 
                      (nric CHAR(9), date DATE, body_temp FLOAT, blood_pressure INT, 
                       heart_rate INT, hydration_level FLOAT, sleep_quality FLOAT)''')
    connection.commit()
    connection.close()

init_db()

def plot_graph(value_type):
    nric = sys.argv[1]
    connection = sq.connect('healthify.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM daily_data WHERE nric=? ORDER BY date ASC', (nric,))
    data = cursor.fetchall()
    if not data:
        messagebox.showwarning("No Data", "No records found for the selected type.")
        return
    days=[f'Day {i + 1}' for i in range(len(data))]
    values=[]
    for rec in data:
        if value_type=="Temperature":
            values.append(rec[2])
        elif value_type=="Blood Pressure":
            values.append(rec[3])
        elif value_type=="Heart Rate":
            values.append(rec[4])
        elif value_type=="Hydration Level":
            values.append(rec[5])
        elif value_type=="Sleep Hours":
            values.append(rec[6])
    plt.figure(figsize=(10, 5))
    plt.plot(days, values, marker='x')
    plt.title(f'{value_type} over {len(days)} days')
    plt.xlabel('Days')
    plt.ylabel(value_type)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def return_menu():
    nric_signin = sys.argv[1]
    root.destroy()
    # Path handling and Popen for virtual environment compatibility
    script_dir = os.path.dirname(os.path.abspath(__file__))
    menu_path = os.path.join(script_dir, 'Menu_Signin.py')
    sub.Popen([sys.executable, menu_path, nric_signin])

root = tk.Tk()
root.title("Healthify - Daily Health Checkups")
root.attributes('-fullscreen', True)
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

image = Image.open('background.jpg')
image = image.resize((window_width, window_height))
background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(root, text="Healthify - View Health Data", font=("Helvetica", 20, "bold"), bg="#f0f7fa", fg="#00796b")
title_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#f0f7fa")
button_frame.pack(pady=20)

button_types = ["Temperature", "Blood Pressure", "Heart Rate", "Hydration Level", "Sleep Hours"]

for value_type in button_types:
    button = tk.Button(button_frame, text=value_type, font=("Helvetica", 14), command=lambda vt=value_type: plot_graph(vt))
    button.pack(side="left", padx=10)

menu_button = tk.Button(root, text='Go back to Menu', font=("Helvetica", 12), relief=tk.FLAT, cursor='hand2', fg='#0000FF', command=return_menu, bg='#FFFFFF')
menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

root.mainloop()

