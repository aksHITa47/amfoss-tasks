import sys

def primefac(n):
    for i in range (2,n):
        if n%i==0:
            return False
    return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    primem = 0
    for i in range(2, n+1):
        if n%i == 0 and primefac(i):
            primem = i
    print(primem)
