from collections import deque

N, L = map(int, input().split())
now = list(map(int, input().split()))

mydeque = deque()

for i in range(N):
    # 덱의 가장 마지막 데이터와 덱에 추가하려는 데이터의 값을 비교
    while mydeque and mydeque[-1][0] > now[i]:
        pass