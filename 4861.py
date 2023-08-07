T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # M은 회문의 길이
    b = [input() for _ in range(N)]

    # 행탐색
    cnt = 0
    result = ''
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M//2):
                if b[i][j + k] == b[i][j+M-1+k]:
                    cnt += 1
                    result += b[i][j]
                    print(result)
                    if cnt == M // 2:
                        break
                else:
                    cnt = 0
                    result = ''

        # 열탐색
    print(result)