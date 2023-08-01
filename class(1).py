# 카운팅 정렬 : 정수를 정렬하는 알고리즘으로, 요소 별로 개수를 세어서 정렬


# def counting(arr):
#     max_v = max(arr)
#     count_arr = [0] * (max_v + 1)
#
#     for i in arr:
#         count_arr[i] += 1
#
#     sorted_arr = []
#     for i, count in enumerate(count_arr):
#         sorted_arr.extend([i] * count)
#
#     return sorted_arr
#
#
# numbers = [1, 4, 1, 2, 7, 5, 2]
# sorted_list = counting(numbers)
# print(sorted_list)


# 탐욕 알고리즘 : 부분 문제에서 가장 최선의 선택을 해서 전체 문제를 푸는 알고리즘
# 거스름돈 문제 : 동전종류가 100원, 50원, 10원 / 가장 적은 수의 동전으로 거스름돈을 줄 수 있을까?

# change = 350
# cnt = 0
# new_dict = {'10': 0, '50':0, '100': 0}
# n = change // 100
# if n > 0:
#     new_dict['100'] = n
#     n = change % 100
#     if n // 10 >= 5:
#         new_dict['50'] = 1
#         new_dict['10'] = n // 10 - 5
#     else:
#         new_dict['10'] = n // 10
# new_list = new_dict.values()
# for i in new_list:
#     cnt += i
# print(cnt)

# def greedy(money, coins):
#     coins.sort(reverse=True)
#     change = {coin:0 for coin in coins}
#     for coin in coins:
#         while money >= coin:
#             money -= coin
#             change[coin] += 1
#
#     return change
#
# result = greedy(380, [10, 50, 100])
# print(result)

# 4834문
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     cards = input()
#     # 카운트 결과를 저장할 딕셔너리 생성
#     counts = {str(n):0 for n in range(10)}
#     for card in cards:
#         counts[card] += 1
#     max_cnt = max(counts.values())
#     max_index = max([int(key) for key, value in counts.items() if value == max_cnt])
#
#     print(f'#{tc} {max_index} {max_cnt}')

# 4835문
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     new_arr = []
#
#     for j in range(N - M + 1): # 입력받은 리스트 내에서 가능한 구간합의 개수만큼 반복
#         result = 0
#         for k in range(j, j + M): # M의 범위로 구간합 구해서 저장하기
#             result += arr[k]
#             new_arr.append(result)
#
#     max_arr = max(new_arr)
#     min_arr = min(new_arr)
#
#     print(f'#{tc} {max_arr-min_arr}')

# 4831문
# T = int(input())
#
# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split()) # K:최대이동가능거리 , N:종점, M:충전기 정류장의 개수
#     arr = list(map(int, input().split()))
#     ch = [0] * (N + 1)
#
#     for i in arr:
#         ch[i] += 1
#
#     current = 0
#     cnt = 0
#
#     while current < N:
#
#         #갈 수 있는 최대 거리
#         if ch[current + K]:
#             current += K
#             cnt += 1
#         # 충전소 찾기
#         else:
#             # 충전소를 찾으면 충전
#             for j in range(1, K):
#                 if ch[current + K - j]:
#                     current += (K - j)
#                     cnt += 1
#                     break
#                 # 범위 내에 충전소가 없으면 반복 중단
#             else:
#                 cnt = 0
#                 break
#         if current + K >= N:
#             current = N
#
#     print(f'#{tc} {cnt}')

# 4831문 다른 풀이
T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())  # K:최대이동가능거리 , N:종점, M:충전기 정류장의 개수
    arr = list(map(int, input().split()))  # 충전소의 위치만 저장
    current, cnt = 0, 0
    # 종점도착 시까지 반복
    while current != N:
        # 현위치에서 종점까지의 거리가 K보다 작은 경우
        if N <= current + K:
            current = N
            break

        for i in range(len(arr) -1, -1, -1): # 출발점으로부터 가장 먼 충전소부터 순회
            # 최대 이동 가능 거리 내에 충전소가 있을 경우 충전
            if arr[i] <= current + K:
                cnt += 1
                current = arr[i]
                arr = arr[i + 1:]  # 해당 충전소 이후의 정류장만 남기기
                break
            # 최대 이동 가능 거리 내에서 충전소를 찾지 못 한 경우
            if i == 0:
                cnt = 0
                current = N

    print(f'#{tc} {cnt}')
