# 리스트 내의 요소를 왼쪽, 오른쪽 이동시키기
arr = [3, 5, 1, 9, 7]

directions = [input() for i in range(4)]
stack = []

for i in directions:
    if i == 'R':  # 오른쪽으로 미는 경우
        stack.append(arr.pop())
        arr = stack + arr
    else:  # 왼쪽으로 미는 경우
        stack.append(arr.pop(0))
        arr = arr + stack
    stack.clear()

print(*arr)

#
arr = [3, 5, 1, 9, 7]
T = [input() for _ in range(4)]


def Right(lst):
    # 리스트 뒤쪽에 맨 앞 4개의 요소 추가
    for i in range(4):
        lst.append(lst[i])
    # 맨 앞의 요소 4개 삭제
    for _ in range(4):
        lst.pop(0)


def Left(lst):
    # 리스트 맨 뒤에 맨 앞 한 개의 요소 추가
    lst.append(lst[0])
    lst.pop(0)  # 맨 앞의 요소 하나 삭제

for i in range(4):
    if T[i] == "R":
        Right(arr)
    else:
        Left(arr)
print(*arr)
