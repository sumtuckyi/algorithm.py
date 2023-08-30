# 이동경로는 항상 6-7-8처럼 1씩 증가
# 먼저 모든 칸에 대해 그 칸을 기준으로 상하좌우에 이동할 수 있는 방의 개수를 카운트
# 그런 다음 모든 칸에 대해 인접한 칸을 탐색하여 해당 칸으로 이동할 수 있다면 해당칸 값에 1을 더한 값과 원래 값 중 큰 값을 선택
#
# def bfs(a, b, N):
#     dx, dy = a, b
#     for i, j in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
#         if 0 <= dx + i < N and 0 <= dy + j < N:
#             if arr[dx + i][dy + j] == arr[dx][dy] + 1:
#                 d[a*N+b] += 1
#
#
# def dp(a, b, N):
#     dx, dy = a, b  # 해당 점을 기준으로
#     for i, j in [(1, 0), (-1, 0), (0, -1), (0, 1)]:  # 상하좌우에 이동가능한 칸이 있으면
#         if 0 <= dx + i < N and 0 <= dy + j < N:
#             if arr[dx + i][dy + j] == arr[dx][dy] + 1:
#                 d[a*N+b] = max(d[a*N+b], d[(dx+i)*N+(dy+j)]+1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     d = [0]*(N*N+1) # 카운트 배열
#     #카운트 배열 초기값 채우기
#     for i in range(N):
#         for j in range(N):
#             bfs(i, j, N)
#     for i in range(N):
#         for j in range(N):
#             dp(i, j, N)
#     max_v = max(d)
#     idx = d.index(max_v)
#     print(f'#{tc} {arr[idx//N][idx%N]} {max_v+1}')

#
dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            for r, c in dir:
                if 0 <= i + r <N and 0 <= j + c < N:
                    if arr[i+r][j+c] == arr[i][j] + 1:
                        v[arr[i][j]] = 1

    start, cnt, temp = 0, 1, 1
    for i in range(len(v)-1, -1, -1):
        if v[i] == 1:
            temp += 1
        else:
            if cnt <= temp:
                cnt = temp
                start = i + 1 # 연속된 숫자의 시작점 갱신
            temp = 1
    print(f'#{tc} {start} {cnt}')