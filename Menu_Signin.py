import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess as sub
import sys
import os

# Helper to execute scripts using the correct python path and absolute paths
def run_script(script_name, args=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, script_name)
    
    if os.path.exists(script_path):
        root.destroy()
        command = [sys.executable, script_path]
        if args:
            command.append(args)
        # Using sub.call as per original logic, except for update_profile which used Popen
        
        sub.Popen(command)
       
            
    else:
        messagebox.showerror("Error", f"File not found: {script_name}")

def view_profile():
    nric = sys.argv[1]
    run_script('viewprof.py', nric)

def update_profile():
    nric = sys.argv[1]
    run_script('updateprof.py', nric)

def manage_goals():
    nric = sys.argv[1]
    run_script('goals.py', nric)

def record_data():
    nric = sys.argv[1]
    run_script('recdata.py', nric)

def view_progress():
    nric = sys.argv[1]
    run_script('progress.py', nric)

def healthy_living():
    nric = sys.argv[1]
    run_script('healthliv.py', nric)

def logout():
    run_script('signin.py')

root = tk.Tk()
root.title('Healthify - Menu')
root.attributes('-fullscreen', True)

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

#to ensure background is found via absolute path
script_dir = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(script_dir, 'background.jpg')

image = Image.open(bg_path)
image = image.resize((window_width, window_height))
photo = ImageTk.PhotoImage(image)

tk.Label(root, image=photo).pack()

menu_frame = tk.Frame(root, bg='#FFFFFF', bd=10, relief=tk.RIDGE)
menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=800, height=700)

title_label = tk.Label(menu_frame, text='Healthify - Menu',
                       font=('Times New Roman', 24, 'bold'), fg='#333333',
                       bg='#FFFFFF')
title_label.pack(pady=20)

options_font = ('Arial', 18)

view_profile_button = tk.Button(menu_frame, text='1) View Your Current Profile',
                                command=view_profile,
                                font=options_font, bg='#4CAF50', fg='#000000',
                                width=30)
view_profile_button.pack(fill=tk.X, padx=20, pady=10)

update_profile_button = tk.Button(menu_frame, text='2) Update Your Profile',
                                  command=update_profile,
                                  font=options_font, bg='#4CAF50', fg='#000000',
                                  width=30)
update_profile_button.pack(fill=tk.X, padx=20, pady=10)

manage_goals_button = tk.Button(menu_frame, text='3) Manage Daily Goals',
                                command=manage_goals,
                                font=options_font, bg='#4CAF50', fg='#000000',
                                width=30)
manage_goals_button.pack(fill=tk.X, padx=20, pady=10)

record_data_button = tk.Button(menu_frame, text='4) Record your data',
                               command=record_data,
                               font=options_font, bg='#4CAF50', fg='#000000',
                               width=30)
record_data_button.pack(fill=tk.X, padx=20, pady=10)

view_progress_button = tk.Button(menu_frame, text='5) View Progress Analysis',
                                 command=view_progress,
                                 font=options_font, bg='#4CAF50', fg='#000000',
                                 width=30)
view_progress_button.pack(fill=tk.X, padx=20, pady=10)

healthyliving_but = tk.Button(menu_frame, text='6) Healthy Living',
                              command=healthy_living,
                              font=options_font, bg='#4CAF50', fg='#000000',
                              width=30)
healthyliving_but.pack(fill=tk.X, padx=20, pady=10)

logout_button = tk.Button(menu_frame, text='7) Log Out', command=logout,
                          font=options_font, bg='#4CAF50', fg='#000000', width=30)
logout_button.pack(fill=tk.X, padx=20, pady=10)

root.mainloop()

