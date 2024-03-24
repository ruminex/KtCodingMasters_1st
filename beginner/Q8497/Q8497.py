N = [int(x) for x in input().split()]

dist = abs(N[0] - N[1])
quo = (int)(dist/3)
mod = (dist%3)

if(mod == 0):
    print(quo)
elif(mod == 1):
    print(quo+3)
elif(mod == 2):
    print(quo+2)