n,t =map(int, input().split())
fence = list(map(int, input().split()))
for i in range(1,n):
    fence[i]+=fence[i-1]
print(fence[n-t])