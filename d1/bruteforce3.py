# 최대 상금 - 완전 탐색
T = int(input())
for tc in range(1, T + 1):
    num, c = input().split()
    c = int(c)  # 교환횟수
    now = set([num]) # 가능한 숫자판 순서
    next = set() # 다음 턴
    for _ in range(c):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(len(num) - 1):
                for j in range(i+1, len(num)):
                    s[i], s[j] = s[j], s[i]
                    next.add(''.join(s))
                    s[i], s[j] = s[j], s[i]  # 원상복구
        now, next = next, now
    result = max(map(int, now))
    print(f'#{tc} {result}')


