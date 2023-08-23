arr1 = [1, 2, 3, 4]
bit1 = [0, 0, 0, 0]


# def print_subset(bit, arr, n): # 이진수를 부분집합으로 변환
#     total = 0
#     for i in range(n):
#         if bit[i]:
#             print(arr[i])
#             # total += arr[i]
#     # print(total, bit)


# for i in range(2): # 원소의 개수가 4개인 경우 부분집합의 경우의 수
#     bit1[0] = i
#     for j in range(2):
#         bit1[1] = j
#         for k in range(2):
#             bit1[2] = k
#             for l in range(2):
#                 bit1[3] = l
#                 print(bit1)
#                 print_subset(bit1, arr1, len(arr1))

arrays =[]
for i in range(1 << len(arr1)):  # 0 ~ (2 ^ n - 1)
    arr = []
    for j in range(len(arr1)):
        if i & (1 << j):
            arr.append(arr1[j])
    arrays.append(arr)
    # print(bin(i), arr)

# print(arrays)
result = [i for i in arrays if sum(i) == 3]
print(result)