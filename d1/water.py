# from collections import deque
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())  # 지도의 행과 열
#     b = [list(input()) for _ in range(N)]
#     w = []
#     q = deque()
#     cnt = [[float('inf') for _ in range(M)] for _ in range(N)]
#     # 물인 지점을 저장
#     for i in range(N):
#         for j in range(M):
#             if b[i][j] == 'W':
#                 w.append((i, j))
#                 cnt[i][j] = 0
#     for i, j in w:
#         x, y = i, j
#     for l in range(N):
#         for m in range(M):
#             if (l != i or m != j) and b[l][m] == 'L':  # 시작점을 제외한 좌표 중 땅에 대해서만
#                 if cnt[l][m] == 1:
#                     continue
#                 cnt[l][m] = min(abs(x-l)+abs(y-m), cnt[l][m])
#     total = 0
#     for i in range(N):
#         for j in range(M):
#             total += cnt[i][j]
#     print(f'#{tc} {total}')
#     print(cnt)


from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 지도의 행과 열
    b = [list(input()) for _ in range(N)]
    w = []
    q = deque()
    total = 0
    cnt = [[0 for _ in range(M)] for _ in range(N)]
    v = [[0 for _ in range(M)] for _ in range(N)]
    # 물인 지점을 저장
    for i in range(N):
        for j in range(M):
            if b[i][j] == 'W':
                w.append((i, j))
    # 물인 칸을 기준으로 탐색
    # 물인 칸을 모두 큐에 넣기
    for i, j in w:
        q.append((i, j))
    while q:
        x, y = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x+di < N and 0 <= y+dj < M:
                if b[x+di][y+dj] == 'L' and v[x+di][y+dj] == 0:  # 아직 방문하지 않은 땅이라면
                    cnt[x+di][y+dj] = cnt[x][y] + 1  # 물로부터의 거리 구해주기
                    v[x+di][y+dj] = 1  # 방문표시
                    q.append((x+di, y+dj))  # 새로운 기준점으로
    for i in range(N):
        for j in range(M):
            total += cnt[i][j]
    print(f'#{tc} {total}')


# 최단거리 저장과 방문여부 확인을 하나의 2차원 배열로 처리
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 지도의 행과 열
    check = [[-1 for _ in range(M)] for _ in range(N)]  # 최단거리를 저장할 리스트
    q = deque()
    for i in range(N):
        t = input()
        for j in range(M):
            if t[j] == 'W':
                q.append((i, j))
                check[i][j] = 0  # 최단거리를 0으로 설정
    result = 0 # 탐색하면서 최단거리가 구해지면 바로 더해줌
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x+dx < N and 0 <= y+dy < M and check[x+dx][y+dy] == -1:
                check[x+dx][y+dy] = check[x][y] + 1
                q.append((x+dx, y+dy))
                result += check[x+dx][y+dy]
    print(f'#{tc} {result}')