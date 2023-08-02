T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    y, x = 0, 0  # 반복을 시작할 지점

    plus_d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cross_d = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    max_fly = 0

    def catch_fly(y, x, delta):

        total = 0
        dir_y, dir_x = y, x
        for i, j in delta:
            total += board[dir_y][dir_x]
            for _ in range(M - 1):
                dir_y, dir_x = y + i, x + j
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

    # def catch_fly(list_x, list_y):
    #     for i in range(N):
    #         for j in range(N):
    #             y, x = i, j
    #             flies = []
    #             cnt = 0
    #             direction = 0
    #             flies.append(board[i][j])  # 기준점 파리 박멸
    #             while True:
    #                 y, x = y + list_y[direction], x + list_x[direction]  # 상->하->좌->우 순서로 이동
    #                 if 0 <= x < N and 0 <= y < N and cnt != M - 1:
    #                     flies.append(board[y][x])
    #                     cnt += 1
    #                 else:
    #                     if direction < 3:
    #                         direction += 1
    #                         y, x = i, j
    #                         cnt = 0
    #                     else:
    #                         break
    #             max_fly.append(sum(flies))
    #     return max(max_fly)
    #
    #
    # a = catch_fly(plus_dx, plus_dy)
    # b = catch_fly(x_dx, x_dy)
    #
    # print(f'#{h + 1} {max(a, b)}')