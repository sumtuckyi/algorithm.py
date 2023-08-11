# 스도쿠 검증
def sudoku(arr):
    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)]
    # 행탐색
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):  # 행별로 1~9까지 있는지 카운트
            cnt[arr[i][j]] += 1
        for k in range(1, 9+1):  # 각 행에 대해
            if cnt[k] == 0:  # 숫자가 하나라도 중복되면 0을 반환
                return 0
    # 열탐색
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[j][i]] += 1
        for k in range(9):
            if cnt[k] == 0:
                return 0
    # 정방형 탐색
    for i in range(3):
        for j in range(3):
            cnt = [0] * 10
            for x, y in d:
                cnt[arr[3*i+1+x][3*j+1+y]] += 1
            for k in range(9):
                if cnt[k] == 0:
                    return 0
    return 1

T = int(input())

for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    ans = sudoku(board)
    print(f'#{tc} {ans}')




# for tc in range(1, T + 1):
#     arr = [list(map(int, input().split())) for _ in range(9)]
#     ans = sudoku(arr) # 올바른 스도쿠인 경우 1
#     # 행과 열 탐색
#     for i in range(9):
#         if len(set(arr[i])) != 9:  #
#             ans = 0
#             break
#         for j in range(9):
#             temp = []
#             temp.append(arr[j][i])
#             if len(set(temp)) != 9:
#                 ans = 0
#                 break
