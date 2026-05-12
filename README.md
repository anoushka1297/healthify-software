# Healthify- Your Wellness Companion

> Computer Science Project (2024–25) 
> Retrospectively documented—original development was done offline

A desktop wellness tracking app built in Python. Log daily health metrics, set fitness goals, track progress over time, and access healthy living resources, all through a Tkinter GUI.

---

## Features

- Account creation, login, and profile management with BMI indicator
- Daily health logging- body temperature, blood pressure, heart rate, hydration, sleep
- Goals tracker with progress bars, auto-removes completed goals
- Matplotlib line graphs for each health metric over time
- Curated healthy living resources (recipes, workouts, yoga, mental health, podcasts)

---
### Sign-in page
<img width="1470" height="928" alt="Screenshot 2026-05-12 at 11 48 29 PM" src="https://github.com/user-attachments/assets/b3ce2ad3-ad1f-4516-bbc1-9474aa51d7d9" />

### Menu page
<img width="1470" height="925" alt="Screenshot 2026-05-12 at 11 41 36 PM" src="https://github.com/user-attachments/assets/b4805452-a040-4377-b049-22dfdbb8b240" />

### Goals tracking
<img width="1470" height="928" alt="Screenshot 2026-05-12 at 11 43 29 PM" src="https://github.com/user-attachments/assets/b1a2c27b-048f-42d4-85e0-a8b6b1f7e9f1" />

### Data recording
<img width="1470" height="924" alt="Screenshot 2026-05-12 at 11 42 12 PM" src="https://github.com/user-attachments/assets/bb72edfe-6354-4494-acf5-7ea3d04b5abb" />

### Graph for health metric
<img width="1464" height="916" alt="Screenshot 2026-05-13 at 12 02 32 AM" src="https://github.com/user-attachments/assets/a687f106-8d95-4242-b78c-ae2773749100" />

## Requirements

- Python 3.x
- `sqlite3` — part of Python's standard library, no install needed
- The following third-party packages:

```bash
pip install pillow matplotlib
```

If youd prefer to use a virtual environment:

```bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install pillow matplotlib
```

---

## Running the App

```bash
python Account_Create.py
```

This opens the sign-up screen. Once you create an account you can sign in and access everything from the main menu. The `AccountDetails.csv` and `healthify.db` files are created automatically on first use- no manual setup needed.

---

## Project Structure

```
healthify/
├── Account_Create.py   #Sign up
├── signin.py           #Login
├── Menu_Signin.py      #Main menu hub
├── viewprof.py         #View profile + BMI
├── updateprof.py       #Edit profile/change password
├── goals.py            #Goals management
├── recdata.py          #Daily health data entry
├── progress.py         #Health entries tracking graphs
├── healthliv.py        #Healthy living resources
├── background.jpg      #Background image used across screens
├── healthyfood.png     |
├── workout_home.png    | 
├── mentalhealth.png    |- #Other images
├── yoga.png            |
├── sleep.png           |
└── mhs.png             |
```

---

## Notes

- `AccountDetails.csv` and `healthify.db` are generated locally when you run the app
- Passwords are stored in plaintext in the CSV (as-is from the original submission)
- The duplicate daily entry check is intentionally commented out in `recdata.py` to make it easier to populate graph data for testing

---

