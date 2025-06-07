print("Hello!")
favnumber = int(input("What is your favourite number?: "))
if favnumber >= 25:
    print("Your favourite number is high! we can procceed")
    if favnumber % 2 == 0:
        print("Wow your favourite number is even!")
    else:
        print("Your favourite number is odd!")
else:
    print("Your favourite number is too small to procceed")

favfood = input("What is your favourite food: ")
if favfood.upper() == "DOSA":
    print("Nice that is also my favourite food")
    
else:
    print("Nice choice!")
    if favfood.upper() == "CHAPATI" or "NOODLES":
        print("Those are my 2nd favourite foods!")
    else:
        print("again nice selection!")