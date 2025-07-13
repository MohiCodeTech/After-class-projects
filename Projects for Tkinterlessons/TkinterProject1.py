from tkinter import *
root = Tk()
root.title("registration form")
root.geometry("200x200")

def msg():
    print("Registraction successful")
    print(f"Usename is {entry1.get()}, Password is {entry2.get()}")

label1 = Label(root, text="Username: ")
label1.grid(row=0, column=0, padx=5, pady=10)

entry1 = Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=10)

label2 = Label(root, text="Password: ")
label2.grid(row=1, column=0, padx=5, pady=10)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=10)

button1 = Button(root, text="Submit Form", command=msg)
button1.grid(row=2, column=0,columnspan=2, pady=5)

root.mainloop()