N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0
total2 = 0
for i, j in zip(range(N), range(N)): # 좌상향 대각선의 합 구하기
    total += arr[i][j]

for i in range(N): # 우상향 대각선의 합 구하기
    total2 += arr[i][2 - i]

print(total)
print(total2)