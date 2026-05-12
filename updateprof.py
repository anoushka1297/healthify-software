import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess as sub
import sys
import csv
import os

def curaccount_details():
    if len(sys.argv) > 1:
        nric_signin = sys.argv[1]
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, 'AccountDetails.csv')
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == nric_signin:
                    return row

def savechanges():
    nric = sys.argv[1]
    newname = entry_name.get()
    newheight = entry_height.get()
    newweight = entry_weight.get()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'AccountDetails.csv')
    file=open(csv_path, 'r')
    reader=csv.reader(file)
    records=list(reader)
    for i in range(len(records)):
        if records[i][0]==nric:
            records[i][1]=newname
            records[i][4]=newheight
            records[i][5]=newweight
            break
    file.close()
    with open(csv_path, 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerows(records)
    messagebox.showinfo('Success', 'Profile Updated')

def return_menu():
    nric_signin = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    menu_path = os.path.join(script_dir, 'Menu_Signin.py')
    if os.path.exists(menu_path):
        root.destroy()
        sub.Popen([sys.executable, menu_path, nric_signin])

def open_password_dialog():
    dialog = tk.Toplevel()
    dialog.title("Change Password")
    dialog.geometry("300x300")
    tk.Label(dialog, text="Old Password:").pack(pady=5)
    old_password_entry = tk.Entry(dialog, show='*')
    old_password_entry.pack(pady=5, padx=10, fill='x')
    tk.Label(dialog, text="New Password:").pack(pady=5)
    new_password_entry = tk.Entry(dialog, show='*')
    new_password_entry.pack(pady=5, padx=10, fill='x')
    tk.Label(dialog, text="Confirm New Password:").pack(pady=5)
    confirm_password_entry = tk.Entry(dialog, show='*')
    confirm_password_entry.pack(pady=5, padx=10, fill='x')
    def submit_password_change():
        nric = sys.argv[1]
        old_password = old_password_entry.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()
        if not old_password or not new_password or not confirm_password:
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return
        if new_password != confirm_password:
            messagebox.showwarning("Password Mismatch", "New passwords do not match.")
            return
        records = []
        password_correct = False
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, "AccountDetails.csv")
        with open(csv_path, "r") as file:
            reader = csv.reader(file)
            for record in reader:
                if record[0] == nric:
                    if record[6] == old_password:
                        password_correct = True
                        record[6] = new_password
                    records.append(record)
                else:
                    records.append(record)
        if not password_correct:
            messagebox.showwarning("Old Password Error", "Old password is incorrect.")
            return
        with open(csv_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(records)
        messagebox.showinfo("Success", "Password changed successfully!")
        dialog.destroy()
    tk.Button(dialog, text="Submit", command=submit_password_change).pack(pady=10)
    tk.Button(dialog, text="Cancel", command=dialog.destroy).pack(pady=5)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title('HEALTHIFY- Create your account now!')
root.configure(bg='#90EE90')
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
script_dir = os.path.dirname(os.path.abspath(__file__))
bg_path = os.path.join(script_dir, 'background.jpg')
image=Image.open(bg_path)
image = image.resize((window_width, window_height))
photo=ImageTk.PhotoImage(image)
tk.Label(root,image=photo).grid(row=1,column=1)
profile_frame = tk.Frame(root, bg='#FFFFFF', bd=2, relief='groove')
profile_frame.place(anchor=tk.CENTER, relx=0.5, rely=0.5, width=700, height=400)
tk.Label(profile_frame, text="Update Profile", font=("Helvetica", 22, 'bold'),
         fg='#333333', bg='#FFFFFF').grid(row=0, column=0, columnspan=2, pady=(20, 20),
         sticky='n')
old_details = curaccount_details()
old_name, old_height, old_weight = old_details[1], old_details[4], old_details[5]
tk.Label(profile_frame, text="Name:", font=("Arial", 14), fg='#333333',
         bg='#FFFFFF').grid(row=1, column=0, sticky="w", padx=20, pady=10)
entry_name = tk.Entry(profile_frame, font=("Arial", 12), width=40)
entry_name.grid(row=1, column=1, padx=20, pady=10, sticky='ew')
entry_name.insert(0, old_name)
tk.Label(profile_frame, text="Height (cm):", font=("Arial", 14), fg='#333333',
         bg='#FFFFFF').grid(row=2, column=0, sticky="w", padx=20, pady=10)
entry_height = tk.Entry(profile_frame, font=("Arial", 12), width=40)
entry_height.grid(row=2, column=1, padx=20, pady=10, sticky='ew')
entry_height.insert(0, old_height)
tk.Label(profile_frame, text="Weight (kg):", font=("Arial", 14), fg='#333333',
         bg='#FFFFFF').grid(row=3, column=0, sticky="w", padx=20, pady=10)
entry_weight = tk.Entry(profile_frame, font=("Arial", 12), width=40)
entry_weight.grid(row=3, column=1, padx=20, pady=10, sticky='ew')
entry_weight.insert(0, old_weight)
save_button = tk.Button(profile_frame, text="Save Changes", font=("Arial", 14),
                        command=savechanges)
save_button.grid(row=4, column=0, columnspan=2, pady=20, sticky='ew')
change_password_link = tk.Label(profile_frame, text="Change Password?", fg="blue",
                               cursor="hand2", bg='#FFFFFF', font=("Arial", 12))
change_password_link.grid(row=5, column=0, columnspan=2, pady=10, sticky='n')
change_password_link.bind("<Button-1>", lambda e: open_password_dialog())
profile_frame.grid_columnconfigure(0, weight=1)
profile_frame.grid_columnconfigure(1, weight=2)
profile_frame.grid_rowconfigure(0, weight=0)
profile_frame.grid_rowconfigure(1, weight=1)
profile_frame.grid_rowconfigure(2, weight=1)
profile_frame.grid_rowconfigure(3, weight=1)
profile_frame.grid_rowconfigure(4, weight=0)
profile_frame.grid_rowconfigure(5, weight=0)
menu_button = tk.Button(root, text='Go back to Menu', font=("Helvetica", 12,
                        'underline'), relief=tk.FLAT, cursor='hand2',
                        fg='#0000FF', command=return_menu, bg='#FFFFFF')
menu_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
root.mainloop()

