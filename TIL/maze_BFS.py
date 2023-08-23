# 0은 이동할 수 없는 칸을 나타낸다.

from collections import deque

N, M = map(int, input().split())  # 행과 열의 수
maze = [list(map(int, input())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()  # 큐에 탐색할 지점을 넣고 탐색이 완료되면 전단부터 삭제
q.append((0, 0))  # 미로의 시작점, 시작점의 방문여부는 따로 체크하지 않음


def bfs():
    while q:
        x, y = q.popleft()  # 큐의 전단에서 좌표를 삭제하고 임시변수에 저장(큐에는 항상 한 개의 좌표만)
        for k in range(len(d)):  # 상하좌우 탐색
            dx = x + d[k][0]
            dy = y + d[k][1]
            if 0 <= dx < N and 0 <= dy < M:  # 탐색 지점이 미로의 범위 내에 있는 경우
                if maze[dx][dy] == 1:  # 막혀있지 않다면
                    maze[dx][dy] = maze[x][y] + 1  # 바로 전의 칸의 값에 1을 더해준다.(바로 전의 칸의 값은 이동횟수를 의미)
                    q.append((dx, dy))  # 현재 정점에서 갈 수 있는 정점 중 조건을 만족하는 정점만 큐에 순차적으로 삽입


maze[0][0] = 1  # 출발점도 이동횟수에 포함
bfs()
print(maze[N-1][M-1])  # 도착점의 값

