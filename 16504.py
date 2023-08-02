T = int(input())

for tc in range(1, T + 1):
    W = int(input())
    arr = list(map(int, input().split()))
    w = W - 1  # 낙차

    if W == 1:  # 가로가 1이라 낙차가 발생할 수 없는 경우
        max_v = 0
    else:
        max_v = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):  # 리스트의 오른쪽으로 가면서 크거나 같은 높이를 만나면 낙차가 1씩 감소
                if arr[i] <= arr[j]:
                    w -= 1
            if max_v < w:
                max_v = w

    print(f'#{tc} {max_v}')