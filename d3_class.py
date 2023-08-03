T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 보드의 가로, 세로
    K = int(input())  # 폭발 범위
    board = [list(input()) for _ in range(N)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def explosion(y, x, k):  # y, x의 값이 '@'인 경우에 호출
        dir_y, dir_x = y, x  # 기준점
        board[dir_y][dir_x] = '%'
        for i, j in delta:  # 상 하 좌 우 순서로 반복하되
            # 각 방향에서 폭발 범위 만큼 반복
            for h in range(1, k + 1):
                dir_y, dir_x = y + h * i, x + h * j
                if 0 <= dir_y < N and 0 <= dir_x < M:
                    # 폭발 범위에 해당하는 영역이 벽이거나 아직 터지지 않은 폭탄인 경우에는 폭발 x (즉, '_'인 경우에만 폭발함)
                    if board[dir_y][dir_x] != '#' and board[dir_y][dir_x] != '@':  # board[dir_y][dir_x] == '_'
                        board[dir_y][dir_x] = '%'
                    else:
                        break  # 다시 delta for문으로 이동

    # 보드를 차례로 순회하면서 폭탄이 등장하면 함수를 호출함
    for i in range(N):
        for j in range(M):
            if board[i][j] == '@':
                explosion(i, j, K)

    # 이차원 배열 출력 양식에 맞춰 출력하기
    for i in board:
        print(*i)




# input
'''
2
3 5
2
_#_#@
_#_#@
@___#
3 5
2
_#_#_
_#_#_
@_@__
'''


# output
'''
%#_#%
%#_#%
%%%_#

%#%#_
%#%#_
%%%%%
'''



