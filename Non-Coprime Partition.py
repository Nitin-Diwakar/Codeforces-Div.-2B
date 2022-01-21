n = int(input())
if n <=2:
    print("No")
else:
    print("Yes")
    s1 = (n+1)//2
    print(1,s1)
    print(n-1,end=" ")
    for i in range(1,n+1):
        if i == s1:
            continue
        print(i,end=" ")