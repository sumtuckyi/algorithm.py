# 리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음,
# 지정된 노드 번호의 키값을 구하라


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # 노드의 개수(마지막 노드의 번호), 리프 노드의 개수, 지정된 노드 번호
    h = [0 for _ in range(N+1)]
    leaves = []  # 리프 노드의 번호만 따로 저장
    for _ in range(M):
        leaf, value = map(int, input().split())
        h[leaf] = value
        leaves.append(leaf)

    while leaves:  # 리스트가 빌 때까지
        i = leaves.pop(0)  # 리스트의 첫번째 값을 저장
        if not i % 2:  # 리프 노드의 인덱스가 짝수이면(왼쪽 노드이면)
            if i != N:  # 오른쪽 노드가 있으면
                if h[i+1]:
                    h[i//2] = h[i] + h[i+1]
            else:  # 마지막 노드이면
                h[i//2] = h[i]
            leaves.append(i//2)
        else:  # 꺼낸 노드의 인덱스가 홀수이면(오른쪽 노드이면)
            continue  # 이미 왼쪽 노드의 차례에 계산되었음
    print(h)
    print(f'#{tc} {h[L]}')

#
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    for i in range(N, 0, -1):  # 리프 노드를 인덱스가 큰 순으로 탐색
        if i // 2 > 0:
            tree[i//2] += tree[i]  # 부모 노드에 자식 노드의 값을 더하기
    result = tree[L]
