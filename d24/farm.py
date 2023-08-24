# n회 반복
'''
i -> 0~(N-1)까지 n행
1개 : 0 + (N-1)
3개 : 1 + (N-2)
더하면 N-1이 되는 행은 동일한 너비로 수확
n = 7인경우
3,3
2,4
1,5
0,6
1,5
2,4
3,3

N // 2행은 N의 너비로 수확
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = list(list(map(int, input())) for _ in range(N))
    total = 0
    if N == 1:  #농장의 크기가 1인 경우
        total = farm[0][0]
    else:
        total = farm[0][N//2] + farm[N-1][N//2]
        for i in range(1, N-1):  # 1부터 N-2행까지
            for j in range(abs(N//2-i), ((N-1)-abs(N//2-i)+1)):
                total += farm[i][j]
                print(i, j, farm[i][j])
    print(f'#{tc} {total}')


#
start, end = N//2, N//2
result = 0
for i in range(N):
    for j in range(start, end + 1): # 열 순회
        result += arr[i][j]
    if i < N//2:  # 농장의 상단부분
        start -= 1
        end += 1
    else:  # 농장의 하단부분
        start += 1
        end -= 1
    print(f'#{tc} {result}')