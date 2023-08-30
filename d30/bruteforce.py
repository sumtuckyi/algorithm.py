from collections import deque


def search(x, y, total, level):  # 탐색 시작점을 전달
    if level == 2 * (N-1):  # 도착점에 도달하면
        lst.append(total)
        return
    q.append((x, y))
    while q:
        # 기준점 지정
        dx, dy = q.popleft()
        # 오른쪽과 아래쪽 셀에 대해
        for i, j in [(dx, dy+1), (dx+1, dy)]:
            if 0 <= i < N and 0 <= j < N and visited[i][j] == 0:  # 아직 방문하지 않은 경우
                if total + arr[i][j] < min(lst):  # 현재까지의 합이 최솟값보다 작은 경우에만 다음 레벨로
                    visited[i][j] = 1
                    search(i, j, total + arr[i][j], level+1)
                    visited[i][j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    lst = [100000]  # 가능한 경로의 합을 모두 저장
    q = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    search(0, 0, arr[0][0], 0)

    print(f'#{tc} {min(lst)}')

#
dir = [(0, 1), (1, 0)]


def dfs(x, y, sum_v):
    global result
    # 백트래킹, 가지치기(조건이 없으면 시간이 많이 걸림)
    if sum_v >= result:
        return
    if x == N-1 and y == N-1:
        if sum_v < result:
            result = sum_v
        return
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N:
            dfs(nx, ny, sum_v + arr[nx][ny])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    result = float('inf')
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {result}')