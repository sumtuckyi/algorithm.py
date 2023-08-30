# 키가 있으면 1, 없으면 0을 반환하는 함수
def f(i, N, key, arr):
    if i == N:
        return 0
    elif arr[i] == key:
        return 1
    else:
        return f(i+1, N, key, arr)

N = 5
A = [1, 2, 3, 4, 5]
key = 10
print(f(0, N, key, A))

# 선택정렬함수를 재귀적 알고리즘으로 작성
'''
시작 인덱스, 리스트의 길이, 리스트를 인자로 전달받아 
선택 정렬을 수행
구간 내에서의 최솟값을 저장해서 위치 이동 -> 재귀 호출
'''

# 완전탐색
# from itertools import permutations
#
# cards = list(map(int, input().split()))
# new_list = list(permutations(cards, len(cards)))
# new_set = set(new_list)
# #print(new_list)
# cards2 = [list(t) for t in new_set]
# print(cards2)
# for i in cards2:
#     isTrue1 = i[0] + 1 == i[1] and i[0] + 2 == i[2]
#     isTrue2 = i[3] + 1 == i[4] and i[3] + 2 == i[5]
#     if (len(set(i[:2+1])) == 1 and len(set(i[3:])) == 1) or (len(set(i[:2+1])) == 1 and isTrue2) or (len(set(i[3:])) == 1 and isTrue1) or (isTrue1 and isTrue2):
#         print('baby-gin!')

'''
순서화된 집합에 대해 반복적인 작업을 수행해야하는 경우가 많다.
주어진 상황에서 최적인 부분집합을 구해야 하는 경우가 많다. 
ex)먼저 순열을 생성하고 각 경우마다 조건을 만족하는지 확인
1.사전적 순서
2.최소한의 변경
3.바이너리 카운팅으로 부분집합 생성
'''
# arr = [i for i in range(1, 10+1)]
# N = len(arr)
# used = [0]*N
# def perm(level, path):
#     if level == N:
#         print(path)
#         # 요구되는 작업 수행
#         return
#     else:
#         for i in range(N):
#             if used[i] == 0:
#                 used[i] = 1
#                 perm(level + 1, path + [i])
#                 used[i] = 0  # 원상복구
#
# perm(0, [])

#
def check(lst): # 리스트를 받아 베이비진 조건을 만족하는지 확인
    pass


def permutation(level, path, N):  # 주어진 집합에서 N개를 고르는 순열
    global result
    if level == N:
        c = path.copy()
        if check(c): # baby-gin이면
            result = 1
        print(c)
        return result
    else:
        for i in range(len(card)):
            if used[i] == 0:
                used[i] = 1
                permutation(level+1, path + [card[i]], N)
                used[i] = 0


card = list(map(int, input().split()))  # 6장의 카드
used = [0] * 6
result = 0
print(permutation(0, [], 3))