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
