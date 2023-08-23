# 백트래킹 문제
# 순열을 구해서 배열에서 해당하는 좌표의 값을 확인
# 재귀 호출시 현재까지의 합을 인자로 전달하여 계산의 중복을 줄이는 방향으로..
# def back_tracking(level, total):
#     global min_v
#     if level == N:
#         if min_v > total:  # 계산한 값이 기존의 최솟값보다 작으면 갱신
#             min_v = total
#         else:
#             return
#         return
#
#     for j in range(level, N):
#         A[level], A[j] = A[j], A[level]
#         back_tracking(level + 1, total+arr[level][A[level]-1])
#         A[level], A[j] = A[j], A[level]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     min_v = (9*N)+1
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     A = [i for i in range(1, N+1)]
#     back_tracking(0, 0)
#     print(f'#{tc} {min_v}')



#
# def back_tracking(level, n, t):
#     global min_v, cnt
#     if level == n:
#         if min_v > t:
#             min_v = t
#         return
#     else:
#         for j in range(level, n):
#             A[level], A[j] = A[j], A[level]
#             new_total = t + arr[level][A[level]-1]
#             if new_total < min_v:
#                 back_tracking(level + 1, n, new_total)
#                 A[level], A[j] = A[j], A[level]
#                 return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     min_v = (9*N)+1
#     cnt = 0
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     A = [i for i in range(1, N+1)]
#     back_tracking(0, N, 0)
#     print(f'#{tc} {min_v}')
#     print(cnt)


def back_tracking(level, total):
    global min_v
    if level == N:
        if min_v > total:  # 계산한 값이 기존의 최솟값보다 작으면 갱신
            min_v = total
            return
    elif total >= min_v:  # 중간까지 계산한 값이 이미 최솟값과 같거나 큰 경우
        return
    else:
        for j in range(level, N):
            A[level], A[j] = A[j], A[level]
            back_tracking(level + 1, total+arr[level][A[level]-1])
            A[level], A[j] = A[j], A[level]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    min_v = (9*N)+1
    arr = [list(map(int, input().split()))for _ in range(N)]
    A = [i for i in range(1, N+1)]  # 순열을 만들기 위한 리스트
    back_tracking(0, 0)
    print(f'#{tc} {min_v}')

# 다른 풀이
def DFS(idx, now_sum):
    global min_sum
    if now_sum >= min_sum:
        return
    if idx == N:  # 모든 행을 선택한 경우
        if min_sum > now_sum:  # 현재합이 최소합보다 작으면 갱신
            min_sum = now_sum
        return
    for i in range(N):
        if not used[i]:  # 아직 선택하지 않은 열이라면
            used[i] = 1  # 선택하여
            DFS(idx+1, now_sum+arr[idx][i])  # 최솟값 여부 판단(현재 level(행)에서 아직 선택되지 않은 열에 한해서 선택)
            used[i] = 0  # 원상복구(백트래킹)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    min_sum = 21e8
    arr = [list(map(int, input().split()))for _ in range(N)]
    used = [0]*N
    DFS(0, 0)
    print(f'#{tc} {min_sum}')