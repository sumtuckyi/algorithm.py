# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

# 부분집합 생성하기 2
# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
#
# def subset(arr1):
#     for i in range(1<<n):  # 요소가 n개일 때 부분집합의 개수 만큼 반복해서 집합 생성
#         for j in range(n):
#             if i & (1<<j):  # i의 j번째 비트가 1인지 확인
#                 print(arr1[j], end= ", ")
#         print()
#
# subset(arr)
A = [i for i in range(1, 12 + 1)]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    subsets = []  # 모든 부분집합을 구해서 담을 리스트


    def subset(arr): # 부분집합 생성함수
        for i in range(1 << 12): # 집합의 원소 수 만큼
            subset1 = [] # 개별 부분집합
            for j in range(12):
                if i & (1 << j):  # i의 j번째 비트가 1이면
                    subset1.append(arr[j])  # 리스트[j]를 부분집합의 원소로 추가
            subsets.append(subset1)  # 구해진 하나의 부분집합을 리스트에 추가


    subset(A)  # 집합 A의 모든 부분 집합을 subsets에 담기
    new_arr = [i for i in subsets if len(i) == N and sum(i) == K]  # subsets에 담긴 부분집합 중 조건을 만족하는 부분집합만 새로운 리스트에 반환
    print(f'#{tc} {len(new_arr)}')  # 조건을 만족하는 부분집합의 수 출력

# 다른 풀이
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = [i for i in range(1, 12 + 1)]
#     result = 0
#
#     for i in range(1 << 12):
#         sum_sub = 0
#         subset = []
#         for j in range(12):
#             if i & (1 << j):
#                 sum_sub += arr[j]
#                 subset.append(arr[j])
#
#     if len(subset) == N and sum_sub == K:
#         result += 1
#
#     print(f'#{tc} {result}')