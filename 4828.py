T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    max_value = arr[0]
    min_value = arr[0]
    for i in range(1, N):
        if max_value < arr[i]:
            max_value = arr[i]
        if min_value > arr[i]:
            min_value = arr[i]
    ans = max_value - min_value
    print(f'#{tc} {ans}')
