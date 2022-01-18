#Keyboard layout
a = list(input())
b  = list(input())
isomorphic = dict(zip(a,b))
string = list(input())
result = []
for i in string:
    if i.lower() in isomorphic and i.islower():
        result.append(isomorphic[i.lower()])
    elif i.lower() in isomorphic and i.isupper():
        result.append((isomorphic[i.lower()]).upper())
    else:
        result.append(i)
print("".join(result))
