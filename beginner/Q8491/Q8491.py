Init = [int(x) for x in input().split()] #����Ʈ ��������� ���

Numbers = [int(N) for N in input().split()] #����Ʈ ��������� ���

Find_key = Init[1]
answer = -1

for i in range(Init[0]):
    if(Numbers[i] == Find_key):
        answer = (i+1)
        break


print(answer)    