from math import gcd

a,b,x,y = map(int,input().split())
n = gcd(x,y)
x//=n
y//=n
print(min(a//x,b//y))