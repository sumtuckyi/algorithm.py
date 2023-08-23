# deque사용하기
# from collections import deque
#
# q = deque()
# q.extend([i for i in range(1, 10+1)])
#
# for item in q:
#     print(item, end=' ')
# print()
# print(q.popleft())  # 전단의 데이터 삭제
# print(q.pop())  # 후단의 데이터 삭제


#
# from collections import deque
# for _ in range(10):
#     tc = int(input())
#     q = deque()
#     numbers = list(map(int, input().split()))
#     q.extend(numbers)
#     # 숫자 하나라도 0보다 작아지면 암호문 생성 완료
#     idx = 0
#     cnt = -1
#     while True:
#         cnt += 1
#         temp = q.popleft()
#         if cnt % 5 == 0:
#             q.append(temp-1)
#         elif cnt % 5 == 1:
#             q.append(temp-2)
#         elif cnt % 5 == 2:
#             q.append(temp-3)
#         elif cnt % 5 == 3:
#             q.append(temp-4)
#         else:
#             q.append(temp-5)
#         if q[-1] <= 0:
#             q[-1] = 0
#             break
#     print(f'#{tc}', *q)


#
def pw(lst):
    while True:
        # cycle이 반복
        for i in range(1, 6):
            num = lst.pop(0)
            lst.append(num - i)
            if lst[-1] <= 0:
                lst[-1] = 0
                return lst

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    numbers = list(map(int, input().split()))
    result = pw(numbers)
    print(f'#{tc}', *result)