T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    # 챌린지 회차가 증가할수록 함께 증가하는 튕기는 거리, N의 범위에 맞게 설정
    steps = [i for i in range(1, 20 + 1)]

    i = 0  # 챌린지 회차
    idx = 0  # 각 챌린지 별 공이 튕기는 순서
    total = 0  # N번의 챌린지에서 얻을 수 있는 총 점수
    while i < len(scores):  # 챌린지는 총 N번
        step = steps[i]  # 챌린지가 거듭 될 때마다 공이 튕기는 거리가 증가함
        if idx * step <= len(scores) - 1:  # 탁자의 범위 내에 있는 경우에만 탁자에 적힌 숫자를 더해주기
            total += scores[idx * step]
            idx += 1
        else:  # 탁자의 범위를 벗어난 경우 다음 챌린지 회자로 넘어감
            i += 1
            idx = 0

    if total < 0:  # 획득점수가 0점 이하인 경우에는 0을 출력
        total = 0
    print(f'#{tc} {total}')


# range( , , step)의 step을 이용하면 간단한 문제
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    result = 0

    for i in range(N):  # 총 N회의 챌린지 횟수
        for j in range(0, N, i + 1):  # STEP인 i+1은 챌린지 회차마다 1씩 증가
            result += scores[j]

    result = result if result >= 0 else 0
    print(f'#{tc} {result}')