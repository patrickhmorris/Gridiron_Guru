# app/functions.py

import tkinter as tk
from tkinter import PhotoImage


def authenticate(username, password):
    # Placeholder for authentication logic
    return username == "admin" and password == "password"


def create_image_label(master):
    image_path = r'C:\Users\patri\Gridiron Guru\Gridiron Guru.png'
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


def create_fantasy_screen(master, back_command, show_player_points_screen, show_top_scorers_screen,
                          show_waiver_watchlist_screen):
    frame = tk.Frame(master)

    # Back Button in the top-left corner
    create_back_button(frame, back_command)

    # Title Label "Fantasy", centered under "Gridiron Guru"
    title_label = tk.Label(frame, text="Fantasy", font=("Graduate", 16))
    title_label.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)

    # Image label, positioned to align with the title
    image_label = create_image_label(frame)
    image_label.grid(row=1, column=0, columnspan=3, sticky="n", padx=10, pady=10)

    # Configure the buttons
    btn_player_points = tk.Button(frame, text="Player Points", command=show_player_points_screen)
    btn_player_points.grid(row=2, column=0, padx=10, pady=10)

    btn_top_scores = tk.Button(frame, text="Top Scorers of the Week", command=show_top_scorers_screen)
    btn_top_scores.grid(row=2, column=1, padx=10, pady=10)

    btn_waiver_watchlist = tk.Button(frame, text="Waiver Watchlist", command=show_waiver_watchlist_screen)
    btn_waiver_watchlist.grid(row=2, column=2, padx=10, pady=10)

    return frame


def create_players_screen(master, back_command):
    frame = tk.Frame(master)

    # Back Button in the top-left corner
    back_button = create_back_button(frame, back_command)
    back_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)  # Place the back button

    # Title Label "Players", centered at the top
    title_label = tk.Label(frame, text="Players", font=("Helvetica", 16))
    title_label.grid(pady=10)

    # Sample data for players
    sample_players = [
        {"name": "Player A", "position": "Quarterback", "team": "Team X"},
        {"name": "Player B", "position": "Running Back", "team": "Team Y"},
        {"name": "Lamar Jackson", "position": "Running Back", "team": "Baltimore"},
    ]

    # Create a label for each player and pack it into the frame
    for player in sample_players:
        player_label = tk.Label(frame, text=f"{player['name']} - {player['position']} - {player['team']}")
        player_label.grid()

    return frame


def create_teams_screen(master, back_command):
    frame = tk.Frame(master)

    # Back Button
    back_button = create_back_button(frame, back_command)
    back_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)  # Place the back button

    # Title Label "Teams"
    title_label = tk.Label(frame, text="Teams", font=("Helvetica", 16))
    title_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Sample data for teams
    sample_teams = ["Team A", "Team B", "Team C", "Team D"]

    # Display teams
    for i, team in enumerate(sample_teams, start=2):
        team_label = tk.Label(frame, text=team)
        team_label.grid(row=i, column=0, columnspan=3, sticky="w", padx=10, pady=2)

    return frame


def create_standings_screen(master, back_command):
    frame = tk.Frame(master)

    # Back Button
    back_button = create_back_button(frame, back_command)
    back_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)  # Place the back button

    # Title Label "Standings"
    title_label = tk.Label(frame, text="Standings", font=("Helvetica", 16))
    title_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Sample data for standings
    sample_standings = ["1st: Team A", "2nd: Team B", "3rd: Team C", "4th: Team D"]

    # Display standings
    for i, standing in enumerate(sample_standings, start=2):
        standing_label = tk.Label(frame, text=standing)
        standing_label.grid(row=i, column=0, columnspan=3, sticky="w", padx=10, pady=2)

    return frame


# Fantasy Screen Breakdown
def create_player_points_screen(master, back_command):
    frame = tk.Frame(master)
    create_back_button(frame, back_command)

    # Sample data for player points
    sample_data = [
        {"name": "Player 1", "expected": 15, "scored": 20},
        {"name": "Player 2", "expected": 10, "scored": 12}
    ]

    for i, player in enumerate(sample_data, start=1):
        label = tk.Label(frame, text=f"{player['name']} - Expected: {player['expected']}, Scored: {player['scored']}")
        label.grid(row=i, sticky="w", padx=10, pady=2)

    return frame


def create_top_scorers_screen(master, back_command):
    frame = tk.Frame(master)
    create_back_button(frame, back_command)

    # Sample data for top scorers
    sample_scorers = [
        {"name": "Player 3", "points": 24},
        {"name": "Player 4", "points": 18}
    ]

    for i, player in enumerate(sample_scorers, start=1):
        label = tk.Label(frame, text=f"{player['name']} - Points: {player['points']}")
        label.grid(row=i, sticky="w", padx=10, pady=2)

    return frame


def create_waiver_watchlist_screen(master, back_command):
    frame = tk.Frame(master)
    create_back_button(frame, back_command)

    # Sample data for waiver watchlist
    sample_watchlist = ["Player 5", "Player 6", "Player 7"]

    for i, player in enumerate(sample_watchlist, start=1):
        label = tk.Label(frame, text=player)
        label.grid(row=i, sticky="w", padx=10, pady=2)

    return frame
    
