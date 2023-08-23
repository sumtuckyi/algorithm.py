# 문자열 찾기
T = int(input())

for tc in range(1, T + 1):
    N = input()
    M = input()
    result = 1 if N in M else 0
    print(f'#{tc} {result}')
    # key_string = list(input())
    # string = list(input())
    # for i in range((N - 1) - (M - 1))


# 멤버십 연산자를 사용하지 않는 경우
T = int(input())

for tc in range(1, T + 1):
    N = input()
    M = input()
    result = 0
    for i in range(len(M) - len(N) + 1):
        if M[i:i+len(N)] == N:
            result = 1

    print(f'#{tc} {result}')
