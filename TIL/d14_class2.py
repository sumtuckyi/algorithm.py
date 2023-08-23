# 집합 s의 부분집합 모두 구하기
def back_tracking(index, lst):
    global subsets
    if index == len(s):
        subsets.append(lst.copy())
        return

    back_tracking(index + 1, lst)

    lst.append(s[index])
    back_tracking(index + 1, lst)
    lst.pop()


s = [1, 2, 3, 4]
subsets = []
back_tracking(0, [])
# print(subsets)
for subset in subsets:
    print(subset)


# 부분집합 중 원소의 합이 n인 부분집합 구하기
def subset(index, total, arr):
    global cnt
    if total > 10:
        return
    if index == len(my_set):
        if total == 10:
            cnt += 1
            cases.append(arr.copy())
        return
    total += my_set[index]
    arr.append(my_set[index])
    subset(index + 1, total, arr)
    total -= my_set[index]
    arr.pop()
    subset(index+1, total, arr)


my_set = [i for i in range(1, 10+1)]
cnt = 0
cases = []
subset(0, 0, [])
print('조건을 만족하는 부분집합의 개수:', cnt,'조건을 만족하는 부분집합:', *cases, sep='\n')