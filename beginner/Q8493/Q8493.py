N = (int)(input())

word_list = []
for A in range(0,N):
    word_list.append(input())

tmp = list(set(word_list))
answer = sorted(tmp, key=lambda x: (len(x), x))  # key=lambda x:(len(x), x) 가 길이로 정렬한 후에 자동으로 사전식으로 정렬하는 것

for i in range(0,len(answer)):
    print(answer[i])
