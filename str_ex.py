T = int(input())

for tc in range(1, T + 1):

    n, m = list(map(int, input().split(':')))

    # a, b = min(N), max(N)
    # max_v = 0
    # for i in range(1, a + 1):
    #     if a % i == 0 and b % i == 0:  # i가 두 수의 공약수인 경우
    #         max_v = i

    # 유클리드 호제법을 이용한 죄대공약수 반환 함수
    def GCD(a, b):
        if b % a:
            return GCD(b % a, a)
        else:
            return a

    max_v = GCD(n, m)
    print(f'{n//max_v}:{m//max_v}')