N = (int)(input())

word_list = []
for A in range(0,N):
    word_list.append(input())

tmp = list(set(word_list))
answer = sorted(tmp, key=lambda x: (len(x), x))  # key=lambda x:(len(x), x) �� ���̷� ������ �Ŀ� �ڵ����� ���������� �����ϴ� ��

for i in range(0,len(answer)):
    print(answer[i])
