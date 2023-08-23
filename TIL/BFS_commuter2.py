from collections import deque

def bfs(s):
    q = deque([s])
    visited[s] = 1
    while q:
        cn = q.popleft()
        for i in range(1, N+1):
            # 현재 정점에서 인접해 있고 방문한 적이 없으며 화재 발생지역이 아닌 경우
            if adj_m[cn][i] == 1 and not visited[i] and i != T:
                q.append(i)
                if i == N: # 도착지점인 경우
                    return visited[cn]
                else:  # 도착지점은 아닌 경우
                    visited[i] = visited[cn] + 1
    return -1

N, M = map(int, input().split())  # 정점의 수와 간선의 수
adj_m = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):  # 인접배열 채우기
    x, y = map(int, input().split())
    adj_m[x][y] = adj_m[y][x] = 1
T = int(input())  # 화재 발생지점
# 1에서 출발하여 마지막 정점인 N에 도착하려 하는 경우의 최소환승횟수를 리턴

print(bfs(1))