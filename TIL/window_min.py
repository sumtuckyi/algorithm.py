# deque를 이용하여 정렬없이 최솟값 구하기 - sliding window
from collections import deque

N, L = map(int, input().split())
now = list(map(int, input().split()))

mydeque = deque()

for i in range(N):
    # 덱의 가장 마지막 데이터와 덱에 추가하려는 데이터의 값을 비교
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    if len(mydeque) >= 1 and mydeque[0][1] <= i - L:
         mydeque.popleft()
    mydeque.append((now[i], i))
    print(mydeque[0][0], end=' ')
