n=int(input())
s=input()
o=[s[0]]
for i in range(1,len(s)):
    if o[-1]!=s[i]:
        o.append(s[i])
print (n-len(o))
