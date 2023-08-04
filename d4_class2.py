# IM형
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    areas = []

    def search(y, x):
        for i in range(y, N):
            for j in range(x, N):
                if board[i][j] == board[y][x]:
                    if i == y:
                        areas.append(abs(j-x+1))
                    elif j == x:
                        areas.append(abs(i-y+1))
                    else:
                        areas.append(abs(i-y+1) * abs(j-x+1))


    for i in range(N):
        for j in range(N):
            search(i, j)

    maximum = max(areas)
    result = areas.count(maximum)

    print(f'#{tc} {result}')

# 다른 풀이
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    maxarea = 0
    cnt = 0

    for y in range(N):
        for x in range(N):
            cur = board[y][x]  # 사각형 왼쪽 위의 좌표값

            for ny in range(y, N):
                for nx in range(x, N):
                    if board[ny][nx] == cur:
                        area = (ny - y + 1) * (nx - x + 1)
                        if area > maxarea:
                            maxarea = area
                            cnt = 1
                        elif area == maxarea:  # 최대면적과 동일한 경우가 발생하면 카운트 누적
                            cnt += 1
    print(f'#{tc} {cnt}')