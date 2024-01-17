# main.py

import tkinter as tk
from app.functions import authenticate, create_post_login_screen, create_image_label, create_core_screen, create_fantasy_screen

def show_screen(frame):
    for f in [login_frame, post_login_frame, core_frame, fantasy_frame]:
        f.pack_forget()
    frame.pack()

def show_post_login_screen():
    show_screen(post_login_frame)

def show_core_screen():
    show_screen(core_frame)

def show_fantasy_screen():
    show_screen(fantasy_frame)

def check_login():
    if authenticate(entry_username.get(), entry_password.get()):
        show_post_login_screen()
    else:
        message_label.config(text="Login Failed: Incorrect username or password.")

window = tk.Tk()
window.title("Gridiron Guru")
title_label = tk.Label(window, text="Gridiron Guru", font=("Helvetica", 16, "bold"))
title_label.pack()
login_frame = tk.Frame(window)
login_frame.pack()
image_label_login = create_image_label(login_frame)
image_label_login.pack()
label_username = tk.Label(login_frame, text="Username")
label_username.pack()
entry_username = tk.Entry(login_frame)
entry_username.pack()
label_password = tk.Label(login_frame, text="Password")
label_password.pack()
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()
login_button = tk.Button(login_frame, text="Login", command=check_login)
login_button.pack()
message_label = tk.Label(login_frame, text="")
message_label.pack()
post_login_frame, button_core, button_fantasy = create_post_login_screen(window)
core_frame = create_core_screen(window, show_post_login_screen)
fantasy_frame = create_fantasy_screen(window, show_post_login_screen)
button_core.config(command=show_core_screen)
button_fantasy.config(command=show_fantasy_screen)
window.mainloop()
