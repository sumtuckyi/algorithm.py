T = int(input())

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def peak(b):  # 봉우리의 개수를 구하는 함수
    global cnt
    for i in range(N):
        for j in range(N):
            x, y = i, j  # 봉우리인지 확인할 기준점
            adj_p = 0  # 인접한 칸의 개수
            check = 0  # 인접한 칸의 값이 기준점보다 작은 경우 카운트
            for l, m in d:  # 상하좌우로 탐색
                if 0 <= x + l < N and 0 <= y + m < N:  # 탐색 범위가 보드의 범위를 벗어나지 않는 경우
                    adj_p += 1  # 인접한 칸의 개수 카운트
                    if b[x][y] > b[x + l][y + m]:  # 인접한 칸의 값이 기준점보다 작은지 확인
                        check += 1
            if adj_p == check:  # 인접한 칸의 개수와 기준점보다 값이 작은 칸의 개수가 같으면 봉우리 체크
                cnt += 1


for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0  # 봉우리의 개수
    peak(board)
    print(f'#{tc} {cnt}')


# 불값을 이용하여 봉우리 체크
    for i in range(N):
        for j in range(N):
            x, y = i, j  # 봉우리인지 확인할 기준점
            high_fd = False  # 더 높은 인접지역을 찾았는지 확인하는 변수
            for l, m in d:  # 상하좌우로 탐색
                if 0 <= x + l < N and 0 <= y + m < N:  # 탐색 범위가 보드의 범위를 벗어나지 않는 경우
                    if b[x][y] <= b[x+l][y+m]:  # 인접지역이 기준점보다 높은 경우
                        high_fd = True
                        break
            if not high_fd:
                cnt += 1

# for, else문 사용 - 간결한 코드 작성 가능
    for i in range(N):
        for j in range(N):
            x, y = i, j  # 봉우리인지 확인할 기준점
            for l, m in d:  # 상하좌우로 탐색
                if 0 <= x + l < N and 0 <= y + m < N:  # 탐색 범위가 보드의 범위를 벗어나지 않는 경우
                    if b[x][y] <= b[x+l][y+m]:  # 인접지역이 기준점보다 높은 경우
                        break
            else:  # for문이 break없이 완료될 경우(인접지역이 기준점보다 높은 경우가 없을 경우)
                cnt += 1
