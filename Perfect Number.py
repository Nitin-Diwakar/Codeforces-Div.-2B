n = int(input())
count = 0
for i in range(0,10000):
    temp = i
    ans = 0
    while(temp):
        x = temp%10
        ans+=x
        temp/=10
    if ans == 10:
        count+=1
    if count == n:
        print(i)
        break