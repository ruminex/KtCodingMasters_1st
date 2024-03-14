N = int(input())

Rimbo = input().split()

list_Rimbo = [int (k) for k in Rimbo]

X = True
for a in range (0, len(list_Rimbo)):
    if(list_Rimbo[a] <= 160):
        print('I' + ' ' + (str)(list_Rimbo[a]))
        X = False
        break

if(X==True):
    print('P')