def fibonacci(n):
    if n == 0:
        return 1
    else:
        return n - fibonacci(n - 1) + fibonacci(n - 2)

num = int(input('enter a number!: '))
ans = fibonacci(5)
print(f"The fibonacci of {num} is {ans}")