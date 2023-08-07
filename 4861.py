T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # M은 회문의 길이
    b = [input() for _ in range(N)]

    # 행탐색
    result = 0
    for j in range(N):
        for i in range(N-M+1):
            s = b[j][i:i+M]
            if s == s[::-1]:
                result = s

    # 열탐색
    for i in range(N):
        for j in range(N-M+1):
            s1 = ''
            for k in range(M):
                s1 += b[j+k][i]

            if s1 == s1[::-1]:
                result = s1

    print(f'#{tc} {result}')    print(result)