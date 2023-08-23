T = int(input())


def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


for tc in range(1, T + 1):
    E, N = map(int, input().split())  # 간선의 수와 루트 노드
    arr = list(map(int, input().split()))
    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    cnt = 0
    # 트리 구조 표현하기
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    preorder(N)
    print(f'#{tc} {cnt}')

#
def sub_tree(node): # node를 루트로 하는 서브트리의 노드의 수를 구하는 함수
    global cnt
    for i in range(2):  # 왼쪽 자식(0), 오른쪽 자식(1)
        if tree[i][node]:  # 해당 노드의 자식이 있다면
            cnt += 1
            n = tree[i][node]  # 자식 노드의 번호
            sub_tree(n)  # 자식 노드에 대해 재귀호출
    

    for tc in range(1, T + 1):
        E, N = map(int, input().split())
        temp = input().split()
        # 이진 트리 초기화(노드번호는 1부터 E+1번까지 존재)
        tree = [[0 for _ in range(E+2)] for _ in range(2)]
        for i in range(E):
            p_node = int(temp[2*i])
            c_node = int(temp[2*i+1])
            if tree[0][p_node] == 0:
                tree[0][p_node] = c_node
            else:
                tree[1][p_node] = c_node
        cnt = 1
        sub_tree(N)
        print(f'#{tc} {cnt}')