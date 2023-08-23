def bfs():
    q = [(sx, sy, 0, 0)]  # 출발점과 현재 버스 번호, 누적 환승횟수를 큐에 삽입
    # visited[sy][sx] = 1  # 방문했음을 표시
    while q:
        cx, cy, cb, cnt = q.pop(0)  # 탐색 시작점, 버스 번호, 환승횟수
        visited[cy][cx] = 1  # 방문했음을 표시
        buses = lines[cy][cx]  # 현 지점에서 탈 수 있는 버스 종류
        if len(buses) > 1:
            for i in range(1, len(buses)):  # 순차적으로 타고 가봄
                cb = i  # 현재 탄 버스의 번호
                for a, b in d:
                    if 1 <= cx + a <= m and 1 <= cy + b <= n:  # 지도의 범위 내에 있고
                        if not visited[cy + b][cx + a]:  # 아직 방문하지 않았는데
                            print(cy + b, cx + a)
                            if (cy + b, cx + a) == (ey, ex):  # 해당 지점이 도착점인 경우
                                return cnt
                            elif cb in lines[cy + b][cx + a]:  # 해당 지점을 지나가는 경우
                                q.append((cy + b, cx + a, cb, 0))
                            else:  # 해당 지점을 지나가지 않는 경우
                                cnt += 1  # 환승해야함
    return 1

m, n = map(int, input().split())  # 맵의 크기 (열의 크기, 행의 크기)
k = int(input())  # 버스의 수
lines = [[[0] for _ in range(m+1)] for _ in range(n+1)]
visited = [[0]*(m+1) for _ in range(n+1)]
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for i in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            lines[y][x].append(b)
sx, sy, ex, ey = map(int, input().split())

print(bfs())

'''
[
 [[0], [0], [0], [0], [0], [0], [0], [0]], 
 [[0], [0, 2], [0, 1, 2, 7], [0, 2], [0, 2], [0, 2], [0], [0]], 
 [[0], [0], [0, 1, 7], [0, 3], [0, 3], [0, 3], [0, 3], [0]],
 [[0], [0], [0, 7], [0], [0], [0], [0], [0, 6]], [[0], [0],
 [0, 7], [0], [0], [0], [0], [0, 6]], [[0], [0, 5], 
 [0, 7, 5], [0, 5, 8], [0, 5, 8], [0, 5, 8], [0, 5, 8], [0, 6, 5]],
 [[0], [0], [0, 7], [0], [0], [0], [0], [0, 6]]
]

'''