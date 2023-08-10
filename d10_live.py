# recursive func
def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

cnt = 0
print(fibo(30), cnt)

# memoization을 재귀적 구조에 사용
def fibo2(n):
    global cnt2
    cnt2 += 1
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibo2(n-1) + fibo2(n-2)
        return memo[n]

N = 30
memo = [0]*(N+1)
memo[0] = 0
memo[1] = 1
cnt2 = 0
print(fibo2(N), cnt2)

# DP
def fibo3(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibo3(100))

# DFS
'''
시작점 방문
방문여부 배열의 값 바꿔줌
while
    if 시작점의 인접 정점 중 방문 안 한 정점이 있다면
        시작점을 스택에 푸시
        시작점을 방문점으로 재할당
        방문점의 방문여부 값을 바꿔줌
    else
        if 스택이 비어있지 않다면
            스택의 최상단 값 삭제하고 그 값을 시작점으로 할당
        else 즉, 비어있다면
            모든 노드를 다 돈 것이므로 탐색 종료
'''


'''
# 7개의 노드와 8개의 간선
7 8  
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7  
'''
#인접행렬이나 인접 리스트로 입력값 저장하기

V, E = map(int, input().split())  # 1번 부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

def dfs(n, V, adj_m):  #V개의 정점을 가진 그래프에서 n에서 탐색 시작
    stack = []  # stack생성
    visited = [0] * (V+1)  # visited 생성
    visited[n] = 1 # 시작점 방문 표시
    print(n)  # do[n]
    while True:
        # 현재 정점 n에 인접하고 미방문한 정점 찾기
        for w in range(1, V+1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)  # push(n), n = w
                n = w
                print(n)  # 갱신된 시작점 표시
                visited[n] = 1
                break  #  인접한 미방문 정점을 찾았으므로 for문을 종료
        else:  # 현재 정점 기준으로 인접한 정점 중 미방문 정점이 없을 때
            if stack:  # 스택이 비어있지 않은 경우(지나온 정점이 남아있는 경우)
                # 스택의 최상단 값을 새로운 시작점으로
                n = stack.pop()
            else:  # 스택이 비어있다면 모든 정점을 다 순회한 것이므로 while문 종료
                break

dfs(1, V, adj_m)