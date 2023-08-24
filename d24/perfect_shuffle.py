# N개의 카드를 받아 2개의 덱으로 나눈다.(홀수면 첫번째 덱이 하나 더 많음)
# 첫번째 덱의 카드를 먼저 놓는다. 그 다음부터는 교대로 쌓는다.

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(input().split())
    shuffled = []
    if N % 2:  # 카드 수가 홀수인 경우
        g1 = cards[:(N//2)+1]
        g2 = cards[(N//2)+1:]
    else:  # 카드 수가 짝수인 경우
        g1 = cards[:(N//2)]
        g2 = cards[(N//2):]
    for i in range(N):
        if not i % 2:  # 짝수번째 순서이면
            shuffled.append(g1[i//2])
        else:  # 홀수번째 순서이면
            shuffled.append(g2[i//2])
    print(f'#{tc}', *shuffled)