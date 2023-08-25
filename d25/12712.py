T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    plus_d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cross_d = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    max_fly = 0

    def catch_fly(y, x, delta):  # 인자로 받은 좌표를 기준으로 살충제를 뿌렸을 때 잡을 수 있는 파리의 수를 반환함
        dir_y, dir_x = y, x
        total = board[dir_y][dir_x]
        for i, j in delta:
            for h in range(1, M):
                dir_y, dir_x = y + h * i, x + h * j
                if 0 <= dir_y < N and 0 <= dir_x < N:
                    total += board[dir_y][dir_x]
        return total


    for i in range(N):
        for j in range(N):
            if max_fly < catch_fly(i, j, plus_d):
                max_fly = catch_fly(i, j, plus_d)

    for i in range(N):
        for j in range(N):
            if max_fly < catch_fly(i, j, cross_d):
                max_fly = catch_fly(i, j, cross_d)

    print(f'#{tc} {max_fly}')