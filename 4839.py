T = int(input())


def binary_search(pages, p):
    start = 1
    end = pages
    cnt = 0
    mid = 0
    while p != mid:
        mid = int((start + end) / 2)
        # cnt += 1
        if p > mid:
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