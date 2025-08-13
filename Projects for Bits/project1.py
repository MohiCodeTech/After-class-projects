A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
C = int(input("Enter a number: "))

result1 = A & B
result2 = B & C
result3 = B | C
result4 = result2 & result3
Q = result1 | result4
print(Q)