'''
Union-Find
노드 간의 집합 관계를 빠르게 파악하고 관리해야 하는 경우
union : 그룹을 합치는 함수
find : 연결되어 있는지 확인하는 함수
'''

# 초기화
# 원소의 집합이 하나의 트리
# 각 원소가 속하는 집합의 번호는 루트 노드의 원소
# 그룹을 합치기 전에 두 원소가 같은 집합에 속하는 것은 아닌지 먼저 확인
# 같은 집합인지 확인하기 위해 find함수를 사용
# find함수를 구현하기 위해 모든 자식노드가 부모노드에 대한 정보를 가지고 있도록 한다.

N, Q = map(int, input().split())  # 노드와 쿼리의 개수
# 초기화
par = [0]*(N + 1)
for i in range(1, N + 1):
    par[i] = i  # 처음에 노드 i의 부모는 자기 자신

# find : 해당 노드의 부모 노드를 반환함. 부모노드가 동일 하면 같은 집합임
def find(n):
    if par[n] == n:  # 부모노드가 자기 자신인 경우
        return n
    else:  # 다른 부모노드가 있는 경우
        par[n] = find(par[n]) # 부모노드를 찾아 거슬러 올라감
    return par[n]  # 최종적으로 찾은 부모노드 반환

# union :
def union(a, b):
    if find(a) != find(b):  # 두 노드가 같은 집합에 속하지 않는다면
        par[find(a)] = find(b) # a가 속한 트리를 b의 부분트리로 합친다.
    else:
        return

for i in range(Q):
    uof, n1, n2 = map(int, input().split())
    if uof:  # union 질의인 경우
        union(n1, n2)
    else:  # find 질의인 경우
        if find(n1) == find(n2):  # 같은 그룹이면
            print('YES')
        else:
            print('NO')

#
def find(node):
    if node != root(node):
        root[node] = find(root[node])
    return root[node]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if rank[root_x] > rank[root_y]:
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1

rank = [0] * (N + 1)