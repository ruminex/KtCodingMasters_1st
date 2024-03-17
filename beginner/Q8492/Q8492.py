Init_list = [1,2]

N = (int)(input())

if(N==1):
    print(1)
elif(N==52):
    print(2)
else:
    for i in range(0,N-2):
        Init_list.append(Init_list[0] + Init_list[1])
        Init_list.pop(0)
    print((Init_list[1]%796796))