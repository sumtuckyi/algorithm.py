# 십진수-이진수 변환
# N = int(input())

# def binary(n):
#     # 종료조건
#     if n == 0:
#         return '0'
#     elif n == 1:
#         return '1'
#     else:  # 몫은 0이나 1이 아닌 한 계속 나누고 나머지가 발생하면(여기선 1) 문자열로 변환하여 연산
#         return binary(n // 2) + str(n % 2)
#
# print(binary(2))
# print(binary(15))

# 콜라츠 추측
# N = int(input())
#
# def func(N, cnt):
#     # 종료 조건
#     if N == 1:
#         print(cnt)
#         return
#     if N % 2 == 0:  # N이 짝수인 경우 함수 호출하고 카운트해주기
#         func(N // 2, cnt + 1)
#     else:  # N이 1이 아닌 홀수인 경우 함수 호출
#         func((N * 3) + 1, cnt + 1)
#
# func(6, 0)

# 각 자릿수의 합 구하기
# N = int(input())
#
# def sum_nums(n):
#     if n == 0:  # (n // 10) == 0과 동일
#         return n
#     else:
#         return sum_nums(n // 10) + (n % 10)
#
# print(sum_nums(N))


# 중복순열
# from itertools import permutations
#
#
# def perm(cards, n):
#     if len(cards) == 1:
#         return 5
#     else:
#         arr = list(permutations(cards, n -1))
#         new_set = set(arr)
#         set_arr = list(new_set)
#         total = 0
#         for i in range(set_arr):
#             cnt = 0
#             for j in cards:
#                 if i[n-2]-3 <= j <= i[n-2]+3:
#                     cnt += 1
#                 total += cnt
#         return total


card = list(input())
path = [0] * 4  # 카드를 총 4장 뽑는 경우
cnt = 0

def card_cnt(level):
    global cnt
    # 4장의 카드를 뽑은 경우에 경우의 수 증가
    if level == 4:
        cnt += 1
        return  # 함수 스택에서 바로 아래의 스택에서 호출된 함수로 되돌아간다.

    for i in range(5):  # 5개의 카드 중 하나를 선택
        path[level] = card[i]  # level은 함수 재귀 호출시마다 1씩 증가
        # 백트래킹 기법, 연속으로 뽑는 카드의 차이가 4 이상이면 더이상 반복문을 수행하지 않고(즉 다음에 올 카드를 고려하는 과정을 생략) 다음 카드를 선택(다음 반복으로 넘어감)
        if int(path[level]) - int(path[level-1]) >= 4:  # level이 0이면 path[-1]과 대소를 비교하게됨..
            continue
        if int(path[level-1]) - int(path[level]) >= 4:
            continue
        card_cnt(level + 1)  # 깊이를 추가하여 함수의 코드 블럭을 실행하고 작업이 완료되면 다시 작업 스택 최상단의 함수로 돌아옴

card_cnt(0)
print(cnt)
