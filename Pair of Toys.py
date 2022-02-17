# from itertools import combinations,permutations
# # a = [*range(1,10)]
# # print([x for x in permutations(a,2)])

# toys,cost = map(int,input().split())
# a = [*range(1,toys+1)]
# re = 0
# for x in permutations(a,2):
#     if sum(x) == cost:
#         re+=1
# print(re//2)

import math


def solve(toys,cost):
    if cost <= toys:
        return(math.floor(cost/2))
    mn = toys-cost
    mx = toys
    return max(0,math.floor((mn-mx+1)/2))
   
        
toys,cost = map(int,input().split())
print(solve(toys,cost))

