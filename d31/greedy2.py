# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     lst = []
#     dp = [0] * N
#     for i in range(N):
#         s, e = map(int, input().split())
#         lst.append((s, e))
#     # 시작 시간이 이른 순으로 정렬
#     lst.sort(key=lambda x: x[0])
#     # dp배열 채우기
#     for i in range(N):
#         s, e = lst[i]  # 기준점
#         temp = []
#         for j in range(0, i):  # 기준점보다 시작시간이 이른 경우만 고려
#             if lst[j][1] <= s:  # 기준점의 시작시간보다 종료시간이 이르거나 같은 경우
#                 temp.append(dp[j])  # 해당 회의의 dp값을 저장
#         if temp:  # 리스트가 비어있지 않다면
#             dp[i] = max(temp) + 1
#         else:  # 리스트가 비어있다면
#             dp[i] = 0
#     print(f'#{tc} {max(dp)+1}')

#
T = int(input())
for tc in range(1, T + 1):
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

    print(f'#{tc} {len(s)}')