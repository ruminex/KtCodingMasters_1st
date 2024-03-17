N = (int)(input())

count = 0

if(N>2):
    for A in range(2, (N+1)):
        count += 1
        for B in range(2, A):
            if(A%B == 0):
                count -= 1
                break

if  (N==1):
    print(0)
elif(N==2):
    print(1)
else:
    print(count)            