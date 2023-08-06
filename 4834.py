# 숫자 카드(카운팅 정렬)
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = int(input())  # ex) 12345899
    counts = [0] * 10 # 데이터 내의 정수 중 최댓값이 9

    for i in range(N):
        counts[cards % 10] += 1  # 1의 자리부터 순차적으로 배열의 해당하는 인덱스 값을 카운트
        cards //= 10  # 입력받은 값에서 일의자리를 순차적으로 제외한 값을 재할당
    max_cnt = counts[0]
    max_index = 0

    for index, cnt in enumerate(counts):  # (index, value)순서
        if cnt == max_cnt:  # 카운팅 값이 같은 경우에는 인덱스를 비교
            if index > max_index:
                max_index = index
        elif cnt > max_cnt:
            max_cnt = cnt
            max_index = index

    print(f'#{tc} {max_index} {max_cnt}')