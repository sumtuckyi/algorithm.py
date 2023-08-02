# 색칠하기
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    areas = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0] * 10 for _ in range(10)]  # 격자 생성
    cnt = 0

    for area in areas:
        x1, y1, x2, y2, c = area
        for k in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                arr[k][j] += c
                # if c == 1:
                #     arr[k][j] += 1
                # else:
                #     arr[k][j] += 2

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')

