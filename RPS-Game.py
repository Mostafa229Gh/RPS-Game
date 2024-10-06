import tkinter as tk
from random import randint
from tkinter import font
from tkinter import messagebox


def show_frame(frame):
    frame.tkraise()

# Function to handle game logic


def play_game(player_choice):
    global Player1Wins, Player2Wins, choose
    computerMove = randint(0, 2)
    Player_2 = choice1[computerMove]

    robot_move_label.config(text=f"Robot move: {Player_2}")

    if player_choice == Player_2:
        result_text.set("That's a tie!")
    elif (player_choice == "rock" and Player_2 == "scissors") or \
         (player_choice == "paper" and Player_2 == "rock") or \
         (player_choice == "scissors" and Player_2 == "paper"):
        Player1Wins += 1
        result_text.set("Player 1 wins!")
    else:
        Player2Wins += 1
        result_text.set("Player 2 wins!")

    score_text.set(f"Player 1: {Player1Wins} | Player 2: {Player2Wins}")

    # Check if someone won
    if Player1Wins >= choose or Player2Wins >= choose:
        if Player1Wins > Player2Wins:
            winner_label.config(text="Player 1 Wins!")
        else:
            winner_label.config(text="Player 2 Wins!")
        show_frame(winner_frame)

# Function to start the game


def start_game():
    global choose, Player1Wins, Player2Wins
    try:
        choose = int(score_entry.get())
        if choose <= 0:
            raise ValueError
        Player1Wins, Player2Wins = 0, 0
        score_text.set(f"Player 1: {Player1Wins} | Player 2: {Player2Wins}")
        result_text.set("")
        robot_move_label.config(text="")
        show_frame(game_frame)
    except ValueError:
        messagebox.showerror(
            "Invalid Input", "Please enter a valid number for the score to win!")

# Function to reset game state for a new game


def reset_game():
    global Player1Wins, Player2Wins
    Player1Wins, Player2Wins = 0, 0
    score_entry.delete(0, tk.END)
    score_entry.insert(0, "3")
    result_text.set("")
    robot_move_label.config(text="")
    show_frame(start_frame)


# Initialize the GUI window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("250x300")  # Set window size to 250px by 300px

# Font settings
large_font = font.Font(size=12)
button_font = font.Font(size=10)

choice1 = ["rock", "paper", "scissors"]
Player1Wins, Player2Wins, choose = 0, 0, 3

# Create frames for different screens
start_frame = tk.Frame(window)
game_frame = tk.Frame(window)
winner_frame = tk.Frame(window)

for frame in (start_frame, game_frame, winner_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# ------------------- Start Frame -------------------
tk.Label(start_frame, text="Set score to win", font=large_font).pack(pady=10)
score_entry = tk.Entry(start_frame, font=large_font, justify="center")
score_entry.insert(0, "3")
score_entry.pack(pady=10)

start_button = tk.Button(start_frame, text="Start",
                         font=button_font, command=start_game)
start_button.pack(pady=10)

# ------------------- Game Frame -------------------
# Score at the top
score_text = tk.StringVar()
tk.Label(game_frame, textvariable=score_text, font=large_font).pack(pady=10)

# Removed "Robot Move" title
robot_move_label = tk.Label(game_frame, text="", font=large_font)
robot_move_label.pack(pady=10)

result_text = tk.StringVar()
tk.Label(game_frame, textvariable=result_text, font=large_font).pack(pady=10)

button_frame = tk.Frame(game_frame)
button_frame.pack(pady=10)

# Create buttons for Rock, Paper, Scissors
buttons = []
for choice in choice1:
    button = tk.Button(button_frame, text=choice.capitalize(), font=button_font,
                       command=lambda c=choice: play_game(c), width=8, height=1)
    button.pack(side=tk.LEFT, padx=5)
    buttons.append(button)

# ------------------- Winner Frame -------------------
winner_label = tk.Label(winner_frame, text="", font=large_font)
winner_label.pack(pady=20)

exit_button = tk.Button(winner_frame, text="Exit",
                        font=button_font, command=window.quit)
exit_button.pack(side=tk.LEFT, padx=10, pady=10)

play_again_button = tk.Button(
    winner_frame, text="Play Again", font=button_font, command=reset_game)
play_again_button.pack(side=tk.RIGHT, padx=10, pady=10)

show_frame(start_frame)

window.mainloop()
