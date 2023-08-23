#DFS 실습
# input
'''
RKFCBICM
0 1 1 1 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
'''
# output
'''
RKBIFCCM
'''
# stack으로 그래프를 DFS
S = input()
adj_m = [list(map(int, input().split())) for _ in range(len(S))]


def dfs(n, V, adf_m):  # n에서 시작하여 V개의 정점을 탐색
    stack = [] # 갈림길을 저장
    path = []
    visited = [0]*V # 갔던 노드를 다시 탐색하지 않기 위해 체크
    visited[n] = 1 # 시작점 방문 체크
    path.append(S[n])
    while True:
        for i in range(0, V):
            if adf_m[n][i] == 1 and visited[i] == 0:  # 시작점에 인접해있고 아직 방문하지 않은 경우
                stack.append(n)
                n = i # 해당 노드를 새로운 시작점으로 삼고
                visited[i] = 1
                path.append(S[n])
                break # 인접노드 찾는 것을 중단
        else:  # 시작접 인접 노드 중 방문하지 않은 노드가 없다면
            if stack:
                n = stack.pop() # 새로운 시작점
            else:
                break
    print(*path, sep='')



dfs(0, len(S), adj_m) # DFS탐색 결과 출력

# DFS를 재귀함수로 구현
# lst = list(input())
# N = len(lst)
# adj = [list(map(int, input().split())) for _ in range(N)]  # 인접행렬이 입력값으로 주어질 때
# visited = [False for _ in range(N)]
#
# def DFS(v):  # 몇 번째 노드부터 탐색을 시작할지 인자로 전달
#     print(lst[v], end='')  # 현재 방문한 노드 출력
#     visited[v] = True
#
#     for i in range(N):  # 노드의 개수만큼 탐색
#         if adj[v][i] and not visited[i]:
#             DFS(i)
#
# DFS(0)