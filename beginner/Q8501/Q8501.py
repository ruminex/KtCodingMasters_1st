N = (int)(input())
answer = 0
K = [int (i) for i in (input().split())]
K.sort()

if(N<3):
    for a in K:
        if(a!=0):
            print(-1)
        else:
            print(0)

            
else:
    if((K[0] != 0) | (K[1] != 0)):
        print(-1)
    else:
        if((sum(K) % 3) !=0):
            print(-1)
        else:
            K.sort(reverse=True)
            for b in range(0,len(K)):
                answer = (answer * 10)
                answer = (answer + K[b])
            print(answer)
        
    