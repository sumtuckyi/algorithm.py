# x2 또는 +1 연산을 통해 b를 만들 수 있다면 그때의 최소 연산횟수를 구하고, 불가능하면 -1을 출력
# b는 a보다 반드시 크다
# ax2와 b를 비교하여 b가 더 큰 경우->
# (반복)a에 2를 한 번 더 곱하여 다시 대소비교 -> a가 더 커진 경우/여전히 b가 더 큰 경우 -> 다시 2를 나눠준 뒤에 차이만큼 1을 더해서 b를 만들어줌/a에 2를 곱한 뒤 반복
# 다른 방법
# n*2를 하거나 n+1을 한다 -> (곱, 합 => 2*a+1), (합, 곱 => (a+1)*2), (곱, 곱 => a*2*2), (합, 합 => a+1+1)
# 2 -> 5/6/8/4
a, b = map(int, input().split())
dp = [0]*1_000_000_000
temp = a
cnt = 1
plus = temp+1
mul = temp*2
while True:
    if plus == b or mul == b:
        break
    else:
        if dp[plus] == 0:
            dp[plus] = cnt
        if dp[mul] == 0:
            dp[mul] = cnt
    plus += 1
    mul *= 2
    cnt += 1
print(cnt)

#
cnt = 0
while b >= a:
    if b == a:
        print(cnt)
        exit()
    if b % 10 == 1:  # 1의 자리가 1인 경우, 1을 제거
        b //= 10
    elif b % 2 == 0:  # 짝수인 경우, 2로 나눈다
        b //= 2
    else:  # 위의 두 조건에 해당하지 않으면 b를 만들 수 없다.
        print(-1)
        exit()
    cnt += 1
print(-1)