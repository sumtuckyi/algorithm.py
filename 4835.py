# 구간합 구하기
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    D = [0] * (N + 1)
    arr2 = []
    max_v = 0

    for i in range(1, N):
        D[0] = 0
        D[1] = arr[0]
        D[i + 1] = D[i] + arr[i]

    min_v = D[M]
    for i in range(M, N + 1):

        total = D[i] - D[i - M]
        if total > max_v:
            max_v = total
        if total < min_v:
            min_v = total

    print(f'#{tc} {max_v - min_v}')