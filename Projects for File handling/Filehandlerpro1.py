with open("sample.txt", "r") as file:
    text = file.read()
    print(text)

with open("sample.txt", "w")as file:
    file.write("Hello\n")
    file.write("Them\n")
    file.write("Theirs\n")

with open("sample.txt", "r") as file:
    text = file.read()
    print(text)

with open("sample.txt", "a") as file:
    file.write("Ours\n")
    file.write("altogether\n")

with open("sample.txt", "r") as file:
    text = file.read()
    print(text)
