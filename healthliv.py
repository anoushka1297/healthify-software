import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import webbrowser
import subprocess as sub
import sys
import os

def open_link(url):
    webbrowser.open_new(url)

def menu_signin():
    nric_signin = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    menu_path = os.path.join(script_dir, 'Menu_Signin.py')
    if os.path.exists(menu_path):
        root.destroy()
        sub.Popen([sys.executable, menu_path, nric_signin])

def create_healthy_living_frame(parent):
    healthy_living_frame = tk.Frame(parent, bg="#e0f7fa", padx=20, pady=20)
    healthy_living_frame.pack(expand=True, fill='both')
    title_label = tk.Label(healthy_living_frame, text="Healthy Living Resources",
                           font=("Helvetica", 24, "bold"), bg="#e0f7fa")
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
    resources = [
        ("Healthy Recipes",
         "https://www.eatingwell.com/recipes/23006/health-condition/diabetic/low-cholesterol/",
         "healthyfood.png"),
        ("Home Workouts", "https://youtu.be/gC_L9qAHVJ8?si=DyDlyQ8T-ZnPoi-s",
         "workout_home.png"),
        ("Mental Health Awareness", "https://youtu.be/RUrpw8RLEDI?si=FoDCqxTZ8mHEQw16",
         "mentalhealth.png"),
        ("Yoga for Beginners", "https://youtu.be/AB3Y-4a3ZrU?si=1sP0Q_dVfsaLYhDl",
         "yoga.png"),
        ("Sleep and Recovery",
         "https://www.calm.com/blog/how-to-sleep-better-at-night-naturally", "sleep.png"),
        ("The Model Health Show Podcast",
         "https://www.youtube.com/playlist?app=desktop&list=PL3zvw5sD7WKwPUsdb57K14sBfGCEKIUtH",
         "mhs.png")
    ]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for index, (title, url, image_path) in enumerate(resources):
        resource_frame = tk.Frame(healthy_living_frame, bg="#ffffff", bd=2,
                                  relief="groove", padx=10, pady=10)
        resource_frame.grid(row=index // 2 + 1, column=index % 2, padx=10, pady=10,
                            sticky="nsew")
        healthy_living_frame.columnconfigure(index % 2, weight=1)
        full_image_path = os.path.join(script_dir, image_path)
        try:
            image = Image.open(full_image_path)
            image = image.resize((200, 125)) 
            thumbnail = add_rounded_corners(image, radius=30)
            thumbnail = ImageTk.PhotoImage(thumbnail)
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            thumbnail = None
        if thumbnail:
            thumbnail_label = tk.Label(resource_frame, image=thumbnail)
            thumbnail_label.image = thumbnail 
            thumbnail_label.pack(side=tk.TOP, pady=(0, 10))
        resource_button = tk.Button(resource_frame, text=title, command=lambda url=url:
                                    open_link(url), bg="#a5d6a7", font=("Helvetica", 12), width=25)
        resource_button.pack(side=tk.BOTTOM)

def add_rounded_corners(image, radius):
    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    alpha = Image.new('L', image.size, 255)
    w, h = image.size
    alpha.paste(circle.crop((0, 0, radius * 2, radius * 2)), (0, 0))
    alpha.paste(circle.crop((0, 0, radius * 2, radius * 2)), (w - radius * 2, 0))
    alpha.paste(circle.crop((0, 0, radius * 2, radius * 2)), (0, h - radius * 2))
    alpha.paste(circle.crop((0, 0, radius * 2, radius * 2)), (w - radius * 2, h - radius * 2))
    image.putalpha(alpha)
    return image

root = tk.Tk()
root.title("Healthy Living")
root.attributes('-fullscreen', True) 
root.configure(bg="#e0f7fa")

create_healthy_living_frame(root)

button_frame = tk.Frame(root, bg='white')
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(10, 10)) 

menusignin_button = tk.Button(button_frame, text='Go back to Menu',
                              command=menu_signin,
                              font=('Arial', 12, 'underline'), fg='#0000FF',
                              bg='#FFFFFF', relief=tk.FLAT, cursor="hand2")
menusignin_button.pack(pady=(10, 20)) 

root.mainloop()

