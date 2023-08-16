from copy import deepcopy


def back(i, total):
    global min_v, path, result
    if i == m:  # 다 뽑은 경우
        if total < min_v:  # 더 작으면 최솟값을 갱신
            min_v = total
            result = deepcopy(path)
        return
    for j in range(n):  # N개의 패에 대해서
        if check[j] == 1:  # 이미 사용한 패인 경우
            continue
        path.append(cards[j])
        check[j] = 1
        back(i+1, total * cards[j])
        check[j] = 0
        path.pop()


n, m = map(int, input().split())
cards = list(map(int, input().split()))
check = [0]*n  # 패가 사용되었는지 체크
path = []  # 선택된 패들의 값을 저장할 리스트
min_v = float('inf')  # 예를 들어 21e8
result = []
back(0, 1)
result.sort()
print(*result)