# 우선순위 큐 : 데이터가 우선순위에 따라 저장되며,
# 일반적인 큐와 달리 우선순위가 높은 것부터 출력된다.
# 힙 : 우선순위 큐를 구현하는 트리 기반의 자료구조
'''
heapq.heappush(heap, item) : 최소힙을 유지하면서 item을 heap에 푸시
heapq.heappop(heap) : 최소힙을 유지하면서, heap에서 가장 작은 값을 삭제하고 반환.
(힙이 비어있으면 IndexError가 발생)
pop하지 않고 가장 작은 항목에 접근하려면 heap[0]를 사용함.
heapq.heappushpop(heap, item) : heap에 item을 푸시한 다음 가장 작은 항목을 삭제하고 반환.
heapq.heapify(list) : list를 힙으로 변환
heapq.heapreplace(heap, item) : heap에서 가장 작은 항목을 삭제하고 반환하며, 그 다음에 새로운 item을 푸시한다.
'''
# 다른 풀이법으로 풀어보기



#
import heapq
N = int(input())
K = list(map(int, input().split()))  # 수열 중 몇 번째 원소를 출력할 것인지
ugly = []
heap = [1]
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)  # 1, 2, 3, 5를 최소힙에 푸시


while len(ugly) < max(K):  # 출력해야할 원소 중 가장 마지막 순서의 원소까지만 어글리넘버 생성
    n = heapq.heappop(heap)  # 힙에서 최솟값 출력(처음에는 1)
    if n not in ugly:  # 이미 생성된 어글리넘버가 아닐 경우에만
        ugly.append(n)  # 어글리 넘버 생성
        heapq.heappush(heap, n*2)  # 생성된 어글리 넘버에 2를 곱해주기
        heapq.heappush(heap, n*3)
        heapq.heappush(heap, n*5)

for i in K:
    print(ugly[i-1], end=' ')


# 5177문
# import heapq  # 기본적으로 최소힙
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     tree = []
#     number = map(int, input().split())
#     for num in number:
#         heapq.heappush(tree, num)  # 최소힙(트리)에 데이터를 추가
#     sum_v = 0
#     N = len(tree) // 2
#     while N:
#         sum_v += tree[N-1]
#         N //= 2
#     print(f'#{tc} {sum_v}')


