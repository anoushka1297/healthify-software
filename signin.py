import tkinter as tk
from tkinter import messagebox
import csv
from PIL import Image, ImageTk
import subprocess as sub
import os
import sys  

def signin_user():
    nric = entry_nric.get()
    password = entry_password.get()

    if not (nric and password):
        messagebox.showerror('Error', 'Please fill all fields.')
        return

    with open('AccountDetails.csv', 'r') as file:
        reader = csv.reader(file)
        found = False

        for row in reader:
            if row and row[0] == nric and row[6] == password:
                found = True
                break

    if found:
      messagebox.showinfo('Success', 'Sign-in successful!')
      script_dir = os.path.dirname(os.path.abspath(__file__))
      Menu_Signin_path = os.path.join(script_dir, 'Menu_Signin.py')
      if os.path.exists(Menu_Signin_path):
          root.destroy()
          #Using sys. executable to find the correct 'python' or 'python3'
          sub.Popen([sys.executable, Menu_Signin_path, nric])
          

    else:
        messagebox.showerror(
            'Error',
            'Invalid NRIC and/or password combination.'
        )


def home_page():
	script_dir = os.path.dirname(os.path.abspath(__file__))
	Account_Create_path = os.path.join(script_dir, 'Account_Create.py')
	if os.path.exists(Account_Create_path):
	  root.destroy ()
	  #Using sys. executable to find the correct 'python' or 'python3'
	  sub.Popen([sys.executable, Account_Create_path])
    
    


root = tk.Tk()

root.title('Sign In')

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

root.geometry(f'{window_width}x{window_height}')

image = Image.open('background.jpg')
image = image.resize((window_width, window_height))

photo = ImageTk.PhotoImage(image)

tk.Label(root, image=photo).pack()

form_frame = tk.Frame(root, bg='#FFFFFF', bd=10, relief=tk.RIDGE)

form_frame.place(
    relx=0.5,
    rely=0.5,
    anchor=tk.CENTER
)

title_label = tk.Label(
    form_frame,
    text='WELCOME TO HEALTHIFY - SIGN IN',
    font=('Times New Roman', 20, 'bold'),
    fg='#333333',
    bg='#FFFFFF',
    wraplength=500
)

title_label.pack(pady=10)

label_font = ('Arial', 14)

tk.Label(
    form_frame,
    text='Enter your username:',
    font=label_font,
    fg='#333333',
    bg='#FFFFFF'
).pack(anchor='w', padx=10, pady=5)

entry_nric = tk.Entry(form_frame, width=30)
entry_nric.pack(anchor='w', padx=10, pady=5)

tk.Label(
    form_frame,
    text='Enter your Password:',
    font=label_font,
    fg='#333333',
    bg='#FFFFFF'
).pack(anchor='w', padx=10, pady=5)

entry_password = tk.Entry(form_frame, width=30, show='*')
entry_password.pack(anchor='w', padx=10, pady=5)

signin_button = tk.Button(
    form_frame,
    text='Sign In',
    command=signin_user,
    font=('Arial', 14, 'bold'),
    bg='#4CAF50',
    fg='#000000'
)

signin_button.pack(pady=20)

create_account_button = tk.Button(
    form_frame,
    text='Create New Account',
    command=home_page,
    font=('Arial', 12, 'underline'),
    fg='#0000FF',
    bg='#FFFFFF',
    relief=tk.FLAT,
    cursor="hand2"
)

create_account_button.pack(pady=10)

root.mainloop()
