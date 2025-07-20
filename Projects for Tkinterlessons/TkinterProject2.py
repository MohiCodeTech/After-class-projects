#rock paper, scissor idk how im gonna do this
from tkinter import *
import tkinter as tk
import random
root = Tk()
root.title("Rock, paper, scissors game with the computer")
root.geometry("400x500")

label1 = tk.Label(root, text="Rock, Paper, Scissors Shoot!", font=("Sans-serif", 19))
label1.pack(pady=10)

comp_label = tk.Label(root, text="", font=("Arial", 13))
comp_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Sans", 14))
result_label.pack(pady=10)


def play(user_choice):
    comp_choice = random.choice()
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

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

rock_btn = tk.Button(btn_frame, text="Rock", width=10, font=("Arial", 19), command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, font=("Arial", 19), command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, font=("Arial", 19), command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()