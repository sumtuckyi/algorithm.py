# 이진탐색
T = int(input())


def binary_search(pages, p):  # 찾고자 하는 페이지와 탐색 범위를 인자로 입력받아 총 몇 번의 탐색이 이루어지는지 반환하는 함수
    start = 1
    end = pages
    cnt = 0

    mid = 0  # p자리의 인자가 될 수 없는 값으로 초기화
    while p != mid:
        mid = int((start + end) / 2)
        # cnt += 1
        if p > mid:  # p가 mid보다 큰 경우에도 그냥 다음탐색의 범위에 mid를 포함시킴
            start = mid
        else:
            end = mid
        cnt += 1
    return cnt


for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    # array = [i for i in range(1, P + 1)]

    a = binary_search(P, A)
    b = binary_search(P, B)

    if a < b:
        result = 'A'
    elif a > b:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')