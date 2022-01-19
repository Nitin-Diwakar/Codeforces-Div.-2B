n,l,r = map(int,input().split())


# for minimum
mnSum = 0
i = 0
count_min = 0
while count_min < l:
    mnSum+=(2**i)
    i+=1
    count_min+=1
mnSum = mnSum + (n-l)
print(mnSum,end=" ")
# for maximum
mxSum = 0
i = 0
count_max = 0
while count_max < r:
    mxSum+=(2**i)
    i+=1
    count_max+=1
largest_nm = 2**(r-1)
mxSum = mxSum + (n-r)*largest_nm
print(mxSum)