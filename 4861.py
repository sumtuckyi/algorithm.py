# 회문 찾아서 출력하기
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

    print(f'#{tc} {result}')

# 다른 풀이
def find_p(N, M, arr):
    for i in range(N):
        for j in range(N-M+1):
            h = arr[i][i:i+M]
            v = [arr[k][i] for k in range(j, j+M)]

            if h == h[::-1]:
                return h
            if v == v[::-1]:
                return v

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = find_p(N, M, arr)
    print(f'#{tc}', ''.join(result))