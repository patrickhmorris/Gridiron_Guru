# app/functions.py

import tkinter as tk
from tkinter import PhotoImage

def authenticate(username, password):
    # Placeholder for authentication logic
    return username == "admin" and password == "password"

def create_image_label(master):
    image_path = r'C:\Users\grays\PycharmProjects\Gridiron_Guru\Gridiron Guru.png'
    image = PhotoImage(file=image_path)
    image_label = tk.Label(master, image=image)
    image_label.image = image  # Keep a reference
    return image_label

def create_post_login_screen(master):
    frame = tk.Frame(master)
    image_label = create_image_label(frame)
    image_label.grid(row=0, column=1, sticky="ne")  # Top right corner
    button_style = {'padx': 10, 'pady': 10, 'width': 10, 'height': 2}
    button_core = tk.Button(frame, text="Core", **button_style)
    button_core.grid(row=1, column=0, padx=10, pady=10)
    button_fantasy = tk.Button(frame, text="Fantasy", **button_style)
    button_fantasy.grid(row=1, column=1, padx=10, pady=10)
    button_gambling = tk.Button(frame, text="Gambling", **button_style)
    button_gambling.grid(row=1, column=2, padx=10, pady=10)
    return frame, button_core, button_fantasy  # Return buttons for later configuration

def create_back_button(master, back_command):
    back_button = tk.Button(master, text="← Back", command=back_command)
    back_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
    return back_button

def create_core_screen(master, back_command):
    frame = tk.Frame(master)

    # Back Button in the top-left corner
    create_back_button(frame, back_command)

    # Title Label "Core", centered under "Gridiron Guru"
    title_label = tk.Label(frame, text="Core", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)

    # Image label, positioned to align with the title
    image_label = create_image_label(frame)
    image_label.grid(row=1, column=0, columnspan=3, sticky="n", padx=10, pady=10)

    # Button "Players", centered at the bottom
    button_players = tk.Button(frame, text="Players", padx=10, pady=10)
    button_players.grid(row=2, column=0, padx=10, pady=10)

    # Button "Teams", centered at the bottom
    button_teams = tk.Button(frame, text="Teams", padx=10, pady=10)
    button_teams.grid(row=2, column=1, padx=10, pady=10)

    # Button "Standings", centered at the bottom
    button_standings = tk.Button(frame, text="Standings", padx=10, pady=10)
    button_standings.grid(row=2, column=2, padx=10, pady=10)

    return frame

def create_fantasy_screen(master, back_command):
    frame = tk.Frame(master)

    # Back Button in the top-left corner
    create_back_button(frame, back_command)

    # Title Label "Fantasy", centered under "Gridiron Guru"
    title_label = tk.Label(frame, text="Fantasy", font=("Graduate", 16))
    title_label.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)

    # Image label, positioned to align with the title
    image_label = create_image_label(frame)
    image_label.grid(row=1, column=0, columnspan=3, sticky="n", padx=10, pady=10)

    # Button "Player Points", centered at the bottom
    btn_player_points = tk.Button(frame, text="Player Points", padx=10, pady=10)
    btn_player_points.grid(row=2, column=0, padx=10, pady=10)

    # Button "Top Scores of the Week", centered at the bottom
    btn_top_scores = tk.Button(frame, text="Top Scores of the Week", padx=10, pady=10)
    btn_top_scores.grid(row=2, column=1, padx=10, pady=10)

    # Button "Waiver Waitlist", centered at the bottom
    btn_waiver_waitlist = tk.Button(frame, text="Waiver Waitlist", padx=10, pady=10)
    btn_waiver_waitlist.grid(row=2, column=2, padx=10, pady=10)

    return frame
