# 지그재그 순회
m, n = 4, 3
arr = [[1] * m for _ in range(n)]
print(arr)
for i in range(n):  # n은 행의 수
    for j in range(m):  # m은 열의 수
        arr[i][j + (m-1-2*j) * (i%2)] = i  # 홀수번째 행일 때에만 j의 값이 증가할수록 열의 인덱스는 감소한다.
print(arr)

# 행우선 탐색
N = 2
M = 4
arr2 = [[0, 1, 2, 3], [4, 5, 6, 7]]
for i in range(N):
    for j in range(M):
        print(arr2[i][j])

print()
# 열우선 탐색
for i in range(M):
    for j in range(N):
        print(arr2[j][i])

print()
# 지그재그 탐색
for i in range(N):
    for j in range(M):
        print(arr2[i][j + (M - 1 - 2*j) * (i % 2)])  # j가 커질수록 두번째 인덱스의 값은 1씩 작아지도록


arr3 = [[0] * M for _ in range(N)]
# arr4 = [[0] * M] * N
# [0] * M 리스트를 참조하는 객체가 N-1개 더 만들어짐
print(arr3)

max_v = 0
for i in range(N):
    row_total = 0
    for j in range(M):
        row_total += arr2[i][j]
    if max_v < row_total:
        max_v = row_total

print(max_v)

# 전치행렬
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:  # 대각선 기준 우상단의 요소에 대해서만 전치
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)