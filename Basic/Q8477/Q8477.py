A = input()
A = A.split()

list_a = [int (i) for i in A]

sum = 0

for a in range(0,len(list_a)):
    sum += list_a[a]

if sum == 180 :
    print('P')
else:
    print('F')
