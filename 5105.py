# T = int(input())
#
#
# def maze():
#     global cnt, found, coord
#     while q:
#         x, y = q.pop(0)  # 큐 전단의 좌표에서 탐색 시작
#         # 우하상좌 순으로 탐색
#         for k in range(4):
#             dx = x+d[k][0]
#             dy = y+d[k][1]
#             if 0 <= dx < N and 0 <= dy < N:  # 범위 안에 있고
#                 if board[dx][dy] == 3:  # 탐색 시작점이 도착점인 경우 리턴
#                     found = True
#                     coord = x, y
#                     return
#                 if board[dx][dy] == 0:  # 아직 방문하지 않았으면서 벽이 아니라면
#                     board[dx][dy] = -1
#                     check[dx][dy] = check[x][y] + 1  # 방문하고 표시
#                     q.append((dx, dy))  # 큐에 삽입한 순서대로 탐색 시작
#                     maze()
#
#
# for tc in range(1, T + 1):
#     N = int(input())
#     board = [list(map(int, input())) for _ in range(N)]
#     check = [[0 for _ in range(N)] for _ in range(N)]
#     d = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 우하상좌
#     cnt = 0  # 이동한 칸의 수
#     q = []
#     coord = (0, 0)
#     found = False
#     for i in range(N):  # 시작점 찾기
#         for j in range(N):
#             if board[i][j] == 2:
#                 q.append((i, j))
#                 check[i][j] = 0
#                 maze()
#     ans = check[coord[0]][coord[1]] if found else 0
#     print(f'#{tc} {ans}')

# 다른 풀이
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                return i, j

def bfs(y, x):
    queue = []
    queue.append((y, x))  # 시작 위치 큐에 추가
    visited[y][x] = 1  # 시작 위치 방문 표시
    while queue:
        cy, cx = queue.pop()
        # 도착 위치면 거리 반환
        if arr[cy][cx] == '3':
            return visited[cy][cx] - 2  # 시작과 끝지점은 제외
        for dy, dx in direction:  # 시작 위치를 기준으로 상하좌우 탐색
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N:
                # 아직 방문하지 않았고 벽이 아닌 경우라면
                if arr[ny][nx] != '1' and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append((ny, nx))
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    si, sj = start()
    print(f'#{tc} {bfs(si, sj)}')