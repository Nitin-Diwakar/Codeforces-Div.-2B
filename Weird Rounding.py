
n,k = map(str,input().split())
k = int(k)
count = 0
for i in range(len(n)-1,-1,-1):
    if k <= 0:
        break;
    
    if n[i] == '0':
        k-=1
    else:
        count+=1

if k <= 0:
    print(count)
else:
    print(len(n)-1)