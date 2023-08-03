# array = [1, 2, 3, 4, 5]
#
# def search(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return 1
#
#
# print(search(array, 4))


# binary search
# def binary_search(a, n, key):
#     start = 0
#     end = n - 1
#
#     while start <= end: # 탐색구간이 한 칸이라도 존재한다면(=가 성립하는 경우)
#         mid = (start + end) // 2
#         if a[mid] == key:
#             return True
#         elif a[mid] < key:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return False

def binary_search(a, n, key):
    start = 0
    end = n - 1

    while start <= end:
        mid = start + end // 2
        if key == a[mid]:
            return mid
        elif key > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False

array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(binary_search(array, 5, 20))
