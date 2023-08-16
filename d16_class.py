'''
f(i, N) # i는 현재 단계, N은 목표
if i == N: # 재귀호출된 함수의 종료 조건
    return
else:
    f(i+1, N)
'''

# 부분집합의 합 구하기 : 반복문 대신 재귀 사용하기
# def copy_arr(i, N, s):
#     if i == N:  # 배열의 인덱스 범위를 벗어나면 함수 종료
#         print(bit, end=' ')
#         print(f' : {s}')
#         return
#     else:
#         bit[i] = 1  # 부분집합에 arr[i]포함
#         copy_arr(i+1, N, s+arr[i])
#         bit[i] = 0  # 부분집합에 arr[i] 미포함
#         copy_arr(i+1, N, s)
#         return
#
#
# arr = [i for i in range(1, 3+1)]  # 전체 집합
# n = len(arr)
# bit = [0]*n
# copy_arr(0, n, 0)

# 연습문제 : 부분집합의 합이 k가 되는 부분집합을 구하여라.
# def copy_arr(i, N, s, t):
#     global cnt
#     cnt += 1
#     if s == t:
#         print(bit, end='\n')
#         return
#     elif i == N:  # 배열의 인덱스 범위를 벗어나면 함수 종료
#         return
#     elif s > t:
#         return
#     else:
#         bit[i] = 1  # 부분집합에 arr[i]포함
#         copy_arr(i+1, N, s+arr[i], t)
#         bit[i] = 0  # 부분집합에 arr[i] 미포함
#         copy_arr(i+1, N, s, t)
#         return
#
#
# arr = [i for i in range(1, 10+1)]  # 전체 집합
# n = len(arr)
# bit = [0]*n
# cnt = 0
# t = 10
# copy_arr(0, n, 0, 10)
# print(cnt)

# 순열 구하기
def perm(i, N):
    global cnt
    if i == N:
        print(A)
        cnt += 1
        return
    else:
        # 자기 자신부터 오른쪽 끝까지
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            perm(i+1, N)
            A[i], A[j] = A[j], A[i]  # 재귀함수를 호출하기 전의 상태로 복구


cnt = 0
A = [1,2,3,4,5]
perm(0, 5)

print(cnt)

# 분할정복
# def f1(b, e):
#     global cnt1
#     if b == 0:
#         return 1
#     r = 1
#     for i in range(e):
#         cnt1 += 1
#         r *= b
#     return r
#
#
# def f2(b, e):
#     global cnt2
#     if b == 0 or e == 0:
#         return 1
#     if e % 2:
#         r = f2(b, (e-1)//2)
#         cnt2 += 1
#         return r*r*b
#     else:
#         r = f2(b, e//2)
#         cnt2 += 1
#         return r*r
#
# cnt1 = 0
# cnt2 = 0
# print(f1(2, 20), cnt1)
# print(f2(2, 20), cnt2)