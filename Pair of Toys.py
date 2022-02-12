def solve(n,k):



    if k < n:
        return k//2
    if k//2 > n:
        return 0
    c = (k-1)//2 + 1
    return n-c+1
n,k = map(int,input().split())
print(solve(n,k))
