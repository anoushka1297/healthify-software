import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import sys
import subprocess as sub
import sqlite3 as sq
import os

root = tk.Tk()
root.title("Healthify - Goals")
root.attributes('-fullscreen', True)
root.configure(bg="#e0f7fa")

goals_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge", padx=10, pady=10)
goals_frame.pack(pady=20, padx=10, fill="x")

goal_sections = []

def fetch_and_display_goals():
    for widget in goals_frame.winfo_children():
        widget.destroy()
    nric_signin = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, 'healthify.db')
    connection = sq.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT goal_name, current_prog, max_prog, goal_unit FROM goals WHERE NRIC=?", (nric_signin,))
    goals = cursor.fetchall()
    for goal in goals:
        goal_name, current_prog, max_prog, unit = goal
        create_goal_section(goals_frame, goal_name, current_prog, max_prog, unit)
    connection.close()

def create_goal_section(parent, title, value, max_value, unit):
    nric_signin = sys.argv[1]
    goal_data = {"name": title, "progress": value, "max_value": max_value, "unit": unit}
    frame = tk.Frame(parent, bg="#f0f4c3", padx=10, pady=10, bd=1, relief="solid")
    frame.pack(fill="x", pady=10)
    title_label = tk.Label(frame, text=title, bg="#f0f4c3", font=("Helvetica", 12, "bold"))
    title_label.grid(row=0, column=0, sticky="w")
    value_label = tk.Label(frame, text=f"{value} of {max_value} {unit}", bg="#f0f4c3", font=("Helvetica", 10))
    value_label.grid(row=1, column=0, sticky="w")
    progress = ttk.Progressbar(frame, length=200, value=value, maximum=max_value)
    progress.grid(row=1, column=1, padx=10)
    edit_button = tk.Button(frame, text="Edit", bg="#80deea", command=lambda: update_goal(goal_data, frame, value_label, progress))
    edit_button.grid(row=1, column=2, padx=5)
    remove_button = tk.Button(frame, text="Remove", bg="#ef5350", command=lambda: remove_goal(goal_data['name'], nric_signin))
    remove_button.grid(row=1, column=3, padx=5)
    goal_sections.append(goal_data)

def update_goal(goal_data, frame, value_label, progress):
    nric_signin = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, 'healthify.db')
    connection = sq.connect(db_path)
    cursor = connection.cursor()
    try:
        new_progress_value = int(simpledialog.askstring("Update Progress", f"Enter new progress for {goal_data['name']}:", parent=root))
        new_max_value = int(simpledialog.askstring("Update Max Value", f"Enter new maximum value for {goal_data['name']}:", parent=root))
        new_unit = simpledialog.askstring("Update Unit", f"Enter new unit for {goal_data['name']}:", parent=root)
        if new_progress_value > new_max_value:
            messagebox.showerror("Invalid input", "Progress cannot be greater than the maximum value.")
            return
        goal_data['progress'] = new_progress_value
        goal_data['max_value'] = new_max_value
        goal_data['unit'] = new_unit
        query = "UPDATE goals SET current_prog=?, max_prog=?, goal_unit=? WHERE NRIC=? AND goal_name=?"
        data = (goal_data['progress'], goal_data['max_value'], goal_data['unit'], nric_signin, goal_data['name'])
        cursor.execute(query, data)
        connection.commit()
        if goal_data['progress'] >= goal_data['max_value']:
            cursor.execute("DELETE FROM goals WHERE NRIC=? AND goal_name=?", (nric_signin, goal_data['name']))
            connection.commit()
            messagebox.showinfo("Congratulations!", f"You've completed the goal: {goal_data['name']}!")
        fetch_and_display_goals()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for progress and maximum value.")
    finally:
        cursor.close()
        connection.close()

def remove_goal(goal_name, nric_signin):
    if messagebox.askyesno("Confirm Removal", f"Are you sure you want to remove the goal: {goal_name}?"):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, 'healthify.db')
        connection = sq.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM goals WHERE NRIC=? AND goal_name=?", (nric_signin, goal_name))
        connection.commit()
        cursor.close()
        connection.close()
        messagebox.showinfo("Goal Removed", f"The goal '{goal_name}' has been removed.")
        fetch_and_display_goals()

def add_goal():
    nric_signin = sys.argv[1]
    goal_name = simpledialog.askstring("Add Goal", "Enter the name of your goal:", parent=root)
    if goal_name:
        try:
            max_value = int(simpledialog.askstring("Add Goal", "Enter the maximum value for this goal:", parent=root))
            progress_value = int(simpledialog.askstring("Add Goal", "Enter your current progress:", parent=root))
            unit = simpledialog.askstring("Add Goal", "Enter the unit for this goal (e.g., km, steps, kg):", parent=root)
            if progress_value > max_value:
                messagebox.showerror("Invalid input", "Progress cannot be greater than the maximum value.")
                return
            script_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(script_dir, 'healthify.db')
            connection = sq.connect(db_path)
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE if not exists goals(NRIC char(9), goal_name varchar(30), goal_unit varchar(10), current_prog INT, max_prog INT)')
            cursor.execute("INSERT INTO goals VALUES(?,?,?,?,?)", (nric_signin, goal_name, unit, progress_value, max_value))
            connection.commit()
            cursor.close()
            connection.close()
            fetch_and_display_goals()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for the maximum value and progress.")

def return_menu():
    nric_signin = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    menu_path = os.path.join(script_dir, 'Menu_Signin.py')
    if os.path.exists(menu_path):
        root.destroy()
        sub.Popen([sys.executable, menu_path, nric_signin])

fetch_and_display_goals()

add_goal_frame = tk.Frame(root, bg="#e0f7fa")
add_goal_frame.pack(fill="x", pady=10)
add_goal_button = tk.Button(add_goal_frame, text="➕ Add Goal", font=("Helvetica", 14), bg="#a5d6a7", relief="flat", command=add_goal)
add_goal_button.pack(pady=10)
return_menu_button = tk.Button(add_goal_frame, text="↩️ Return to Menu", font=("Helvetica", 14), bg="#a5d6a7", relief="flat", command=return_menu)
return_menu_button.pack(pady=10)

root.mainloop()

