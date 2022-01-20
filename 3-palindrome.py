n = int(input())
for i in range(1,n+1):
    if i%4 == 1 or i%4 == 2:
        print('a',end="")
    elif i%4 == 0 or i%4 == 3:
        print("b",end="")