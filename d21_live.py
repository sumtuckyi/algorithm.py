# 트리 자료구조
'''
한 개 이상의 노드로 이루어진 유한 집합
노드 중 최상위 노드를 루트라 한다.
조상 노드 - 간선을 따라 루트 노드에 이르는 경로에 있는 모든 노드들
노드의 차수(degree) : 한 노드에 연결된 자식 노드의 수
노드의 높이 : 루트에서 노드에 이르는 간선의 수
'''

'''
이진트리 : 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
포화 이진 트리
완전 이진 트리
편향 이진 트리
'''

'''
입력값
노드 개수 간선 개수(트리 구조에서 간선의 수는 노드의 수보다 1개 적음)
간선정보(ex: 부모 자식) * 간선 개수
포화 이진 트리나 완전 이진 트리가 아닌 이상 루트 노드가 1이라는 보장이 없음
'''


'''
def preorder(T):
    if T:
        visit(T)  # 루트를 처리
        preorder(T.left) # 루트의 왼쪽 서브트리를 처리(재귀 호출이 되면 왼쪽 서브트리의 루트를 처리 -> 왼쪽 서브트리 -> 오른쪽 서브트리 순으로/ 트리 구조 자체가 재귀적 구조)
        preorder(T.right)
'''
# 이진트리의 표현
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

'''
# VLR
def preorder(n):
    if n:  # 존재하는 정점이면
        print(n)  # 루트 처리
        preorder(ch1[n])  # 왼쪽 서브트리로 이동
        preorder(ch2[n])  # 오른쪽 서브트리로 이동

# LVR
def inorder(n):
    if n:
        preorder(ch1[n])
        print(n)
        preorder(ch2[n])

# LRV
def postorder(n):
    if n:
        preorder(ch1[n])
        preorder(ch2[n])
        print(n)

V = int(input())  # 노드의 개수
E = V - 1  # 간선의 개수
arr = list(map(int, input().split()))
# 부모를 인덱스로 자식을 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)
# 자식을 인덱스로 부모를 저장
par = [0]*(V+1)
for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    if ch1[p] == 0:  # 자식 1이 아직 없으면
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

# 실제 루트 찾기(루트가 1이라는 보장이 없음)
root = 1
while par[root] != 0:
    root += 1

# 전위, 중위, 후위 순회 출력
preorder(1)
print()
inorder(1)
print()
postorder(1)


# 트리를 순회하기

# N, K = map(int, input().split())
# V = int(input())
# adj_m = [[0] * (N+1) for _ in range(N+1)]
# visited = [0]*(N+1)
# for i in range(K):
#     x, y = map(int, input().split())
#     adj_m[x][y] = 1


# v에서 전위순회 시작
# 루트 -> 왼쪽 -> 오른쪽
# def preorder(v):
#     visited[v] = 1  # 루트를 처리, 재귀 호출부터는 방문한 노드를 처리
#     print(v, end = ' ')
#     for i in range(N, 0, -1):  # 큰 수일수록 왼쪽에 위치하며 전위순회는 왼쪽 서브트리를 먼저 순회하므로
#         if adj_m[v][i] == 1 and not visited[i]:
#             preorder(i)  # 루트의 왼쪽 서브트리를 처리


# 중위순회
#왼쪽 -> 루트 -> 오른쪽
# def inorder(v):
#     for i in range(N, 0, -1):
#         if adj_m[v][i] == 1 and not visited[i]:
#             print(i, end = ' ')
#             inorder(i)  # 루트의 왼쪽 서브트리를 처리
#             visited[v] = 1  # 루트를 처리


# 후위순회
# 왼쪽 -> 오른쪽 -> 루트
# def postorder(v):
#     for i in range(N, 0, -1):  # 큰 수일수록 왼쪽에 위치하고 후위 순회는 왼쪽 서브트리를 먼저 순회하므로
#         #print(f'{i}번째 인접노드')
#         if adj_m[v][i] == 1 and not visited2[i]: # 하위 노드가 있고 아직 방문하지 않았다면
#             postorder(i)  # 루트의 왼쪽 서브트리를 처리
#     # 마지막에 루트를 처리
#     print(v, end=' ')
#     visited2[v] = 1

#
# visited2 = [0]*(N+1)
# preorder(V)
# print()
# postorder(V)