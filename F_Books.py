n, t = map(int, input().split())
a = list(map(int, input().split()))

w = 0
s = 0
o = 0

for i in range(n):
    s += a[i]

    while s > t:
        s -= a[w]
        w += 1

    o = max(o, i - w + 1)

print(o)