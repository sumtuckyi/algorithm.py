# 5177문 - 이진 최소힙 구현하기
# 마지막 노드의 조상 노드의 키값의 합을 구하라


def enq(n):  # 최대힙에 데이터를 삽입하는 함수
    global last
    last += 1
    heap[last] = n
    p = last // 2
    c = last
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 노드의 수
    arr = list(map(int, input().split()))  # 데이터 입력값
    heap = [0 for _ in range(N+1)]
    last = 0
    for i in arr:
        enq(i)
    result = 0
    par = last // 2
    while par > 0:  # 루트 노드까지 조상을 찾아감
        result += heap[par]
        par //= 2
    print(f'#{tc} {result}')


#
import heapq  # 기본적으로 최소힙
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = []
    number = map(int, input().split())
    for num in number:
        heapq.heappush(tree, num)  # 최소힙(트리)에 데이터를 추가
    sum_v = 0
    N = len(tree) // 2
    while N:
        sum_v += tree[N-1]
        N //= 2
    print(f'#{tc} {sum_v}')