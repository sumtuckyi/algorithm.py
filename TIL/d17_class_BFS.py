# 문제 1
def bfs(v):
    q.append(v)  # 시작 노드를 큐에 추가
    visited[v] = 1
    while q:
        v = q.pop(0)  # 큐에서 하나의 노드를 꺼낸 후 출력
        print(v)
        for i in range(N):  # 현재 노드와 연결된 모든 노드를 확인
            if adj_m[v][i] == 1 and visited[i] == 0:  # 연결되어 있고 아직 탐색하지 않았다면
                visited[i] = 1
                q.append(i)  # 해당 노드를 큐에 추가


V = int(input())
N = 6
visited = [0]*(N)
adj_m = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0]
]  # 양방향이므로 방문여부를 체크할 리스트가 필요
q = []
bfs(V)

# 문제2
def bfs(v):
    q.append(v)
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in range(N):
            if adj_m[v][i] == 1:
                q.append(i)


V = int(input())
N = 6
adj_m = [
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]  # 단방향이므로 못 되돌아가기 때문에 방문체크용 리스트가 필요없음
q = []
bfs(V)