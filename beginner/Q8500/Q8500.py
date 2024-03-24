import math

N = [int (i) for i in input().split()]

combi = math.factorial(N[0]) / (math.factorial(N[1]) * math.factorial(N[0]-N[1]))

print((int)(combi))