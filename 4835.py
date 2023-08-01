# 구간합 구하기
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    D = [0] * (N + 1) # 구간합을 저장할 리스트
    arr2 = []
    max_v = 0

    for i in range(1, N):
        D[0] = 0
        D[1] = arr[0]
        D[i + 1] = D[i] + arr[i]

    min_v = D[M]
    for i in range(M, N + 1):

        total = D[i] - D[i - M]
        if total > max_v:
            max_v = total
        if total < min_v:
            min_v = total

    print(f'#{tc} {max_v - min_v}')

# 다른 풀이 - 오답 출력됨, 코드 수정할 것
#  T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     new_arr = []
#
#     for j in range(N - M + 1): # 입력받은 리스트 내에서 가능한 구간합의 개수만큼 반복
#         result = 0
#         for k in range(j, j + M): # M의 범위로 구간합 구해서 저장하기
#             result += arr[k]
#             new_arr.append(result)
#
#     max_arr = max(new_arr)
#     min_arr = min(new_arr)
#
#     print(f'#{tc} {max_arr-min_arr}')
