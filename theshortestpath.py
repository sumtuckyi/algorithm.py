# 회사에서 출발 -> 모든 고객의 집을 방문 -> 집 도착

T = int(input())

def dfs(level, total):
    global min_d
    if level == N+1:  # 모든 고객을 다 방문하고 집으로 돌아온 경우
        if min_d > total:  # 그때의 이동거리와 기존 최단거리를 비교
            min_d = total
        return
    elif total > min_d:
        return
    else:
        for i in range()


for tc in range(1, T+1):
    N = int(input())  # 고객의 수
    coords = list(map(int, input().split()))
    c = [coords[0], coords[1]]  # 회사의 좌표
    h = [coords[2], coords[3]]  # 집의 좌표
    for i in range(4, 2*N+4):

    min_d = float('inf')  # 최단거리 초기화






#
def back_tracking(level, total):
    global min_v
    if level == N:
        if min_v > total:  # 계산한 값이 기존의 최솟값보다 작으면 갱신
            min_v = total
            return
    elif total >= min_v:  # 중간까지 계산한 값이 이미 최솟값과 같거나 큰 경우
        return
    else:
        for j in range(level, N):
            A[level], A[j] = A[j], A[level]
            back_tracking(level + 1, total+arr[level][A[level]-1])
            A[level], A[j] = A[j], A[level]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    min_v = (9*N)+1
    arr = [list(map(int, input().split()))for _ in range(N)]
    A = [i for i in range(1, N+1)]
    back_tracking(0, 0)
    print(f'#{tc} {min_v}')