# 부분집합의 합이 10이 되는 경우 출력하기
def subset(index, total, rs):
    global cnt, call
    call += 1
    # 가지치기
    if total > S:
        return
    # 가지치기2 : 현재 깊이까지의 부분집합의 합과 이를 제외한 나머지를 다 더해도 목표값에 미치지 못 하는 경우
    if rs + total < S:
        return
    if index == len(my_set):
        if total == S:
            cnt += 1
        return
    else:
        total += my_set[index]
        # arr.append(my_set[index])
        subset(index + 1, total, rs-my_set[index])
        # total -= my_set[index]
        # arr.pop()
        subset(index+1, total-my_set[index], rs+my_set[index])


T = int(input())
for tc in range(1, T + 1):
    N, S = map(int, input().split())  # N은 집합의 크기, S는 부분집합의 합
    my_set = list(map(int, input().split()))
    cnt = 0
    call = 0  # 함수의 호출횟수

    subset(0, 0, sum(my_set))
    print(f'#{tc} {cnt} {call}')
