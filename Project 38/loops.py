number = 4
for i in range(1,11):
    print(f"{number} x {i} = {number * i}")

for i in range(1,6):
    print('* '* i)

for i in range(1,6):
    for j in range(1, i + 1):
        print('* ', end="")
    print()
