t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum=[]
    for k in range(n):
        for j in range(0,100,100//a[k]):
            if j not in sum:
                sum.append(j)
    sum.sort()
    if sum == list(range(0, 100)):
        print("Yes")
    else:
        print("No")