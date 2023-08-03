T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board1 = [list(list(input())) for _ in range(N)]

# 행탐색

    def game(board, n):
        result = "NO"

        for i in range(n):
            cnt = 1  # 연속한 돌의 개수
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = "YES"
                        #print("행")
                        return result
                else:
                    cnt = 1

    # 열탐색

        for i in range(n):
            cnt = 1
            for j in range(n - 1):
                if board[j][i] == board[j + 1][i] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = "YES"
                        #print("열")
                        return result
                else:
                    cnt = 1

    # 대각선 탐색 1
        cnt = 1
        for i in range(n - 1):
            for j in range(n - 1):
                if i == j:
                    if board[i][j] == board[i + 1][j + 1] == 'o':
                        cnt += 1
                        if cnt == 5:
                            result = "YES"
                            #print("좌상향 대각선")
                            return result
                    else:
                        cnt = 1

    # 대각선 탐색 2
        cnt = 1
        for i in range(n - 1):
            for j in range(n):
                if i + j == n - 1:
                    if board[i][n-1-i] == board[i + 1][n-1-(i+1)] == 'o':
                        cnt += 1
                        if cnt == 5:
                            result = "YES"
                            #print("우상향 대각선")
                            return result
                    else:
                        cnt = 1
        if result == "NO":
            return result

    #game(board1, N)
    print(f'#{tc} {game(board1, N)}')