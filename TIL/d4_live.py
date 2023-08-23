# 6485
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stops = [int(input()) for _ in range(P)]
    count = [0] * 5001
    result = []

    for i in range(N):
        for j in range(lines[i][0], lines[i][1] + 1):
            count[j] += 1

    for i in stops:
        result.append(count[i])

    print(f'#{tc}', *result)



'''
lines를 배열로 받지 않고 입력 받은 동시에 바로 반복문의 인자로 전달하는 방법
for i in range(N):
    A, B = map(int, input().split())
    for j in range(A, B + 1):
        count[j] += 1
'''

'''
문제에서 요구하는 형식으로 출력하기
print(f'#{tc}', end = ' ')
for i in stops:
    print(cnt[x], end = ' ')
print()
'''