firstnum = int(input("Enter the first number: "))
secondnum = int(input("Enter the second number: "))

if firstnum > secondnum:
    greater = firstnum
else:
    greater = secondnum

while True:
    if (greater % firstnum == 0) and (greater % secondnum == 0):
        print("LCM is: ", greater)
        break
    greater+=1