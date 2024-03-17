import math

N = (int)(input())

K = [int(k) for k in input().split()]

def ceil_2multi(N):
    tmp = 0
    while ((N/2) !=0):
        tmp += 1
        N = (int)(N/2)
    return tmp 

Upper = ceil_2multi(N)
init_number = (2 ** Upper)

