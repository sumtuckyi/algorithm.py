# N은 2이상 5000이하

import heapq

N = int(input())
m = list(map(int, input().split()))
heapq.heapify(m)
t = 0 # 최소시간

while len(m) != 1:  # m에 원소가 하나 남을 때까지
    min1 = heapq.heappop(m)
    min2 = heapq.heappop(m)
    temp = min1 + min2
    t += temp
    heapq.heappush(m, temp)

print(t)