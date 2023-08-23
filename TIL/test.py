# 실제 IM형 기출
T = int(input())

for tc in range(1, T + 1):
    N, P = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def bomb(y, x):
        dir_y, dir_x = y, x
        virus = board[dir_y][dir_x]
        for i, j in delta:
            for k in range(1, P + 1):
                if 0 <= dir_y + k * i < N and 0 <= dir_x + k * j < N:
                    virus += board[dir_y + k * i][dir_x + k * j]
        return virus

    for i in range(N):
        for j in range(N):
            if max_v < bomb(i, j):
                max_v = bomb(i, j)

    print(f'#{tc} {max_v}')