limak, bob = map(int, input().split())
p = 0
while limak <= bob:
    limak *= 3
    bob *= 2
    p += 1

print (p)
