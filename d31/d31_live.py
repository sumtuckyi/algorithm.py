# 조합
# 재귀호출을 사용한 조합 생성
# def ncr(n, r):  # n개 중에 r개의 원소를 뽑는 함수
#     if r == 0:
#         print(tr)
#     elif n < r:  # 남은 원소보다 많은 원소를 선택해야 하는 경우
#         return
#     else:
#         tr[r-1] = a[n-1]
#         ncr(n-1, r-1)  # n-1번째 원소를 뽑는 경우
#         ncr(n-1, r)  # n-1번째 원소를 뽑지 않는 경우
#
#
# a = [1, 2, 3, 4, 5]
# N = 5
# R = 3
# tr = [0] * R
# ncr(N, R)

#
'''
경우의 수만 필요한 경우(파스칼의 삼각형으로 재귀적으로 해결 가능) / 실제 각 경우의 수마다의 조합의 원소가 필요한 경우
n개의 원소 중 r개를 고르는 경우,
첫번째로 선택되는 원소는 0부터 n-r번 인덱스까지(j,k로 선택될 원소를 남김) 
두번째로 선택되는 원소는 i+1부터 n-r+1번 인덱스까지(k로 선택될 원소를 남김)
세번째로 선택되는 원소는 j+1부터 n-r+2번 인덱스까지 선택 가능
...

r이 3까지만 되어도 3중 for문으로 조합을 생성할 수 있다.
r이 그보다 더 큰 경우에는..?

'''


# def ncr2(n, r, s):  # n개에서 r개를 고르는 조합, s는 선택할 수 있는 구간의 시작
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = A[i]
#             ncr2(n, r-1, i+1)
#
#
# A = [1, 2, 3, 4, 5, 6]
# N = len(A)
# R = 2
# comb = [0]*R
# ncr2(N, R, 0)

# 동적 프로그래밍으로 조합 구현하기
# T = int(input())
#
# for _ in range(T):
#     N, M = map(int, input().split())
#     DP = [[0 for _ in range(M + 1)] for _ in range(M + 1)]
#
#     for i in range(M + 1):
#         DP[i][0] = 1
#         DP[i][i] = 1
#         DP[i][1] = i
#
#     for i in range(1, M + 1):
#         for j in range(1, i):
#             DP[i][j] = DP[i - 1][j - 1] + DP[i - 1][j]
#
#     print(DP[M][N])

# 부분집합의 합 문제
# n개의 원소를 가지는 집합의 모든 부분 집합 중 원소의 합이 m이 되는 경우를 모두 출력
# 바이너리 카운팅 또는 재귀로 구할 수 있다.
# i번째 원소를 포함시키거나 포함시키지 않거나 하는 선택을 n번 연속으로 한다.
# n번째 선택이후에 부분집합이 완성되면 조건에 부합하는지 확인


# def subset(i, N):
#     if i == N:
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += arr[j]
#         if s == 0:  # 합이 0이 되는 부분집합을 구하고자 함
#             for j in range(N):
#                 if bit[j]:
#                     print(arr[j], end =' ')
#             print()
#     else:
#         bit[i] = 1
#         subset(i+1, N)
#         bit[i] = 0
#         subset(i+1, N)
#     return
#
# arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# N = len(arr)
# bit = [0] * N
# subset(0, N)

#
def subset(i, N, s):
    if i == N:  # 부분집합이 완성되면(집합의 크기가 N이므로)
        # 이 경우에는 부분집합을 완성시킨 다음 계산을 하는 작업을 생략할 수 있음
        # s = 0
        # for j in range(N):
        #     if bit[j]:
        #         s += arr[j]
        if s == 0:  # 합이 0이 되는 부분집합을 구하고자 함
            for j in range(N):
                if bit[j]:
                    print(arr[j], end =' ')
            print()
    else:
        bit[i] = 1
        subset(i+1, N, s+arr[i])  # i포함
        bit[i] = 0
        subset(i+1, N, s)  # i 미포함
    return

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N
subset(0, N, 0)

# greedy
# 그리디 알고리즘의 유형에 해당하면 그렇게 접근하고 그렇지 않으면 완전탐색 또는 dp으로 접근해야 최적해를 보장할 수 있다.
# 그러나 데이터의 크기가 커지면 완전탐색으로는 과도한 시간이 걸리기 때문에 동적 프로그래밍을 이용해야 한다.
# 예를 들어 0-1knapsack 유형은 탐욕법으로 최적해를 구할 수 없음
