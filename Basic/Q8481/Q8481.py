IQ_dict = {}

N = (int)(input())

for i in range(0,N):
    tmp = input().split()
    name = tmp[0]
    score = tmp[1]
    IQ_dict[name] = (int)(score)


top_students = list(IQ_dict.items())

print(top_students)
top_students.sort(key=lambda x: (-x[1], list(IQ_dict.keys()).index(x[0])))
print(top_students)
# for i in range(min(3, len(top_students))):
    # print(top_students[i][0])