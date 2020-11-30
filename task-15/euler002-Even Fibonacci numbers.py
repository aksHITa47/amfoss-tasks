import sys

def evensum_fibser(n):
    f1  = 2
    f2  = 8
    sum = 10
    while True :
        fn = 4*f2 + f1
        if fn>=n: return sum
        sum += fn
        f1, f2 = f2, fn
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(evensum_fibser(n))
