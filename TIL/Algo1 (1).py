T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    result = 0
    # 평탄화 영역의 높이 값의 합 구하기
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            total += board[i][j]
    # 평탄화 높이 구하기
    avg = total // ((x2 - x1 + 1) * (y2 - y1 + 1))
    # 평탄화 영역의 높이를 모두 평탄화 높이로 맞추기 위해 필요한 작업의 수 계산
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            # 높이를 낮춰야 하는 경우
            if board[i][j] >= avg:
                result += (board[i][j] - avg)
            # 높이를 높여야 하는 경우
            else:
                result += (avg - board[i][j])

    print(f'#{tc} {result}')