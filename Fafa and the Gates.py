
n = int(input())
moves = input()

x=y=coin = 0
for i in range(n-1):
    if moves[i] == 'U':
        y+=1
        # print("Y:",y)
    else:
        x+=1
        # print("X:",x)
    if x==y and moves[i] == moves[i+1]:
        coin+=1
    # n-=1
print(coin)