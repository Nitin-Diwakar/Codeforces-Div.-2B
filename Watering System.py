from itertools import count


n,A,B = map(int,input().split())
size = list(map(int,input().split()))
total = sum(size)
first = size[0]
size[1:].sort()
count = 0
for i in range(n-1,0,-1):
    if (first*A//total) >= B:
        break
    total-=size[i]
    count+=1
print(count)