#Longetst1s
n = int(input("Enter a number to find its longest consecutive 1s: "))
current_count = 0  
max_count = 0
while n > 0:
    if n & 1:
        current_count +=1
        max_count = max(max_count, current_count)
    else:
        current_count = 0
    n >>= 1

print("longest consecutive ones: ", max_count)