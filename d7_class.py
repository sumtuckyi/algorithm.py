# IM형 기출
# str.find(), list.index()

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    cnt = 0
    for i in passcode:
        for j in range(len(sample)):
            if sample[j] == i:
                cnt += 1
                sample = sample[j + 1:]
                break

    result = 1 if cnt == K else 0
    print(f'#{tc} {result}')

# 다른 풀이 1
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    cnt = 0
    result = 0  # 반복문 수행 결과 패스코드를 모두 찾지 못하면 반환될 값

    for i in range(N):
        if passcode[cnt] == sample[i]:
            cnt += 1
        if cnt == K:
            result = 1
            break

    print(f'#{tc} {result}')

# 다른 풀이 2 - index()와 try, except문 사용
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    indexes = []
    result = 1

    for i in range(len(passcode)):
        now = passcode[i]
        try:
            index = sample.index(now)
            sample = sample[index + 1:]
        except:
            result = 0

    print(f'#{tc} {result}')

# 다른 풀이 3 - 문자열로 변환하여 find() 사용