t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(str, input().split()))
    count=0
    for i in range(n):
        if a[0][i]!=a[0][len(a[0])-1]:
            count+=1
    print(count)