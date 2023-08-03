# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     array = list(map(int, input().split()))
#     sorted_array = sorted(array, reverse= True)
#
#     result = []
#     for i, j in zip(range(0, 4 + 1), range(len(array) - 1, len(array) - 6, -1)):
#         result.append(sorted_array[i])
#         result.append(sorted_array[j])
#
#     print(f'#{tc}', *result)


# 다른 풀이
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []

    while len(numbers) > 0:
        max_value = max(numbers)
        result.append(max_value)
        numbers.remove(max_value)

        min_value = min(numbers)
        result.append(min_value)
        numbers.remove(min_value)

    print(f'#{tc}', *result[:10])