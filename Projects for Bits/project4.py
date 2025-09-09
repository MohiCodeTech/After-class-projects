def power8(number):
    if number <= 0:
        return False
    else:
        return (number & (number - 1) == 0 and (number - 1) % 7 == 0)
    
number = int(input("Enter a number to check if it is a power of 8: "))

if power8(number):
    print("The number is a power of 8")
else:
    print("The number is not a power of 8")