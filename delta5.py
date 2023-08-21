T = int(input())
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bomb():
    max_v = 0
    for i in range(N):
        for j in range(N):
            x, y = i, j
            virus = board[x][y]
            for p in range(1, P+1):  # 폭탄의 범위 만큼 반복
                for a, b in delta:
                    dx, dy = x + p*a, y + p*b
                    if 0 <= dx < N and 0 <= dy < N:
                        virus += board[dx][dy]
            if max_v < virus:
                max_v = virus
    return max_v


for tc in range(1, T + 1):
    N, P = map(int, input().split())  # 마을의 크기, 백신의 범위
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {bomb()}')
