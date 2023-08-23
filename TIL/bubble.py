# 버블 정렬, O(N^2)
# 인접한 두 요소를 비교하여 큰 값을 오른쪽으로 이동시키는 과정을 반복


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     for i in range(N - 1, 1, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#     print(f'#{tc}', *arr)

numbers = [63, 31, 27, 11, 25]


def bubble(arr):
    for i in range(len(arr)):  # range(5), 하나의 요소가 정렬이 되는 횟수
        for j in range(len(arr) - i - 1):  # j는 비교 대상 중 앞쪽, 비교가 발생하는 횟수(정렬이 하나씩 될 때마다 비교횟수가 1씩 줄어든다.)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


bubble(numbers)