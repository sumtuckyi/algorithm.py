# 돌을 놓을 위치(col, row)와 돌의 색이 주어지면 보드의 상황이 어떻게 달라지는지 갱신한다.
# 흑돌은 1이고 백돌은 2, 보드의 크기는 4, 6, 8중에 하나
# 시작 전 게임판의 상태는 동일하다. (중심부 4칸에 돌을 배치)
# 게임이 끝난후 흑돌과 백돌의 개수를 각각 구한다.
# 돌을 놓는 기준점에서 8방향으로 보드의 범위 내라면 끝까지 탐색
coordinations = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
B = 1
W = 2


def change(x, y, wob, N):
    b[y-1][x-1] = wob  # 보드에 돌 놓기
    dx, dy = x-1, y-1  # 기준점
    # 놓은 돌과 같은 색의 돌을 만날 때까지 반복
    for c, d in coordinations:  # 8방향으로 탐색
        dy, dx = dy + c, dx + d
        temp = []  # 포위한 돌의 좌표를 저장
        while 0 <= dx < N and 0 <= dy < N and b[dy][dx] != wob:  # 범위 내에 있고 놓은 돌과 같은 색이 아닌 한
            temp.append((dy, dx))
            dy, dx = dy + c, dx + d  # 다음칸을 탐색
        if 0 <= dx < N and 0 <= dy < N and b[dy][dx] == wob:  # 반복문 종료 후 놓은 돌과 같은 색의 돌을 만나면
            print(temp)
            for i, j in temp:
                b[i][j] = wob  # 놓은 돌과 같은 색으로 바꿈
    print(b)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    b = [[0] * N for i in range(N)]
    # 보드 초기화
    b[N // 2 - 1][N // 2 - 1] = W
    b[N // 2 - 1][N // 2] = B
    b[N // 2][N // 2 - 1] = B
    b[N // 2][N // 2] = W

    for i in range(M):
        col, row, bw = map(int, input().split())
        change(col, row, bw, N)
        print(b)
    # 모든 돌을 놓은 후 테이블의 상황 출력하기
    cb = cw = 0
    for i in range(N):
        for j in range(N):
            if b[i][j] == 1:  # 흑돌인 경우
                cb += 1
            else:
                cw += 1
    print(f'#{tc} {cb} {cw}')