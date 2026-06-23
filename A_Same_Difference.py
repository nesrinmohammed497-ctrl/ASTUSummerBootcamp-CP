t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    last = s[-1]
    count = 0

    for i in range(n-1, -1, -1):
        if s[i] == last:
            count += 1
        else:
            continue

    print(n - count)