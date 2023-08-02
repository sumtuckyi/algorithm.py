# arr1 = [['_'] * 5 for _ in range(4)]
arr = []
for i in range(4):
    a = []
    for j in range(5):
        a.append('_')
    arr.append(a)


def exploded(y, x):  # 인자로 기준점의 좌표를 전달하면
    direction = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]
    for k, l in direction:
        dir_x, dir_y = x + l, y + k  # 기준점에서 각 방향으로 순차적으로 탐색
        if 0 <= dir_y < len(arr) and 0 <= dir_x < len(arr[0]):
            arr[dir_y][dir_x] = '#'


for i in range(2):
    y, x = map(int, input().split())
    exploded(y, x)
    for i in arr:
        print(*i)