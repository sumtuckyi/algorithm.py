# BFS
'''
그래프 탐색 시에 큐를 이용하여 현재 정점에서 가장 가까운 정점부터 순차적으로 탐색한다.
0. visited배열과 queue생성
1. 탐색할 정점을 큐에 넣으면서
2. 방문 여부를 표시(이미 큐에 넣었음을 의미)
해주면 중복 삽입을 방지할 수 있다.
큐의 특성상 먼저 삽입된 순서대로 탐색이 이루어진다.
'''

# 인접리스트를 이용하기
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, V):
    visited = [0] * (V+1)
    q = []
    q.append(s)
    visited[s] = 1
    while q:  # 큐에 정점이 남아있으면 즉, front != rear이면
        cn = q.pop(0)
        print(cn)  # 방문한 정점에서 할 일
        for i in adj_l[cn]:  # 방문한 정점의 인접리스트를 탐색하면서
            if visited[i] == 0:  # 아직 방문하지 않은 정점이 있다면
                q.append(i)  # 큐에 추가하면서
                visited[i] = visited[cn] + 1  # 방문했음을 표시

V, E = map(int, input().split())  #V는 정점의 개수, E는 간선의 개수
adj_l = [[] for _ in range(V+1)]
arr = list(map(int, input().split()))
# 인접리스트 채우기(인접리스트는 입력값에 따라 오름차순으로 채워지지 않을 수 있음)
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
bfs(2, 7)
