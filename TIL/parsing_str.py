T = int(input())  # 문자열의 길이
N = input()  # 문자열
# 1
arr = [int(i) for i in N]  # [1, 2, 3, 5]
arr2 = list(N)  # ['1', '2', '3', '5']
print(arr2)
print(sum(arr))
# 2
total = 0
for i in N:
    total += int(i)
print(total)
# 3
result = 0
n = int(N)
for _ in range(T):
    result += (n % 10)
    n //= 10
print(result)