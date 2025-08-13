N = int(input("Enter a number: "))
M = int(input("Enter another number: "))
def function(N, M):
    for i in range(N):
        result = N * M
        for j in range(N + 1):
            result = N * M
    print(result)
function(N, M)
