N = input().split()

name_list = input().split()

files = (int)(N[0])
target = N[1]
for i in range(0, files):
    if(target == name_list[i]):
        print(i+1)


