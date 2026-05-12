import tkinter as tk
from PIL import Image, ImageTk
import csv
import sys
import subprocess as sub
import os

# Function to calculate BMI
def calculate_bmi(weight, height):
    if height > 0:
        bmi = weight / (height/100)**2
        return round(bmi, 2)
    else:
        return 0

def account_details():
    if len(sys.argv) > 1:
        nric_signin = sys.argv[1]
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, 'AccountDetails.csv')
        
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == nric_signin:
                    return row

def return_menu():
    nric_signin = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    menu_path = os.path.join(script_dir, 'Menu_Signin.py')
    
    if os.path.exists(menu_path):
        root.destroy()
        # Using sys.executable for virtual environment compatibility
        sub.Popen([sys.executable, menu_path, nric_signin])

row = account_details()
name, dob, gender, height, weight = row[1], row[2], row[3], row[4], row[5]
bmi = calculate_bmi(float(weight), float(height))

# Create the main window
root = tk.Tk()
root.title("View Profile")
root.withdraw()

root.update_idletasks()

root.attributes('-fullscreen', True)

root.deiconify()
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

# Ensure background image is found via absolute path
script_dir = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(script_dir, 'background.jpg')

image = Image.open(bg_path)
image = image.resize((window_width, window_height))
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold the profile information
profile_frame = tk.Frame(root, bg='#FFFFFF', bd=2, relief='groove')
profile_frame.place(anchor=tk.CENTER, relx=0.5, rely=0.4)

# Labels and data for user profile
tk.Label(profile_frame, text="User Profile", font=("Helvetica", 24, 'bold'),
         fg='#333333', bg='#FFFFFF').grid(row=0, columnspan=2, pady=(30, 10))

tk.Label(profile_frame, text="Name:", font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=1, column=0, sticky="w", padx=20, pady=10)
tk.Label(profile_frame, text=name, font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=1, column=1, sticky="w", padx=20, pady=10)

tk.Label(profile_frame, text="DOB:", font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=2, column=0, sticky="w", padx=20, pady=10)
tk.Label(profile_frame, text=dob, font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=2, column=1, sticky="w", padx=20, pady=10)

tk.Label(profile_frame, text="Gender:", font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=3, column=0, sticky="w", padx=20, pady=10)
tk.Label(profile_frame, text=gender, font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=3, column=1, sticky="w", padx=20, pady=10)

tk.Label(profile_frame, text="Height (cm):", font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=4, column=0, sticky="w", padx=20, pady=10)
tk.Label(profile_frame, text=height, font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=4, column=1, sticky="w", padx=20, pady=10)

tk.Label(profile_frame, text="Weight (kg):", font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=5, column=0, sticky="w", padx=20, pady=10)
tk.Label(profile_frame, text=weight, font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=5, column=1, sticky="w", padx=20, pady=10)

tk.Label(profile_frame, text="BMI:", font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=6, column=0, sticky="w", padx=20, pady=10)
tk.Label(profile_frame, text=bmi, font=("Arial", 16), fg='#333333',
         bg='#FFFFFF').grid(row=6, column=1, sticky="w", padx=20, pady=10)

bmi_color = '#00FF00'  # green default
color, remark = 'GREEN', 'Healthy'

if bmi >= 40:
    bmi_color, color, remark = '#800080', 'PURPLE', 'Extreme obesity'
elif bmi >= 30:
    bmi_color, color, remark = '#FF0000', 'RED', 'Obesity'
elif bmi > 25:
    bmi_color, color, remark = '#FFFF00', 'YELLOW', 'Overweight'
elif bmi < 18.5:
    bmi_color, color, remark = '#ADD8E6', 'LIGHT BLUE', 'Underweight'

# Frame for BMI indicator
bmi_indicator_frame = tk.Frame(root, bg='#FFFFFF', bd=2, relief='groove')
bmi_indicator_frame.place(anchor=tk.CENTER, relx=0.5, rely=0.7)

tk.Label(bmi_indicator_frame, text="BMI Indicator", font=("Arial", 16, 'bold'),
         fg='#000000', bg='#FFFFFF').pack(pady=5)

# Create colored bar for BMI status
bmi_status_label = tk.Label(bmi_indicator_frame, text=color, font=("Arial", 14),
                            fg='#000000', bg=bmi_color)
bmi_status_label.pack(pady=5, padx=20)

remark_label = tk.Label(bmi_indicator_frame, text=remark, font=("Arial", 14),
                        fg='#000000', bg='#FFFFFF')
remark_label.pack(pady=5, padx=20)

# Head back to Menu_Signin.py
Menu = tk.Button(root, text='Go back to Menu', font=("Helvetica", 12, 'underline'),
                 relief=tk.FLAT, cursor='hand2',
                 fg='#0000FF', command=return_menu, bg='#FFFFFF')
Menu.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()

