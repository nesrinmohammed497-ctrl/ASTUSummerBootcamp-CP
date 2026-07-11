t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    max_value=max(a)
    ans=[]
    for i in range(m):
        c,l,r = input().split()
        l = int(l)
        r = int(r)
        if l<= max_value <= r:
            if c == '+':
                max_value += 1
            else:
                max_value -= 1
        ans.append(max_value)
    print(*ans)
