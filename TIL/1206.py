# 조망권 확보 세대수
T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    for b in range(2, N - 2):
        max_v = 0
        l1, l2, r1, r2 = arr[b - 2], arr[b - 1], arr[b + 2], arr[b + 1]
        new_list = [l1, l2, r1, r2]
        if l1 < arr[b] and l2 < arr[b] and r1 < arr[b] and r2 < arr[b]:
            for i in new_list:
                if i > max_v:
                    max_v = i
            result += (arr[b] - max_v)
    print(f'#{tc} {result}')
