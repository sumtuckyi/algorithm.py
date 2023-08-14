# N, S = map(int, input().split())
# seq = list(map(int, input().split()))
#
# cnt = 0
#
# def back_tracking(depth, total):
#     global cnt
#     answer = []
#     if total == S: # 부분집합의 합이 S면 카운트하고 재귀 함수 종료
#         cnt += 1
#         return
#     elif depth == N - 1:
#         return
#
#     for i in range(N):
#         if seq[i] in answer:
#             continue
#         else:
#             answer.append(seq[i])
#             print(answer, depth, '원소를 넣었을 때 합이 0인지 확인')
#             back_tracking(depth + 1, sum(answer))
#             answer.pop()
#             answer.append(0)
#             print(answer, '원소를 뺐을 때 합이 0인지 확인')
#             back_tracking(depth, sum(answer))
#
#
# back_tracking(0, float('Inf'))
# print(cnt)


# 부분수열의 크기가 조건에 맞는 경우에 한해 인자로 전달받은 순서의 수열을 포함하는 경우와 그렇지 않은 경우에 대해 조건을 만족하는지 확인하여 카운트
def back_tracking(idx, sum):
    global answer
    # 종료 조건
    if idx >= n:  # 깊이가 수열의 크기를 넘어가면 함수를 종료
        return

    sum += arr[idx]  # 수열에서 현재 인덱스의 값을 포함하는 부분수열의 합
    # 문제의 제약 조건
    if s == sum:  # 부분수열의 합이 목표한 값과 같은 경우 카운트
        answer += 1
    back_tracking(idx+1, sum-arr[idx])  # 부분수열에 현재 인덱스의 값이 포함되지 않는 경우, 다음 순서의 원소에 대해 연산을 수행
    back_tracking(idx+1, sum)  # 부분수열에 현재 인덱스의 값이 포함되는 경우, 다음 순서의 원소에 대해 연산을 수행


n, s = map(int, input().split())
arr = list(map(int, input().split()))  # 1 2 -1 3 7 -2
answer = 0
back_tracking(0, 0)  # 수열의 첫 번째 원소를 포함하는 부분수열과 포함하지 않는 부분수열에 대해 순차적으로 조건을 만족하는지 확인함
print(answer)