#슬라이딩 윈도우
'''
주로 리스트와 같은 시퀀스 타입에서 일정 크기의 '윈도우'를 정한 다음
그 윈도우를 데이터의 처음부터 끝까지 움직이며 문제를 해결한다.
'''
# 예제 - n개의 정수를 입력받고, 연속된 m개의 정수들의 합을 구할 때, 그 최댓값은 얼마인가?
# (2 <= m, n <= 100,000)

'''
input
10 2
3 -2 -4 -9 0 3 7 13 8 -3
output 
21
'''


N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
max_v = 0
# 첫번째 구간
for i in range(M):
    result += numbers[i]
    max_v = result
for i in range(N - M):
    result += numbers[i+M]
    result -= numbers[i]
    if result > max_v:
        max_v = result
print(f'{tc} {max_v}')

# 큐 이용하여 구현하기
# 큐의 길이가 m인지 확인하여 m이면 더하고 그 값을 리스트에 저장한다.
# 그러고 나서 leftpop()하고 다음 순서의 수를 큐에 추가한다.

from collections import deque
q = deque()
T = int(input())
for tc in range(1, T + 1):
    N, W = map(int, input().split())
    scores = list(map(int, input().split()))
    # start, end = 0, 0
    result = []
    coords = []
    for i in range(N):
        if not q or len(q) < W:
            q.append(scores[i])
            print(scores[i])
        while q and len(q) == W:
            result.append(sum(q))
            coords.append((i-(W-1), i))
            q.popleft()
    print(scores)
    print(result, coords)
    # print(f'#{tc} {max(result)}')

# 슬라이딩 윈도우 실습 - 예제
T = int(input())
for tc in range(1, T + 1):
    N, W = map(int, input().split())
    scores = list(map(int, input().split()))

    result = 0
    max_v = float('-inf')
    max_idx = 0  # 첫번째 윈도우가 최댓값인 경우 출력
    for i in range(W):  # 첫번째 윈도우의 경우
        result += scores[i]
        max_v = result
    for i in range(N - W):
        # 다음구간으로 이동
        result += scores[i+W]
        result -= scores[i]
        if result > max_v:  # 최댓값을 갱신(큰 경우만)
            max_v = result
            max_idx = i + 1  # 최댓값 구간의 시작구간

    print(f'#{tc} {max_idx} {max_idx+(W-1)} {max_v}')




#투 포인터
'''
주로 리스트와 같은 시퀀스 타입에서 두 개의 포인터를 사용하여 문제를 해결하는 방법
'''

#예제 - 1부터 10000까지의 n개의 자연수 중에서 연속된 숫자를 더했을 때 합이 m이 되는 경우는 총 몇 가지인가?
# (연속된 숫자의 길이에 대해서는 제한 없음, 1부터 n까지 가능)
'''
input
10 5
1 2 3 4 2 5 3 1 1 2

outout 
3
'''
# 예제의 경우 시작점의 포인터와 끝점의 포인터를 따로 둔다.
# 시작점은 0부터 n이고, 끝점 역시 0부터 n까지 이동한다. 끝점은 시작점보다 크거나 같다(같은 경우는 길이가 1)
# (0, 0) -> (0, 1), (0, 2),...,(0, n) 이 하나의 주기
# (1, 1) -> (1, 2), (1, 3),...,(1, n)
# (2, 2) -> (2, 3), (2, 4),...,(2, n)
# (n, n)

# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
# cnt = 0
# for i in range(n+1):
#     for j in range(i, n):
#         if sum(numbers[i:j+1]) == m:  # 시간복잡도 때문에 지양
#             cnt += 1
# print(cnt)

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
high, low = 0, 0  # 투 포인터
while True:
    if sum >= m or high == n:  # 합이 타겟보다 크거나 같다면
        # 범위 좁히기(시작 인덱스 증가)
        sum -= numbers[low]
        low += 1
    elif sum < m:  # 합이 타겟보다 작다면
        # 범위 넓히기(끝 인덱스 증가)
        sum += numbers[high]
        high += 1
    if sum == m:  # 합이 타겟과 같다면
        cnt += 1
    if low == n:  # low 인덱스가 리스트 끝에 도착하면(모든 범위를 다 탐색한 것이므로)
        break  # 반복문 종료
print(cnt)