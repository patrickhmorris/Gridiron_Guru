# main.py

import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from app.functions import authenticate  # Corrected import statement

def check_login():
    username = entry_username.get()
    password = entry_password.get()
    if authenticate(username, password):
        messagebox.showinfo("Login Success", "You have successfully logged in.")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

# Create the main window
window = tk.Tk()
window.title("Gridiron Guru Login")

# Load and display the image
image_path = 'C:\\Users\\grays\\PycharmProjects\\Gridiron_Guru\\Gridiron Guru.png'
image = PhotoImage(file=image_path)
image_label = tk.Label(window, image=image)
image_label.pack()

# Username
label_username = tk.Label(window, text="Username")
label_username.pack()

entry_username = tk.Entry(window)
entry_username.pack()

# Password
label_password = tk.Label(window, text="Password")
label_password.pack()

entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Login Button
login_button = tk.Button(window, text="Login", command=check_login)
login_button.pack()

# Start the GUI event loop
window.mainloop()

