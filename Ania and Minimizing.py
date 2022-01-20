n,k = map(int,input().split())
s = list(input())

p = 0
while k>0 and p<n:
    if p>0  or p == n-1:
        if s[p] != '0':
            s[p] = '0'
            k -=1
    else:
        if s[p] != '1':
            s[p] = '1'
            k-=1
    p+=1
print("".join(s))