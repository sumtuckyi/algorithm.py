# 연속한 1의 개수
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    arr2 = [0]
    cnt = 1
    for i in range(1, N):

        if arr[i] == arr[i - 1] == 1:
            cnt += 1
            if cnt > arr2[0]:
                arr2.clear()
                arr2.append(cnt)
        else:
            cnt = 1
    if 1 in arr and arr2[0] == 0:
        arr2[0] = 1

    print(f'#{tc} {arr2[0]}')