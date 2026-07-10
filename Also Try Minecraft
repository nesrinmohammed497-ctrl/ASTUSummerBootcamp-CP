n,m =map(int,input().split())
a=list(map(int,input().split()))
for _ in range(m):
    s,t= map(int,input().split())
    count=0
    if s > t :
        for i in range(s-1 , t-1 ,-1):
            if a[i-1] < a[i]:
                count += a[i] - a[i-1]
        print (count )
    else:
        if t-s==1:
            print(a[s-1]-a[s])
        else:
            for i in range(s , t):
                if a[i] < a[i-1]:
                    count += a[i-1] - a[i]
                
            print (count )
