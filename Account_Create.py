import tkinter as tk
from tkinter import messagebox
import csv
from PIL import Image, ImageTk
from datetime import datetime
import subprocess as sub
import sys
import os 

# func
def saveuser():
    NRIC = entry_NRIC.get()
    name = entry_name.get()
    dob_str = entry_dob.get()
    gender = gender_var.get()
    height = entry_height.get()
    weight = entry_weight.get()
    pw = entry_pw.get()

    if not (NRIC and name and gender and height and weight and pw):
        messagebox.showerror('Error', 'Please fill all fields.')
        return

    try:
        dob = datetime.strptime(dob_str, '%d-%m-%Y').date()

    except ValueError:
        messagebox.showerror(
            'Error',
            'Invalid date format. Please enter date in DD-MM-YYYY format.'
        )
        return

    # save to csv
    try:
        with open('AccountDetails.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

            if rows:
                for entry in rows:

                    # Skip empty rows
                    if not entry:
                        continue

                    if entry[0].lower() == NRIC.lower():
                        messagebox.showerror(
                            'Error',
                            'Account for this NRIC already exists.'
                        )
                        break

                else:
                    with open('AccountDetails.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([
                            NRIC,
                            name,
                            dob_str,
                            gender,
                            height,
                            weight,
                            pw
                        ])

                    entry_NRIC.delete(0, tk.END)
                    entry_name.delete(0, tk.END)
                    entry_dob.delete(0, tk.END)
                    gender_var.set(None)
                    entry_height.delete(0, tk.END)
                    entry_weight.delete(0, tk.END)
                    entry_pw.delete(0, tk.END)

                    messagebox.showinfo(
                        'Success',
                        'Your account has been created'
                    )

            else:
                with open('AccountDetails.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        NRIC,
                        name,
                        dob_str,
                        gender,
                        height,
                        weight,
                        pw
                    ])

                entry_NRIC.delete(0, tk.END)
                entry_name.delete(0, tk.END)
                entry_dob.delete(0, tk.END)
                gender_var.set(None)
                entry_height.delete(0, tk.END)
                entry_weight.delete(0, tk.END)
                entry_pw.delete(0, tk.END)

                messagebox.showinfo(
                    'Success',
                    'Your account has been created'
                )

    except FileNotFoundError:
        with open('AccountDetails.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                NRIC,
                name,
                dob_str,
                gender,
                height,
                weight,
                pw
            ])

        entry_NRIC.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_dob.delete(0, tk.END)
        gender_var.set(None)
        entry_height.delete(0, tk.END)
        entry_weight.delete(0, tk.END)
        entry_pw.delete(0, tk.END)

        messagebox.showinfo(
            'Success',
            'Your account has been created'
        )


def open_signin():
	script_dir = os.path.dirname(os.path.abspath(__file__))
	signin_path = os.path.join(script_dir, 'signin.py')
	if os.path.exists(signin_path):
	    root.destroy()
       	    #Using sys.executable to find the correct 'python' or 'python3'
	    sub.Popen([sys.executable, signin_path])
   


# MAIN
root = tk.Tk()

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

root.geometry(f"{window_width}x{window_height}")

root.title('HEALTHIFY- Create your account now!')
root.configure(bg='#90EE90')

image = Image.open('background.jpg')
image = image.resize((window_width, window_height))

photo = ImageTk.PhotoImage(image)

tk.Label(root, image=photo).grid(row=1, column=1)

form_frame = tk.Frame(
    root,
    bg='#FFFFFF',
    bd=10,
    relief=tk.RIDGE
)

form_frame.place(
    relx=0.5,
    rely=0.5,
    anchor=tk.CENTER,
    width=700,
    height=900
)

title_label = tk.Label(
    form_frame,
    text='WELCOME TO HEALTHIFY - YOUR WELLNESS COMPANION',
    font=('Times New Roman', 20, 'bold'),
    fg='#333333',
    bg='#FFFFFF',
    wraplength=500
)

title_label.pack(pady=10)

label_font = ('Arial', 14)

tk.Label(
    form_frame,
    text='Enter your username :',
    font=label_font,
    fg='#333333',
    bg='#FFFFFF'
).pack(anchor='w', padx=10, pady=5)

entry_NRIC = tk.Entry(form_frame, width=30)
entry_NRIC.pack(anchor='w', padx=10, pady=5)

tk.Label(
    form_frame,
    text='Enter your full name:',
    font=label_font,
    fg='#333333',
    bg='#FFFFFF'
).pack(anchor='w', padx=10, pady=5)

entry_name = tk.Entry(form_frame, width=30)
entry_name.pack(anchor='w', padx=10, pady=5)

tk.Label(
    form_frame,
    text='Enter your date of birth (DD-MM-YYYY):',
    font=label_font,
    fg='#333333',
    bg='#FFFFFF'
).pack(anchor='w', padx=10, pady=5)

entry_dob = tk.Entry(form_frame, width=30)
entry_dob.pack(anchor='w', padx=10, pady=5)

tk.Label(
    form_frame,
    text='Enter your gender:',
    font=label_font,
    fg='#333333',
    bg='#FFFFFF'
).pack(anchor='w', padx=10, pady=5)

gender_var = tk.StringVar()
gender_var.set(None)

gender_frame = tk.Frame(form_frame, bg='#FFFFFF')
gender_frame.pack(anchor='w', padx=10, pady=5)

tk.Radiobutton(
    gender_frame,
    text='Male',
    variable=gender_var,
    value='Male',
    bg='#FFFFFF',
    font=label_font
).pack(side=tk.LEFT, padx=5)

tk.Radiobutton(
    gender_frame,
    text='Female',
    variable=gender_var,
    value='Female',
    bg='#FFFFFF',
    font=label_font
).pack(side=tk.LEFT, padx=5)

tk.Radiobutton(
    gender_frame,
    text='Prefer not to say',
    variable=gender_var,
    value='Prefer not to say',
    bg='#FFFFFF',
    font=label_font
).pack(side=tk.LEFT, padx=5)

tk.Label(
    form_frame,
    text='Enter your height (cm):',
    font=label_font,
    fg='#333333',
    bg='#FFFFFF'
).pack(anchor='w', padx=10, pady=5)

entry_height = tk.Entry(form_frame, width=30)
entry_height.pack(anchor='w', padx=10, pady=5)

tk.Label(
    form_frame,
    text='Enter your weight (kg):',
    font=label_font,
    fg='#333333',
    bg='#FFFFFF'
).pack(anchor='w', padx=10, pady=5)

entry_weight = tk.Entry(form_frame, width=30)
entry_weight.pack(anchor='w', padx=10, pady=5)

tk.Label(
    form_frame,
    text='Enter password for the account:',
    font=label_font,
    fg='#333333',
    bg='#FFFFFF'
).pack(anchor='w', padx=10, pady=5)

entry_pw = tk.Entry(form_frame, width=30, show='*')
entry_pw.pack(anchor='w', padx=10, pady=5)

create_button = tk.Button(
    form_frame,
    text='Create Your Account',
    command=saveuser,
    font=('Arial', 14, 'bold'),
    bg='#4CAF50',
    fg='#000000'
)

create_button.pack(pady=20)

signin_button = tk.Button(
    form_frame,
    text='Already have an account? Sign in!',
    command=open_signin,
    font=('Arial', 12, 'underline'),
    fg='#0000FF',
    bg='#FFFFFF',
    relief=tk.FLAT,
    cursor="hand2"
)

signin_button.pack(pady=10)

root.mainloop()
