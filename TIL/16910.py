# 원 안에 속하는 격자점 개수 구하기 - 공식 이용하기
from math import sqrt
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [(i, j) for i in range(-N, N + 1) for j in range(-N , N + 1)]
    result = 0

    for i, j in arr:
        if sqrt(i**2 + j**2) <= N:
            result += 1

    print(f'#{tc} {result}')

