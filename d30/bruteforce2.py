#(출발지점, 도착지점)
# N은 3이상 10이하
# 사무실에서 출발하여 모든 관리구역을 각 한 번씩만 돌고 돌아와야함
# 관리구역이 10개인 경우 1-(2부터 10까지 순열)-1의 경로가 된다.
# 예시) 1-2-3-4-5-6-7-8-10-9-1

def back_trakcking(level, total, path):
    if level == N-1:
        lst.append(total+land[path[-1]-1][0])
        return

    for i in range(2, N + 1): # 2부터 N까지의 순열
        if visited[i] == 0:
            if total + land[path[-1]-1][i-1] < min(lst):
                visited[i] = 1
                back_trakcking(level+1, total + land[path[-1]-1][i-1], path + [i])
                visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    land = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N+1)
    lst = [1000000]
    back_trakcking(0, 0, [1])
    print(f'#{tc} {min(lst)}')


#
def cart(cur, start, total):  # 깊이, 출발 구역(직전에 방문한 구역)
    global result
    if cur == n-1:
        result = min(result, arr[start][0] + total)
        return
    for i in range(1, n):
        if visited[i] == 0 and start != i: # 아직 방문하지 않았고, 출발 구역과 다른 경우에만만
           visited[i] = 1
            cart(cur + 1, i, total + arr[start][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n+1)
    result = float('inf')
    back_trakcking(0, 0, 0)
    print(f'#{tc} {result}')
