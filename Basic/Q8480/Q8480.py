I = []
I.append(int(input()))

count = [0]


def check(N, Size, count):
    while (N[0] >= Size):
        count[0] +=1
        N[0] -= Size

check(I, 50000, count)
check(I, 10000, count)
check(I, 5000, count)
check(I, 1000, count)
check(I, 500, count)
check(I, 100, count)
check(I, 50, count)
check(I, 10, count)

print(count[0])