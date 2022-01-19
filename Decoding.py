
size,word = int(input()),list(input())
result = ""
list1 = []
while size != 0:
    if size%2 == 1:
        list1.append(word[0])
    else:
        list1.insert(0,word[0])
    word.pop(0)
    size= len(word)
print("".join(list1))
       
