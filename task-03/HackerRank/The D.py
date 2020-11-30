n=int(input())
#upper pyramid
for i in range(1,n+1,+2):
    for j in range(n-i,0,-2):
        print("*",end="")
    for k in range(n-i,n):
        print("D",end="")
    for j in range(n-i,0,-2):
        print("*",end="")
    print()
#lower pyramid
for i in range(n-2,0,-2):
    for j in range(n-i,0,-2):
        print("*",end="")
    for k in range(n-i,n):
        print("D",end="")
    for j in range(n-i,0,-2):
        print("*",end="")
