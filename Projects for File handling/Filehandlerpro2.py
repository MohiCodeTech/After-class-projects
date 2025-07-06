with open("sample.txt", 'r') as file:
    print(file.read(5))
    print(file.tell())
    print(file.read(20))

with open("sample.txt", "r") as file:
    line = file.readline()
    print(line)

with open("sample.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open("sample.txt", "r") as file:
    print(file.readlines())

with open("sample.txt", "r") as file:
    for i in file:
        print(i)

with open("sample.txt", "r") as file:
    for line in file.readlines():
        print(line.strip())