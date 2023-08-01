# 숫자 카드(카운팅 정렬)
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = int(input())
    counts = [0] * 10 # 데이터 내의 정수 중 최댓값이 9

    for i in range(N):
        counts[cards % 10] += 1
        cards //= 10
    max_cnt = counts[0]
    max_index = 0

    for index, cnt in enumerate(counts):
        if cnt == max_cnt: # 카운팅 값이 같은 경우에는 인덱스를 비교
            if index > max_index:
                max_index = index
        elif cnt > max_cnt:
            max_cnt = cnt
            max_index = index

    print(f'#{tc} {max_index} {max_cnt}')