T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    boxes = [0] * (N + 1)

    for j in range(1, Q + 1):
        L, R = map(int, input().split())
        for i in range(L, R + 1):
            boxes[i] = j

    print(f'#{tc}', *boxes[1:])

