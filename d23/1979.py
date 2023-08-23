# 흰색이 1, 검은색이 0

T = int(input())


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0  # 단어가 들어갈 수 있는 자리의 개수
    tof = False  # 이전칸이 빈칸인 경우 True
    # 가로 탐색
    for i in range(N):
        cnt = 0  # 연속한 빈칸의 개수
        for j in range(N):
            if puzzle[i][j]:
               tof = True
               cnt += 1
            else:
                tof = False
                if cnt == K:
                    ans += 1
                cnt = 0
            if j == N-1 and cnt == K:  # 행을 끝까지 돈 경우
                ans += 1
    # 세로 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i]:
                tof = True
                cnt += 1
            else:
                tof = False
                if cnt == K:
                    ans += 1
                cnt = 0
            if j == N - 1 and cnt == K:  # 열을 끝까지 돈 경우
                ans += 1
    print(f'#{tc} {ans}')

#