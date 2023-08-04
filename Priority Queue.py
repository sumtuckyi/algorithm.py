import sys
import heapq  # 최소 힙(가장 작은 값이 루트 노드에 위치)
# input() 대신 sys.stdin.readline() 사용

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:  # 입력받은 값이 자연수인 경우에만
        heapq.heappush(heap, (-num))  # 우선순위 큐에 자연수를 추가
    else:
        try:
            print(-1 * heapq.heappop(heap))  # 인자로 받은 힙에서 가장 작은 요소를 반환(즉, 우선순위가 가장 높은 요소), 힙이 비어있을 경우 에러 발생
        except:  # 힙이 비어있어 에러 발생시
            print(0)