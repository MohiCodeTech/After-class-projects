def twoOddOccuringNumbers(arr, size):
    result = arr[0]
    x = 0
    y = 0
    setbit = 0

    for i in range(1, size):
        result = result ^ arr[i]

    setbit = result & ~(result - 1)
    for i in range(size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print("The two odd occuring numbers are: ", x ," and", y)

arr = []
arr_size = int(input("Enter the array size: "))
for i in range(0, arr_size):
    z = int(input("Enter your desired element: "))
    arr.append(z)



twoOddOccuringNumbers(arr, arr_size)
