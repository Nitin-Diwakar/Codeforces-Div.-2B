_,string = input(),input()
ans = 0
preety = set()
for i in string:
    if i.islower():
        preety.add(i)
    else:
        ans = max(ans,len(preety))
        preety.clear();
ans = max(ans,len(preety))
print(ans)