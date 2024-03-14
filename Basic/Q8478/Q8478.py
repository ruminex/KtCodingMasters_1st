'''I = input()
I = I.split()

list_i = [int (k) for k in I]

sum = 0
date = 1
A = list_i[0]
B = list_i[1]
N = list_i[2]

while True: 
    sum += A
    if sum == N :
        print(date)
        break 
    sum -= B
    date += 1'''

import math

def days_to_memorize_words(N, A, B):

    total_days = math.ceil((N - B) / (A - B))
    return total_days


I = input().split()
A, B, N = map(int, I)


print(days_to_memorize_words(N, A, B))
