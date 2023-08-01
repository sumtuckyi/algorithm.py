# 연습문제 1
# import random
#
# a_list = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
#
#
# def cal_abs(new_list):
#
#     dx = [-1, 1, 0, 0]  # 상하좌우
#     dy = [0, 0, -1, 1]
#
#     x, y = 0, 0
#     current = 0
#     result = 0
#     for i in range(5):
#         for j in range(5):
#             current = new_list[i][j]
#             direction = 0
#             total = 0
#             while direction < 4:
#                 y, x = j, i
#                 y, x = y+dy[direction], x+dx[direction]
#                 if 0 <= x <= 4 and 0 <= y <= 4 :
#                     total += abs(current - new_list[x][y])
#                     direction += 1
#                 else:
#                     direction += 1
#             result += total
#     return result
#
#
# a = cal_abs(a_list)
# print(a)

# 연습문제 3
b_list = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]
]

c_list = []
for i in b_list:
    c_list.extend(i)
c_list.sort() # 2차원 배열의 요소를 오름차순으로 정렬
new_arr = [[0] * 5 for _ in range(5)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
x, y = 0, 0
x, y = x + dx[direction], y + dy[direction]
if 0 <= x < 5 and 0 <= y <= 5:


