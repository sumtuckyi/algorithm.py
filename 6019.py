# 공식 찾아서 이용하는 문제
T = int(input())


for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)
    d = time * F

    print(f'#{tc} {d}')