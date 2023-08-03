# 구간합 이용하기

n = int(input())
a = list(map(int, input().split()))
prefix_sum = [0] * 20001
map = {}
answer = 0

map[0] = 1
for i in range(n):
    prefix_sum[i] = a[i]
    if i != 0:
        prefix_sum[i] += prefix_sum[i - 1]
    if prefix_sum[i] in map:  # prefix_sum[i]와 일치하는 키가 map에 존재하는지
        answer += 1
        map.clear()
        map[prefix_sum[i-1]] = 1
    map[prefix_sum[i]] = 1

d = 1
print(answer)
