# 완전 이진트리 구현

def BST(n):
    global node
    if n <= N:  # N은 전체 노드의 수
        BST(2*n)  # 왼쪽 자식 노드로 이동
        tree[n] = node
        node += 1
        BST(n*2+1)  # 오른쪽 자식 노드로 이동

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for i in range(N+1)]
    node = 1  # 완전 이진트리이므로 루트 번호는 1이다.
    BST(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')