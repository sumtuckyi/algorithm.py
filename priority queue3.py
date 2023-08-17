'''
우선순위 큐를 이용하여 최소비교횟수 구하기
비교횟수를 최소한으로 줄이려면 합친 정수와 남은 정수 전체에서 가장 작은 두 값을 골라야 한다.
한 번의 비교가 끝날 때마다 가장 작은 두 값이 달라질 수 있다.
최솟값이 갱신되며 이를 낮은 시간복잡도로 찾기 위해서는 우선순위 큐를 활용할 수 있다.
'''


import heapq
N = int(input())  # 정수의 수

card = list(int(input()) for _ in range(N))
heapq.heapify(card)  # 리스트를 힙으로 변환
ans = 0  # 출력해야할 최솟값

# N=1인 경우에는 비교가 불가하므로 0이 출력되어야 함(반복문이 수행되면 안 됨)
# 리스트의 길이가 1이되는 경우에는 반복문 수행 안 함
# (2개 이상의 정수를 받은 경우라면 모든 연산이 끝난 후이고 1개의 정수인 경우라면 아에 연산을 수행 안 함)
while len(card) != 1:
    first = heapq.heappop(card)  # 힙에서 가장 작은 값을 삭제하고 반환(비어있으면 IndexError 발생)
    second = heapq.heappop(card)
    total = first + second
    ans += total  # 카드를 더할 때마다 집계됨
    heapq.heappush(card, total)  # 합친 값을 우선순위 큐에 넣음
    print(card)

print(ans)