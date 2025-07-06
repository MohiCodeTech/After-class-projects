filereplacement = "Python is hard but if you try harder it will be easy"
with open("sample.txt", "w") as file:
    words = filereplacement.split()
    for word in words:
        file.write("\n" + word)
print("data change successful")

try:
    with open("hello.txt", "x") as file:
        file.write("this is a newly created file")
    print("File created successfully")
except FileExistsError:
    print("file already exists")

import os
filename = "rose.txt"
if os.path.exists(filename):
    print("This file exists")
else:
    print("This file doesnt exist")

anotherfilename = "some.txt"
if not os.path.exists(anotherfilename):
    with open(anotherfilename, "w") as file:
        file.write("A newly made file")
    print("New file created")
else:
    print("File already exists")

#remove file
anotherfilename = "some.txt"
if os.path.exists(anotherfilename):
    os.remove(anotherfilename)
    print(f"File {anotherfilename} has been deleted")
else:
    print(f"No such file as {anotherfilename}")

# remove folder
foldername = "folder1"
if os.path.exists(foldername):
    os.rmdir(foldername)
    print(f"Folder {foldername} has been now deleted")
else:
    print("No folder can be seen with that name")