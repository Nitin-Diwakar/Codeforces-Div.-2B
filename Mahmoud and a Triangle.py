n,segment = int(input()), list(map(int,input().split()))
yes = 0;
segment.sort();
for i in range(2,n):
    if segment[i-1]+segment[i-2] > segment[i]:
        yes = 1;
        break;
if yes:
    print("YES")
else:
    print("NO")
    