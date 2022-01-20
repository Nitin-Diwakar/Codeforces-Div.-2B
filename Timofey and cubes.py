n = int(input())
array = list(map(str,input().split()))

for i in range(0,n//2,2):
    array[i],array[(n-(i+1)+1)-1] = array[(n-(i+1)+1)-1], array[i]
    # print(array)
print(" ".join(array))