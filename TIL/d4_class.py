T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    K = int(input())
    max_v = 0

    delta = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

    def skil(y, x):
        dir_y, dir_x = y, x
        monsters = 0
        for i, j in delta:
            for k in range(1, K + 1):
                if 0 <= dir_y + i * k < N and 0 <= dir_x + j * k < N:
                    monsters += board[dir_y + i * k][dir_x + j * k]
        return monsters

    for i in range(N):
        for j in range(N):
            if max_v < skil(i, j):
                max_v = skil(i, j)


    print(max_v)