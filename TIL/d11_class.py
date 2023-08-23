# 연습문제 1
# N = int(input())
# adj_m = [list(map(int, input().split())) for _ in range(N)]
# visited = [0]*N
#
# def DFS(v):
#     visited[v] = 1
#     print(v, end=' ')
#     for j in range(N):
#         if adj_m[v][j] == 1 and visited[j] == 0:
#             DFS(j)
#
# DFS(0)  # 탐색 시작점 전달

# 연습문제 2
# N = int(input())
# adj_m = [list(map(int, input().split())) for _ in range(N)]
# visited = [0]*3  # 현재 경로에서 방문할 노드를 저장할 리스트
#
# def DFS(v, level):
#     global visited
#     visited[level] = str(v)  # 각 레벨마다 방문한 노드를 저장
#     if level == 2:  # 가장 깊은 레벨에 도착한 경우 출력
#         print(' '.join(visited))
#     for i in range(N):
#         if adj_m[v][i] == 1:
#             DFS(i, level + 1)  # 재귀 호출로 인한 작업이 끝나서 다시 돌아오면 바로 이전 레벨에서의 중단점부터 다시 시작
#
#
# DFS(0, 0)

# 연습문제 3
# path = [0] * 10
#
# V = int(input())  # 추적을 시작할 노드
# evid = [-1, 0, 0, 1, 2, 4, 4]
# time_stamp = [8, 3, 5, 6, 8, 9, 10]
#
# def DFS(v, level):  # v번 인덱스에서 추적 시작
#     global path
#     arr_time = time_stamp[v]  # 현 노드에 도착한 시점
#     arr_point = v  # 현재 노드
#     path[level] = {arr_point: arr_time}
#     dest = evid[v]  # 가야할 노드(현 지점 이전의 노드)의 인덱스
#     if dest == -1: # 가야할 노드의 값이 -1이면
#         time = '출발'
#         point = v
#         path[level] = {point: time}
#         return
#     DFS(dest, level + 1) # 가야할 노드에서 동일한 작업 수행
#
# DFS(V, 0)

# 연습문제 4
# V = int(input())  # 추적을 시작할 노드
# evid = [-1, 0, 0, 1, 2, 4, 4]
# time_stamp = [8, 3, 5, 6, 8, 9, 10]
#
#
# def DFS(idx, time):
#     # 재귀함수 종료 조건
#     if evid[idx] == -1:
#         print(f'{idx}번 index(출발)')
#         return
#
#     DFS(evid[idx], time_stamp[idx]) # 현 지점에서 다음 지점으로
#     print(f'{idx}번 index {time_stamp[idx]}시')  # 최초 함수 호출시 입력받은 시작점이 가장 마지막에 출력됨(도착지점, 도착시각)
#
# DFS(V, time_stamp[V])

# 연습문제 5
# N = int(input())  # 컴퓨터의 대수
# l = int(input())
# adj_m = [[0] * (N+1) for _ in range(N+1)]
# for i in range(l):  # 인접배열 채워주기
#     x, y = map(int, input().split())
#     adj_m[x][y] = adj_m[y][x] = 1  # 양방향 간선으로 생각
# cnt = 0
# visited = [0] * (N+1)
#
#
# def DFS2(v):  # v번 컴퓨터가 바이러스에 걸렸을 때 전파되어 바이러스에 걸린 컴퓨터 대수
#     global cnt
#     visited[v] = 1
#     cnt += 1
#     for i in range(N):
#         if adj_m[v][i] == 1 and visited[i] == 0:
#             DFS2(i)
#
#
# DFS2(1)
# print(cnt)

# 다른 풀이
# def DFS2(v):  # v번 컴퓨터가 바이러스에 걸렸을 때 전파되어 바이러스에 걸린 컴퓨터 대수
#     visited[v] = 1
#     for i in range(N):
#         if adj_m[v][i] == 1 and visited[i] == 0:
#             DFS2(i)
#
# print(sum(visited) - 1)  # 최초 감염된 1번 컴퓨터는 제외

# 인접리스트로 해결하기
# N = int(input())  # 컴퓨터의 대수
# l = int(input())
# arr = [[0]*(N+1) for _ in range(N+1)]
# visited = [0] * (N+1)
# cnt = 0
#
# for _ in range(l):
#     c1, c2 = map(int, input().split())
#     arr[c1].append(c2)
#     arr[c2].append(c1)
# visited[1] = 1
#
#
# def DFS3(c1):
#     global cnt
#     for i in arr[c1]:  # c1노드와 인접한 노드에 대해 반복
#         if not visited[i]:
#             visited[i] = 1
#             cnt += 1
#             DFS3(i)
#
# DFS3(1)
# print(cnt)

# 연습문제 6
N, K = map(int, input().split())
V = int(input())
adj_m = [[0] * (N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(K):
    x, y = map(int, input().split())
    adj_m[x][y] = adj_m[y][x] = 1

def preorder(v): # v에서 전위순회 시작
    visited[v] = 1
    print(v, end = ' ')
    for i in range(N, -1, -1):
        if adj_m[v][i] == 1 and not visited[i]:
            preorder(i)

# 오른쪽(즉, 더 큰 쪽 노드 먼저)-> 왼쪽 -> 루트
def postorder(v):
    for i in range(N, 0, -1):  # 큰 번호 우선
        if adj_m[v][i] == 1 and not visited[i]:
            postorder(i)

        else:  # 하위 레벨의 노드가 없는 경우
            if visited[i] != 1:
                print(i, end=' ')
                visited[i] = 1

# preorder(V)
# print()
postorder(V)