# 기준점에 대해 마름모 영역을 탐색 -> 기준점 중심으로 큐에 상하좌우 4개 영역을 추가 -> 순서대로 상하좌우 탐색 반복
# 서비스 영역의 크기는 K로 2면 기준점 포함 1회 근접 지역 탐색
# k가 3이면 2번만 탐색영역을 정하면 됨. 1이면 정할 필요 없음
# K <= N, 서비스 영역의 최대 크기는 마을의 크기
# 운영 비용 = K**2 + (K-1)**2
# 이익 = M*집의 개수 - 운영 비용
# 마을에서 집은 '1'로 표시
from collections import deque
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check():  # 기준점을 전달하면 인접한 4칸만 확인하는 함수

def search(x, y, k):  # 행과 열, 서비스 영역의 크기
    cnt_h = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 마을에서 탐색할 지점의 좌표를 큐에 전부 저장
    dx, dy = x, y  # 기준점
    q = deque()  # 기준점 중심으로 상하좌우에 집이 있는지 확인해야함
    q.append((x, y))
    for l in range(1, k):  # 서비스 영역의 크기 만큼 반복(k는 최소 2에서 최대 N+1)
        for i, j in d:  # 기준점 상하좌우 탐색
            if 0 <= dx + i*l < N and 0 <= dy + j*l < N and not visited[dx + i*l][dy + j*l]:  # 탐색 지점이 마을 내에 있고 아직 방문하지 않았다면
                q.append((dx + i*l, dy + j*l))  # 다음 탐색 지점 큐에 추가
                visited[dx][dy] = 1  # 방문표시
    while q:
        dx, dy = q.popleft()  # 큐의 첫번째 요소를 꺼냄
        visited2[dx][dy] = 1  # 방문확인
        for i, j in d:  # 기준점 상하좌우 탐색
            if 0 <= dx + i < N and 0 <= dy + j < N and not visited2[dx + i][dy + j]:  # 탐색 지점이 마을 내에 있고 아직 방문하지 않았다면
                if b[dx + i][dy + j] == '1':  # 해당지점에 집이 있으면 카운트
                    cnt_h += 1
    return cnt_h


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # M은 하나의 집이 지불할 수 있는 비용
    b = [list(input().split()) for _ in range(N)]
    # visited = [[0 for _ in range(N)] for _ in range(N)]
    # visited2 = [[0 for _ in range(N)] for _ in range(N)]

    # 마을의 모든 지점에 대해
    # k가 1인 경우(최소 한 개의 집이 존재함)
    max_v = M - 1
    max_h = 0
    # 그 외의 경우
    for k in range(2, N+2):  # k가 2부터 N+1인 경우까지(N이 짝수인 경우에는 서비스 범위가 N+1이어야 중심을 기준점으로 잡았을 때 모든 범위에 서비스 제공 가능)
        for i in range(N):
            for j in range(N):
                h = search(i, j, k)  # 해당 지점을 기준으로 k범위의 집의 수
                print(k,i,j,h)
                if M*h - (k**2 + (k-1)**2) > 0:  # 손해를 보지 않는 경우에 한해
                    if max_h < h:  # 서비스를 제공받는 집의 수 갱신
                        max_h = h
    dd = 1
    print(f'#{tc} {max_h}')