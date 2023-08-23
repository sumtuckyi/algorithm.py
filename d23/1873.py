# 삼성시의 버스 노선
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())  # 노선의 수
#     b_stops = [0] * 5001  # 버스 정류장 번호(인덱스)별 지나는 버스의 수
#     for i in range(N):
#         a, b = map(int, input().split())
#         for j in range(a, b+1):
#             b_stops[j] += 1
#     P = int(input())  # 출력할 정류장의 개수
#     print(f'#{tc}', end=' ')
#     for _ in range(P):
#         idx = int(input())
#         print(b_stops[idx], end=' ')

#
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stops = [int(input()) for _ in range(P)]
    count = [0] * 5001
    result = []

    for i in range(N):
        for j in range(lines[i][0], lines[i][1] + 1):
            count[j] += 1

    for i in stops:
        result.append(count[i])

    print(f'#{tc}', *result)


