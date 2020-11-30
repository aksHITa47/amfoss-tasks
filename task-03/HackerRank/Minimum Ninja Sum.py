t=int(input())
for i in range(t):
    l1=[]
    l2=[]
    l3=[]
    n,k=list(map(int,input().split()))
    while(n>0):
        b=n%10
        l1.append(b)
        n=n//10
    l1.reverse()
    if len(l1)<k:
        v=-1
        print(v)
    else:
        for j in range(len(l1)-k+1):
            x=0
            for m in range(k):
                x=x+l1[j+m]
            l2.append(x)
        for c in range(len(l2)-1):
            x=abs(l2[c]-l2[c+1])
            l3.append(x)
        l3.sort()
        print(l3[0])

