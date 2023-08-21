T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 보드의 크기
    board = [list(map(int, input().split())) for _ in range(N)]
    targets = {}  # 사과의 위치
    direction = 1 # 출발하여 1번 사과에 도착하였을 때의 방향(하)
    result = 1  # 우회전의 횟수

    num = 0  # 사과의 개수
    for i in range(N):  # 사과의 개수와 위치 파악하기
        for j in range(N):
            if board[i][j] != 0:
                num += 1
                targets.setdefault(board[i][j], (i, j))

    arr = [
        [3, 1, 2, 3],
        [3, 3, 1, 2],
        [2, 3, 3, 1],
        [1, 2, 3, 3]
    ]
    cnt = 1  # 사과를 먹을 때마다 카운트
    dir_x, dir_y = targets[1]  # 기준점을 1번 사과의 위치로 초기화
    # while문 안의 조건문을 그리드에 저장하여 코드의 가독성을 높일 수 있다.
    while cnt < num:
        a, b = targets[cnt + 1]  # 다음 사과의 위치
        if dir_x > a and dir_y < b:  # 제 1사분면에 다음사과가 위치
            result += arr[direction % 4][0]
            direction += arr[direction % 4][0]
        elif dir_x < a and dir_y < b:  # 제 2사분면에
            result += arr[direction % 4][1]
            direction += arr[direction % 4][1]
        elif dir_x < a and dir_y > b:  # 제 3사분면에
            result += arr[direction % 4][2]
            direction += arr[direction % 4][2]
        else:  # 제 4사분면에
            result += arr[direction % 4][3]
            direction += arr[direction % 4][3]
        cnt += 1  # 사과를 먹음
        dir_x, dir_y = a, b  # 플레이어 위치 이동


    print(f'#{tc} {result}')