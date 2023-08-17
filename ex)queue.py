import sys
from collections import deque

N = int(sys.stdin.readline())  # 1부터 N까지의 카드를 입력받음

queue = deque()
# 1부터 N까지의 카드를 큐에 삽입
for i in range(N):
    queue.append(i + 1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())