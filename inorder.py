# 완전 이진 트리 탐색하기


# def inorder(n):
#     global ans
#     if n:
#         inorder(ch1[n])
#         ans += tk[n]
#         inorder(ch2[n])
#     return ans


def inorder2(p, N):  # N은 완전 이진 트리의 마지막 정점
    # global ans
    if p <= N:
        inorder2(p*2, N)
        print(tk[p], end='')
        # ans += tk[p]
        inorder2(p*2+1, N)
    return ans


for tc in range(1, 10+1):
    N = int(input())  # 정점의 수
    # 부모노드를 인덱스로 사용
    # ch1 = [0]*(N+1)
    # ch2 = [0]*(N+1)
    tk = [0]*(N+1)  # 정점의 문자열 저장
    ans = ''
    # 간선정보 저장
    for i in range(1, N+1):
        row = list(map(lambda c: int(c) if c.isdigit() else c, input().split()))  # 정점 정보
        tk[i] = row[1]
        # 완전 이진 트리이므로 왼쪽 자식 노드와 오른쪽 자식 노드의 인덱스가 규칙성을 띄므로 따로 저장할 필요 없음
        # if len(row) == 3:
        #     ch1[row[0]] = int(row[2])
        # elif len(row) == 4:
        #     ch1[row[0]] = int(row[2])
        #     ch2[row[0]] = int(row[3])


    # 정점번호는 항상 1(완전 이진 트리)
    print(f'#{tc} ', end='')
    inorder2(1, N)
    print()