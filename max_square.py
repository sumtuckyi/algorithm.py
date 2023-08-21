T = int(input())


def max_area(x, y):
    global max_v, cnt
    num = board[x][y]  # 찾을 목표값

    for i in range(N - x):
        for j in range(N - y):
            dx = x + i
            dy = y + j
            if board[dx][dy] == num:  # 목표값과 동일한 경우
                area = (dx-x+1)*(dy-y+1)  # 면적을 계산
                if max_v < area:
                    max_v = area
                    cnt = 1
                elif max_v == area:
                    cnt += 1


for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split()))for _ in range(N)]
    areas = []
    max_v = -1
    cnt = 0
    for i in range(N):
        for j in range(N):
            max_area(i, j)
    print(f'#{tc} {cnt}')