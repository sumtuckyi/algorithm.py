def bfs():
    q = []
    idx = 0
    for i in range(1, N+1):  # N개의 정점에 대해
        if not visited[i]:
            idx += 1
            q.append(i)
            visited[i] = idx
            while q:
                cn = q.pop(0)
                for j in range(1, N+1):
                    if adj_m[cn][j] and visited[j] == 0:
                        q.append(j)
                        visited[j] = idx


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj_m = [[0] * (N + 1) for _ in range(N+1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        x, y = map(int, input().split())
        adj_m[x][y] = adj_m[y][x] = 1
    bfs()
    print(f'#{tc} {max(visited)}')