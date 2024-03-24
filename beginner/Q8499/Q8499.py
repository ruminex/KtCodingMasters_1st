def count_digits(N):

    digit_count = {str(i): 0 for i in range(10)}

    for number in range(1, N + 1):
        for digit in str(number):
            digit_count[digit] += 1

    return digit_count

N = int(input(""))
result = count_digits(N)

# 결과 출력
for digit, count in result.items():
    print(count)