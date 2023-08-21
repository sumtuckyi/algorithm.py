def captcha():
    global sample
    cnt = 0
    for i in passcode:
        for j in range(len(sample)):
            if i == sample[j]:
                cnt += 1
                sample = sample[j+1:]
                break
    if cnt == K:
        return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    print(f'#{tc} {captcha()}')
