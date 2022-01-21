#AABBB

def castle(n,gaurd,s):
    m = dict()
    me = dict()
    count = 0
    for i in range(len(s)):
        if s[i] not in m:
            m[s[i]] = 1
        else:
            m[s[i]]+=1
        me[s[i]] = 1 
    # print(m)
    # print(me)
    for i in range(len(s)):
        m[s[i]] -=1
        if me[s[i]] == 1:
            count+=1
        if count > gaurd:
            return "YES"
        if m[s[i]] == 0:
            count-=1
        me[s[i]] = 0
    return "NO"


n, gaurd =map(int,input().split())
s = input()
print(castle(n,gaurd,s))
