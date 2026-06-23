n, m, a, b = map(int, input().split())
c1=n*a
c2=(n//m)*b + (n % m * a)
c3=(n//m +1)*b 
print(min(c1,c2,c3))
