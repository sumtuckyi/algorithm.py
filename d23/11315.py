# 오목
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    result = "NO"


    def check_direction(y, x, dy, dx):
        cnt = 0
        while 0 <= y < N and 0 <= x < N:
            if board[y][x] == 'o':
                cnt += 1
                if cnt == 5:
                    return True
            else:
                cnt = 0
            y += dy
            x += dx
        return False


    # 행 탐색
    for i in range(N):
        if check_direction(i, 0, 0, 1):
            result = "YES"
            break

    # 열 탐색
    for i in range(N):
        if check_direction(0, i, 1, 0):
            result = "YES"
            break

    # 대각선 탐색(우하향)
    for i in range(N):
        if check_direction(i, 0, 1, 1):
            result = "YES"
            break
    for i in range(1, N):
        if check_direction(0, i, 1, 1):
            result = "YES"
            break

    # 대각선 탐색(우상향)
    for i in range(N):
        if check_direction(i, 0, -1, 1):
            result = "YES"
            break
    for i in range(1, N - 1):
        if check_direction(N - 1, i, -1, 1):
            result = "YES"
            break

    print(f'#{tc} {result}')

# 다른 풀이
def omok():
    # 양 대각선과 가로 세로 방향으로 각각 탐색
    dy = [1, 0, 1, -1]
    dx = [0, 1, 1, 1]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':
                for dir in range(4):
                    ny, nx = y, x  # 탐색 기준점
                    cnt = 0
                    while 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 'o':  # 탐색하려는 칸이 보드 내에 있고 돌이 있는 칸인 한
                        cnt += 1
                        # 다음 위치로 이동
                        ny += dy[dir]
                        nx += dx[dir]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

    print(f'#{tc} {omok()}')