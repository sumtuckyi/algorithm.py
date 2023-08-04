# 최대 최소의 간격
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0
    for i in range(1, N):
        if arr[min_idx] > arr[i]: # 두 값이 같을 때에는 인덱스가 갱신되지 않음
            min_idx = i

    for i in range(1, N):
        if arr[max_idx] <= arr[i]: # 두 값이 같을 때에는 뒤쪽의 인덱스가 할당됨
            max_idx = i

    if max_idx > min_idx:
        print(max_idx - min_idx)
    else:
        print(min_idx - max_idx)
