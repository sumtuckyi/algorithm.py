# 부분집합의 합이 10이 되는 경우 출력하기
def subset(index, total):
    global cnt
    if total > S:
        return
    if index == len(my_set):
        if total == S:
            cnt += 1
            # cases.append(arr.copy())
        return
    total += my_set[index]
    # arr.append(my_set[index])
    subset(index + 1, total)
    # total -= my_set[index]
    # arr.pop()
    subset(index+1, total-my_set[index])


T = int(input())
for tc in range(1, T + 1):
    N, S = map(int, input().split())  # N은 집합의 크기, S는 부분집합의 합
    my_set = list(map(int, input().split()))
    cnt = 0
    # cases = []
    subset(0, 0)
    print(f'#{tc} {cnt}')