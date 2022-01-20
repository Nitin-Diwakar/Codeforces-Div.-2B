boys = int(input())
girls = int(input())
badges  = int(input())
deck = []
i = 0
for each in range(badges+1):
    a = i
    b = badges-i
    i+=1
    deck.append((a,b))
cnt = 0
for each in deck:
    if each[0]<= boys and each[1] <=girls:
        cnt+=1
print(cnt)