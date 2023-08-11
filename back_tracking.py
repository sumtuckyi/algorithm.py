# 값이 '0'인 좌표 중에 중복 없이 3개만 뽑아 경우의 수 저장하기
coords = [(1, 0), (1, 2), (2, 4), (4, 0), (4, 1), (4, 2), (5, 3), (5, 5), (6, 1), (6, 2), (6, 6)]
map = [[0]*7 for _ in range(7)]
cases = [0]


def back_tracking(depth, lst):
    global cases
    # 종료 조건
    if depth == 3:
        cases.append(lst.copy())  # 결과 리스트에 현재 경우를 추가
        return

    for i in range(len(coords)):
        if coords[i] in lst:  # 중복 걸러내기
            continue
        lst.append(coords[i])
        back_tracking(depth + 1, lst)
        lst.pop()


back_tracking(0, [])
for case in cases:
    print(case)