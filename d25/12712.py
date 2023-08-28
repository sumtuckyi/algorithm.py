T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 보드의 크기, 효과의 범위(기준점 포함)
    board = [list(map(int, input().split())) for _ in range(N)]

    plus_d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cross_d = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    max_fly = 0  #  해당 문제의 경우에는 파리의 수가 양수이므로 0으로 초기화

    def catch_fly(y, x, delta):  # 인자로 받은 좌표를 기준으로 살충제를 뿌렸을 때 잡을 수 있는 파리의 수를 반환함
        dir_y, dir_x = y, x
        total = board[dir_y][dir_x]  # 기준점의 파리 수 
        for i, j in delta:
            for h in range(1, M):  # 범위 만큼 반복
                dir_y, dir_x = y + h * i, x + h * j
                if 0 <= dir_y < N and 0 <= dir_x < N:  # 보드를 벗어나지 않는다면
                    total += board[dir_y][dir_x]
        return total

    # 스프레이를 뿌릴 위치 - '+' 방향
    for i in range(N):
        for j in range(N):
            if max_fly < catch_fly(i, j, plus_d):
                max_fly = catch_fly(i, j, plus_d)
    # 스프레이를 뿌릴 위치 - 대각선 방향
    for i in range(N):
        for j in range(N):
            if max_fly < catch_fly(i, j, cross_d):
                max_fly = catch_fly(i, j, cross_d)

    print(f'#{tc} {max_fly}')
