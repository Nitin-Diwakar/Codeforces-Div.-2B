n,k = map(int,input().split())
CandiesInBox = 0
CandiesEat = 0
for i in range(1,n+1):
    CandiesInBox+=i
    CandiesEat = CandiesInBox - k
    
    if CandiesInBox >= 0  and i+CandiesEat == n:
        print(CandiesEat)
        break