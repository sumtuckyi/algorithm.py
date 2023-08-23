arr1 = [
    [3, 3, 5, 3, 1],
    [2, 2, 4, 2, 6],
    [4, 9, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 3, 5, 9, 2]
]

max_result = 0  # 2차원 배열 내에서 가능한 4방향 합 중 최대값
max_x = 0  # 최대값을 가지는 기준점의 좌표
max_y = 0  # 최대값을 가지는 기준점의 좌표


def sum(y, x):  # 인자로 기준점의 좌표를 전달하면
    direction = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    result = 0
    for i, j in direction:  # 기준점에서 각 방향으로 순차적으로 탐색하여
        dir_y = y + i
        dir_x = x + j
        if 0 <= dir_y < len(arr1) and 0 <= dir_x < len(arr1):
            result += arr1[dir_y][dir_x]
    return result  # 상하좌우를 더한 값을 반환


for i in range(len(arr1)):  # 2차원 배열 내의 모든 요소에 대해 연산을 수행하고 그 결과를 비교하여 최대값 도출
    for j in range(len(arr1)):
        if max_result < sum(i, j):
            max_result = sum(i, j)
            max_y, max_x = i, j

print(max_x, max_y)
