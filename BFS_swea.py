# 출발점과 도착점이 주어질 때 두 노드의 최단거리
# 이동거리를 방문배열에 저장하기
T = int(input())


def bfs(s, g):  # 출발점과 도착점이 주어지면 도달 가능여부와 그 거리를 반환
    q = []
    visited[s] = 1
    q.append(s)
    while q:
        cn = q.pop(0)
        if cn == g:  # 주어진 도착점에 도착하면 이동한 거리를 리턴
            return visited[cn]-1
        for i in range(1, V+1):
            if adj_m[cn][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[cn] + 1
    return 0  # 해당 그래프에서 노드 간 이동이 불가하다면 0을 리턴


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_m = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    for i in range(E):
        x, y = map(int, input().split())
        adj_m[x][y] = adj_m[y][x] = 1
    S, G = map(int, input().split())  # 출발점과 도착점
    result = bfs(S, G)
    print(f'#{tc} {result}')


# 이동거리를 방문확인 배열에 저장하지 않고 따로 변수에 저장하여 리턴하는 경우
from collections import deque


def BFS(start, end):
    q = deque([(start, 0)])  # 큐에 시작노드와 초기거리 저장
    while q:
        n, cnt = q.popleft()  # 현재 노드와 거리를 임시 변수에 저장

        if not visited[n]:  # 현재 노드를 방문한 적이 없다면
            visited[n] = 1  # 방문 표시

        for j in arr[n]:  # 인접 노드에 대해
            if not visited[j] and j == end:  # 아직 방문하지 않았고 도착점이라면
                return cnt + 1
            elif not visited[j]:  # 아직 방문하지 않았지만 도착점이 아니라면
                q.append((j, cnt + 1))
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]  # 인접 리스트 초기화
    visited = [0] * (V+1)
    for i in range(E):  # 인접 리스트 채우기
        n1, n2 = map(int, input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)
    S, G = map(int, input().split())
    print(f'#{tc} {BFS(S, G)}')