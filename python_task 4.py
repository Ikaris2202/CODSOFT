import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

def user_choice(choice):
    global user_score, computer_score
    
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    result = determine_winner(choice, computer_choice)
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    update_scores()
    
    messagebox.showinfo("Result", f"Your choice: {choice}\nComputer's choice: {computer_choice}\n\n{result}")
    
    play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
    if not play_again:
        root.quit()

def update_scores():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

root = tk.Tk()
root.title("Rock, Paper, Scissors")
user_score = 0
computer_score = 0
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16))
title_label.pack(pady=10)

user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=("Arial", 14))
user_score_label.pack()

computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=("Arial", 14))
computer_score_label.pack()

choice_label = tk.Label(root, text="Choose your option:", font=("Arial", 14))
choice_label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", width=15, command=lambda: user_choice("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: user_choice("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: user_choice("Scissors"))
scissors_button.pack(pady=5)
root.mainloop()
