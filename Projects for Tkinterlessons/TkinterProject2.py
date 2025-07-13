#rock paper, scissor idk how im gonna do this
from tkinter import *
import tkinter as tk
import random
root = Tk()
root.title("Rock, paper, scissors game with the computer")
root.geometry("400x500")

label1 = tk.Label(root, text="Rock, Paper, Scissors Shoot!", font=("Sans-serif", 19))
label1.grid(pady=10)

comp_label = tk.Label(root, text="", font=("Arial", 13))
comp_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Sans", 14))
result_label.pack(pady=10)

choices = {"Rock", "Paper", "Scissors"}

def play(user_choice):
    comp_choice = random.choice(choices)
    comp_label.config(text=f"Computer chose: {comp_choice}")
    if user_choice == comp_choice:
        result = "Its a tie!"
    elif(user_choice == "Rock" and comp_choice == "Scissors") or \
        (user_choice == "Paper" and comp_choice == "Rock") or \
        (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You win!"
    else:
        print("You loose😥")

    result_label.config(text=result)

root.mainloop()
