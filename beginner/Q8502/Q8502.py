def count_digit_in_time(N):
    total_seconds = 0

    for hour in range(24):
        for minute in range(60):
            for second in range(60):
                if str(N) in f"{hour:02d}{minute:02d}{second:02d}":
                    total_seconds += 1

    return total_seconds

N = int(input())
result = count_digit_in_time(N)
print(result)