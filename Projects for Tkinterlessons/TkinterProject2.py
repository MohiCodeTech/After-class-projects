
from tkinter import *
import random

def play_game(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
    else:
        result = "You lose!"

    result_text.set(f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.configure(bg='lightblue')

Label(root, text="Rock Paper Scissors", font=('Arial', 18), bg='lightblue').pack(pady=20)

result_text = StringVar()
Label(root, textvariable=result_text, font=('Arial', 12), bg='lightblue').pack(pady=20)

Button(root, text="Rock", width=15, command=lambda: play_game("Rock")).pack(pady=5)
Button(root, text="Paper", width=15, command=lambda: play_game("Paper")).pack(pady=5)
Button(root, text="Scissors", width=15, command=lambda: play_game("Scissors")).pack(pady=5)

Button(root, text="Exit", width=10, command=root.destroy, bg='red', fg='white').pack(pady=20)

root.mainloop()