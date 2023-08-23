# 풍선팡
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    max_v = 0
    def pang(y, x):
        dir_y, dir_x = y, x
        total = board[dir_y][dir_x]  # 여기서는 기준점의 값이 폭발 범위
        for i, j in delta:
            for k in range(1, total + 1):
                if 0 <= dir_y + i * k < N and 0 <= dir_x + j * k < M:
                    total += board[dir_y + i * k][dir_x + j * k]
                else:
                    break
        return total


    for i in range(N):
        for j in range(M):
            if max_v < pang(i, j):
                max_v = pang(i, j)

    print(f'#{tc} {max_v}')

