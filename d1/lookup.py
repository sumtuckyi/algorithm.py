# 탈주범 검거
# 7가지 파이프 모양별 4방향(상, 하, 좌, 우 순서) 연결가능 여부 정보를 담은 리스트 생성
pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
# 상, 하, 좌, 우 이동
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
# 상하, 좌우를 매칭하기 위한 리스트 - 예를 들어 기준점에서 각각 상, 하, 좌, 우에 파이프가 있는 경우 각 파이프의 리스트에서 몇 번째 인덱스가 1이면 이동이 가능한지 판단
opp = [1, 0, 3, 2]

from collections import deque


def bfs(a, b, cnt): # 탐색 시작점과 현재까지의 이동횟수 전달
    if cnt == L:  # 주어진 이동횟수 만큼 이동했다면
        return
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):  # 상하좌우 방향으로
            if 0 <= x + di[i] < N and 0 <= y + dj[i] < M:  # 범위 안에 있고
                if land[x + di[i]][y + dj[i]] != 0:  # 파이프가 존재하는 경우
                    if pipe[land[x + di[i]][y + dj[i]]][opp[i]] == 1 and pipe[land[x][y]][i] == 1:  # 현재 위치와 파이프가 이어져 있다면
                        # # 중복 제거
                        # if (x + di[i], y + dj[i]) in v:
                        #     continue
                        # else:
                        v.append((x + di[i], y + dj[i]))
                        bfs(x + di[i], y + dj[i], cnt+1)


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # 맵의 행, 열/맨홀 좌표(행, 열)/이동횟수
    land = [list(map(int, input().split())) for _ in range(N)]  # 지하터널
    v = deque()
    # v = [[0 for _ in range(M)] for _ in range(N)]  # 방문확인 배열
    cnt = 1  # 총 이동횟수(L까지)
    q = deque()
    bfs(R, C, cnt)
    print(f'#{tc} {len(set(v))}')
