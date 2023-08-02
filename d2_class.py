# 2차원 리스트 IM대비
# 16504문 - gravity
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

# 다른 풀이
T = int(input())

for tc in range(1, T + 1):
    W = int(input())
    arr = list(map(int, input().split()))
    max_v = 0

    for i in range(W):
        cnt = 0
        for j in range(i + 1, W):
            if arr[i] > arr[j]:
                cnt += 1
        if max_v < cnt:
            max_v = cnt

    print(f'#{tc} {cnt}')

# 4836문
# 다른 풀이
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    result = 0
    for i in range(N):
        red1, blue1, red2, blue2, color = map(int, input().split())

        for j in range(red1, red2 + 1):
            for k in range(blue1, blue2 + 1):
                arr[j][k] += color
                if arr[j][k] == 3:
                    result += 1

print(f'#{tc} {result}')

