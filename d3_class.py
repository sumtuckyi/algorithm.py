T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    K = int(input())
    board = [list(input()) for _ in range(N)]

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def explosion(y, x, k):
        dir_y, dir_x = y, x
        board[dir_y][dir_x] = '%'
        for i, j in delta:
            # 폭발 범위 만큼 반복
            for h in range(1, k + 1):
                dir_y, dir_x = y + h * i, x + h * j
                if 0 <= dir_y < N and 0 <= dir_x < M:
                    if board[dir_y][dir_x] != '#' and board[dir_y][dir_x] != '@':  # board[dir_y][dir_x] == '_'
                        board[dir_y][dir_x] = '%'
                    else:
                        break


    for i in range(N):
        for j in range(M):
            if board[i][j] == '@':
                explosion(i, j, K)

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



