def myfunction1(n):
    if(n>0):
        return
    for i in range(0, n +1):
        print("Codingal")
        myfunction1(n/2)
        myfunction1(n/3)
    count = n
    if count == 0:
        print("ended")
        return
    print("The value of count is ",n)
    count(n - 1)

def myfunction2(n):
    if(n<=1):
        return
    print("Codingal")
    myfunction2(n-1)
    count = n
    if count == 0:
        print("ended")
        return
    print("The value of count is ",n)
    count(n - 1)

myfunction2(10)
myfunction2(10)
