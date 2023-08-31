# 여러개의 번들 > 인원 수 / 여러개의 번들 + 낱개 = 인원 수 / 낱개 = 인원 수
# 인원당 최소 한 병의 술이 있어야 함
# 모두 낱개로 사는 경우가 번들의 최저가보다 저렴한 경우라면 더 이상 고려할 필요 없음
# 그렇지 않다면 번들의 수를 늘려가며 번들과 낱개를 적절하게 섞어서 구매해야함
# 번들을 1개 사는 경우 -> 인원 수 충족여부 확인 -> 인원 수보다 적으면 번들을 추가 / 인원 수보다 많으면 번들 + 낱개의 경우와 비교
# N, M = map(int, input())
# lst = []
# for i in range(M):
#     a, b = map(int, input().split())
#     lst.append((a, b))
#     bundle = N // 6
#     bottle = N % 6
#
#
#
# #
# n, m = map()
# six_min = float('inf')  # 번들의 최저가
# one_min = float('inf')  # 낱개의 최저가
# for _ in range(m):
#     six_cost, one_cost = map(int, input().split())
#     # 입력을 받아서 최솟값을 바로 갱신
#     six_min = min(six_min, six_cost)
#     one_min = min(one_min, one_cost)
#
# if one_min * 6 < six_min:  # 낱개로 사는 것이 가장 저렴한 경우
#     print(one_min * n)
# else:  # 그렇지 않다면 번들과 낱개를 섞어서 사기
#     buy = n // 6  # 번들의 개수
#     n %= 6  # 낱개의 개수
#     if n * one_min > six_min:  # 현 인원을 기준으로 최소한으로 번들을 사고 남은 인원은 낱개로 사는 경우가 번들을 하나 더 추가하는 경우보다 저렴한 경우
#         buy += 1
#     else:  # 번들을 최소한으로 사고 남은 인원 만큼을 낱개로 사는 것이 더 저렴한 경우
#         c = buy * six_min + n * one_min
#
#
# #
# n, L = map(int, input().split())
# leaks = list(map(int, input().split()))
# leaks.sort()
# cnt = 1  # 첫 번째 구멍을 막기 위해 1로 초기화
# cur = leaks[0]
# for i in range(1, n):
#     if leaks[i] - cur < L:  # 다음 구멍을 현재 테이프로 막을 수 있다면
#         continue
#     else:
#         cur = leaks[i]  # 새로운 테이프로 막을 구멍을 갱신
#         cnt += 1  # 사용한 테이프의 개수 갱신


<<<<<<< HEAD
# 회의실 문제
# 동적 프로그래밍 이용 풀이(LIS)
=======
#

>>>>>>> origin/master

N = int(input())
lst = []
dp = [0] * N
for i in range(N):
    s, e = map(int, input().split())
    lst.append((s, e))
# 시작 시간이 이른 순으로 정렬
lst.sort(key=lambda x: x[0])
# dp배열 채우기
for i in range(N):
    s, e = lst[i]  # 기준점
    temp = []
    for j in range(0, i):  # 기준점보다 시작시간이 이른 경우만 고려
        if lst[j][1] <= s:  # 기준점의 시작시간보다 종료시간이 이르거나 같은 경우
            temp.append(dp[j])  # 해당 회의의 dp값을 저장
    if temp:  # 리스트가 비어있지 않다면
        dp[i] = max(temp) + 1
    else:  # 리스트가 비어있다면
        dp[i] = 0
<<<<<<< HEAD
print(max(dp)+1)


# 그리디 알고리즘 이용
# 종료시간을 기준으로 오름차순으로 정렬한다
# 첫번째 활동을 선택한다
# 다음 활동 선택 시 첫번째 활동의 종료시간보다 시작시간이 이른 활동은 제외하고 남은 활동에 대해 위의 작업을 반복한다.
'''
10
1 4
1 6
6 10
5 7
3 8
5 9
3 5
8 11
2 13
12 14
'''

N = int(input())
lst = []
for i in range(N):
    s, e = map(int, input().split())
    lst.append((s, e))

lst.sort(key=lambda x: x[1])  # 종료시간 기준으로 정렬
lst = [(0, 0)] + lst
s = []
j = 0
for i in range(1, N+1):
    if lst[i][0] >= lst[j][1]:  # 남은 회의의 시작시간이 현재 회의의 종료시간과 같거나 더 늦다면
        s.append(i)  # 다음 회의로 지정
        j = i
print(s)
print(len(s))
=======
print(max(dp)+1)
>>>>>>> origin/master
