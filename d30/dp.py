# 동적 프로그래밍으로 최소합 구하기


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf')] * N for _ in range(N)]

    dp[0][0] = cost[0][0]

    for i in range(N):
        for j in range(N):
            if i-1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + cost[i][j])
            if j-1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + cost[i][j])

    print(f'#{tc} {dp[-1][-1]}')

# 피보나치 수열
# f(n) = f(n-1) + f(n-2), f(0) = 0, f(1) = 1
N = int(input())
# dp 초기화
dp = [-1] * 36
dp[1] = 0
dp[2] = 1

def fibo(n):
    if dp[n] != -1:  # n의 값이 이미 계산되어 있는 경우
        return dp[n]
    else: # 아직 계산 되지 않은 경우
        dp[n] = fibo(n - 1) + fibo(n - 2)  # 계산하고
        return dp[n]
print(fibo(N))