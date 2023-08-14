def back_tracking(start):  # 시작점을 인자로 전달
    global result
    if maze[start[0]][start[1]] == '3':
        result = 1
        return
    stack.append(start)
    x, y = start
    for i in range(4):  # 우하상좌 순으로 탐색
        # 범위 내에 있고 벽이 아닌 경우
        if 0 <= x+d[i][0] < N and 0 <= y+d[i][1] < N and maze[x+d[i][0]][y+d[i][1]] != '1':
            # 아직 방문하지 않은 지점인 경우
            if [x + d[i][0], y + d[i][1]] not in stack:
                back_tracking([x+d[i][0], y+d[i][1]])
                # 스택 상단의 함수 호출로 도착점을 발견하고 다시 돌아온 경우라면 스택에 남아있는 모든 함수의 동작을 중단하고 빠져나옴
                if result == 1:
                    return
                stack.pop()  # 지나온 경로를 되돌아가기


T = int(input())
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    stack = []
    a, b = 0, 0
    # 시작점은 2, 도착점은 3, 통로는 0 -> 시작점에서 도착점에 도달 가능하면 1을 출력
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                a, b = i, j
    result = 0
    back_tracking([a, b])
    print(f'#{tc} {result}')