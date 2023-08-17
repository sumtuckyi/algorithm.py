T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  #  V개의 노드와 E개의 간선
    adj_m = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬

    # 인접행렬에 간선 정보 저장
    for i in range(E):
        x, y = map(int, input().split())
        adj_m[x][y] = 1  # x가 출발점, y는 도착점
    #print(adj_m)
    start, end = map(int, input().split())  # 경로가 존재하는지 확인할 출발점과 도착점

    def dfs(start, end, V):
        visited = [0] * (V + 1)
        stack = []
        v = start  # 시작점 지정
        visited[v] = 1  # 방문여부 변경
        while True:  # 도착점에 도착하면 반복문을 종료하도록 조건 설정
            for i in range(1, V+1):  # 인접행렬의 1부터 V열까지 미방문 정점이 있는지 탐색
                if adj_m[v][i] == 1 and visited[i] == 0:  # 시작점에서 갈 수 있는 정점이 있을 때
                    stack.append(v)
                    if i == end:  # 해당 노드가 도착점일 경우
                        return 1
                    else:  # 해당 노드가 도착점이 아닌 경우
                        stack.append(i)
                        v = i  # 해당 노드를 새로운 출발점으로 지정
                        visited[v] = 1
                        break
            else: # 현재 시작점에서 인접한 미방문 노드가 없는 경우
                if stack:
                    v = stack.pop()
                else:
                    return 0
    print(f'#{tc} {dfs(start, end, V)}')

#

T = int(input())

def DFS(start, end):
    # 탐색할 노드를 저장할 스택 초기화
    stack = []
    visited = [False] * (V+1)
    stack.append(start)
    # 스택이 비어있으면 반복문 종료
    while stack:
        now = stack.pop()
        visited[now] = True
        for next in range(1, V+1):
            if node[now][next] and not visited[next]:
                stack.append(next)
    if visited[end]:  # 도착점을 방문하였다면
        return 1
    else:
        return 0


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    node = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        node[start][end] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {DFS(S, G)}')