t = int(input())
while t > 0:
    t-=1
    n,p = list(map(int,input().split()))
    d = 0
    for i in range(2,n+1) :
        while i % p == 0:
            i/=p
            d+=1
    print(d)
             
    