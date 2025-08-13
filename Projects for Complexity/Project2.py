def myfunction(n):
    iterations = 0
    for i in range(0, n+1):
        print("First Loop")
        iterations +=1
    
    j = 1
    while(j<=n+1):
        print("Second loop", j)
        j = j * 2
        iterations += 1

    for i in range(0, 100):
        print("Third Loop")
        iterations +=1
        print("For all iterations the time complexity taken was", iterations)

myfunction(3)

