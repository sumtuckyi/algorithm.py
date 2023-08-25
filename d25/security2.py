def solve():
    ans = 0  # 서비스 제공이 가능한 집의 수의 최댓값
    K = N+1  # 가능한 서비스 영역 크기의 최댓값
    for k in range(K, 0, -1):  # N+1의 범위에서 1의 범위까지
        cost = k*k + (k-1)*(k-1)
        for y in range(N):
            for x in range(N):
                cnt = 0 # 현재 위치에서 서비스 가능한 집의 수
                for hy, hx in houses:  # 마을의 모든 집 탐색
                    dist = abs(hy-y) + abs(hx-x)
                    if dist < k:
                        cnt += 1
                if M*cnt >= cost:
                    ans = max(ans, cnt)
        if ans != 0:
            return ans
    return 0  # 해당 k에서 범위 내에 있는 집만으로는 이윤이 나지 않아 서비스 제공이 불가한 경우


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 마을 정보
    houses = []  # 집의 좌표
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                houses.append((i, j))
    result = solve()
    print(f'#{tc} {result}')