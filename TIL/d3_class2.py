# board = [list(map(int, input().split())) for _ in range(5)]
# numbers = [list(map(int, input().split())) for _ in range(5)]
# 2차원 배열을 입력받아 1차원으로 저장하기
board = [int(num) for _ in range(5) for num in input().split()]
numbers = [int(num) for _ in range(5) for num in input().split()]

cnt = 0
#  리스트의 길이는 모자라지만 않게 임의로 정하면 됨
x_list = [0] * 10
y_list = [0] * 10
di_list1 = [0] * 10
di_list2 = [0] * 10

for n in numbers:
    # 부른 숫자의 인덱스를 찾아서
    a = board.index(n)
    # 인덱스를 이용해 해당 숫자의 위치 좌표 계산
    x, y = a // 5, a % 5  # 인덱스의 범위 : 0 ~ 24, 보드의 세로크기로 나눈 몫이 행, 가로크기로 나눈 나머지가 열
    # 가로, 세로 , 대각선 빙고 개수 카운트 증가
    x_list[x] += 1  # x_list[1]은 보드의 1행에 있는 숫자가 불린 횟수
    y_list[y] += 1  # y_list[y]는 보드의 y열에 있는 숫자가 불린 횟수
    di_list1[x + y] += 1  # 우상향 대각선 식별, 동일 대각선에 놓인 x, y 좌표의 합은 일정함
    di_list2[y - x + 4] += 1  # 리스트의 인덱스는 우하향 대각선을 식별
    # 빙고 개수를 확인하여 카운트 증가
    if x_list[x] == 5: # x_list[x]가 5라는 것은 x열에 있는 숫자가 5번 불렸다는 의미
        cnt += 1
    if y_list[y] == 5:
        cnt += 1
    if di_list1[x + y] == 5 or di_list2[y - x + 4] == 5:
        cnt += 1
    d = 1  # 더미 코드, break point
    if cnt == 3:
        print(n)
        break



# def check_bingo(y, x, dy, dx):
#     cnt = 0
#     while 0 <= y + dy < 5 and 0 <= x + dx < 5:
#         if board[y + dy][x + dx] == 'b':
#             cnt += 1
#             if cnt == 5:
#                 return 1
#         else:
#             cnt = 0
#             y += dy
#             x += dx
#     return 0
#
# for i in range(5):  # 사회자가 불러주는 다섯 줄 만큼 반복
#     for j in range(5):
#         for k in range(5):
#             if board[j][k] in numbers[i]:
#                 number = board[j][k]
#                 board[j][k] == 'b'
#                 if i >= 2 and j >= 0 and k >= 0:
#                     for h in range(5):
#                         count += check_bingo(h, 0, 0, 1)
#                         if count == 3:
#                             result = number
#                     for l in range(5):
#                         count += check_bingo(0, l, 1, 0)
#                     for m in range(5):
#                         count += check_bingo(m, 0, 1, 1)
#                     for n in range(1, 5):
#                         count += check_bingo(0, n, 1, 1)
#                     for h in range(5):
#                         count += check_bingo(h, 0, -1, 1)
#                     for h in range(1, 4):
#                         count += check_bingo(4, h, -1, 1)


# 예지 코드
# 빙고
# 위에 다섯줄이 빙고, 밑에서 부터는 사회자가 부르는 숫자, 그랬을 때 빙고가 3개 될때의 숫자를 고르세요
my_nums = [list(map(int, input().split())) for _ in range(5)]
lucky_nums = [list(map(int, input().split())) for _ in range(5)]

# 해야하는거
# 1. 럭키넘버 순서대로 빙고를 칠해준다
# 2. 빙고가 되는지 판단한다

bingo = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


# 빙고가 되는 조건 : 가로의 합이 5, 세로의 합이 5, 대각선의 합이 5

# 럭키넘버 순서대로 빙고를 칠해주는 함수
def append_bingo(lucky): # 불린 숫자를 인자로 받음
    for i in range(5):
        if lucky in my_nums[i]:  # 보드를 행순서대로 탐색
            key = my_nums[i].index(lucky)  # 열의 좌표
            bingo[i][key] += 1


# 빙고 개수 세어주는 함수
def count_bingo():
    count = 0
    # 가로
    for i in range(5):
        if sum(bingo[i]) == 5:
            count += 1
    # 세로
    for i in range(5):
        a = 0
        for j in range(5):
            a += bingo[j][i]
        if a == 5:
            count += 1
    # 대각선
    b = 0
    for i in range(5):  # 우하향 대각선
        b += bingo[i][i]
        if b == 5:
            count += 1
    c = 0
    for i in range(5):  # 우상향 대각선
        c += bingo[4 - i][i]
        if c == 5:
            count += 1

    return count


for i in range(5):
    for j in range(5):
        append_bingo(lucky_nums[i][j])  # 불린 숫자를 차례로 함수의 인자로 전달
        if count_bingo() == 3:  # 숫자를 하나씩 부를 때마다 빙고 여부를 함수를 호출하여 확인
            print(lucky_nums[i][j])
            break

