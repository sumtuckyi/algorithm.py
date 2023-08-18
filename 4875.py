# 미로에서 출발점과 도착점이 주어지면 탈출이 가능한지 판별하는 함수 

def back_tracking(start):  # 시작점(리스트)을 인자로 전달
    global result
    if maze[start[0]][start[1]] == '3':  # 탐색을 시작할 기준점이 도착점이 되면 함수를 종료
        result = 1
        return
    # 종료조건이 참이 아닌 경우에 수행할 내용
    stack.append(start)
    x, y = start
    for i in range(4):  # 우하상좌 순으로 탐색
        # 범위 내에 있고 벽(1)이 아닌 경우
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


#
def maze():
    while stack:
        y, x = stack.pop()
        arr[y][x] == -1  # 지나간 길 표시
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 3:
                    return 1
                elif arr[ny][nx] == 0:  # 지나간 길은 -1로 표시되기 때문에 탐색하지 않는다.
                    stack.append((ny, nx))
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input()))for _ in range(N)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                stack = [(i, j)]
                break
    print(f'#{tc} {maze()}')