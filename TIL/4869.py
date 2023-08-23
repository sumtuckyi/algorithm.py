# 종이붙이기
T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 가로는 20으로 고정, 세로 길이

    def cal_cases(n):
        if n == 10:
            return 1
        elif not n % 20:  # N이 20의 배수인 경우
            return cal_cases(n - 10) * 2 + 1
        else:  # N이 20의 배수가 아닌 경우
            return cal_cases(n - 10) * 2 -1

    result = cal_cases(N)
    print(f'#{tc} {result}')

# 점화식 찾아서 접근
T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 가로는 20으로 고정, 세로 길이


    def func(n):
        if n == 10:
            return 1
        elif n == 20:
            return 3
        else:
            return func(n-10) + (func(n-20) * 2)

    num = func(N)
    print(f'#{tc} {num}')