# 델타를 이용한 2차원 배열 탐색

N = int(input())
arr = list(map(int, input().split()))

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
max_v = 0
for i in range(N):
    for j in range(N):
        # 기준점
        s = arr[i][j]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                s += arr[ni][nj]
        if max_v < s:
            max_v = s