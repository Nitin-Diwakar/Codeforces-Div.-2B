k = int(input())
if k > 36:
    print(-1)
else:
    while k > 0:
        if k >=2:
            print(8,end="")
            k-=2
        else:
            print(9,end="")
            k-=1
    print()
    