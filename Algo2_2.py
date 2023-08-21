T = int(input())


def setting():  # 입력받은 카드를 규칙에 따라 덱에 넣는 함수
    bonus = 0  # 보너스 카드의 값 초기화
    for card in cards_a:  # a 덱에서 카드를 한 장씩 가져온다.
        if card == '+':  # 더하기 카드인 경우
            bonus += 1
        else:  # 숫자인 경우
            if not (card + bonus) % 2:  # 카드가 짝수인 경우
                stack_c.append((card + bonus))
            elif (card + bonus) % 2:  # 카드가 홀수인 경우
                queue_b.append((card + bonus))


def score():  # M번째 순서인 사람의 점수를 구하는 함수
    score_b = 0
    score_c = 0
    for _ in range(M-1):  # M번째 바로 전까지만 카드를 가져감
        if queue_b:  # 큐가 비어있지 않다면
            queue_b.pop(0)  # 전단의 숫자카드를 한 장 가져감
        if stack_c:  # 스택이 비어있지 않다면
            stack_c.pop()  # 최상단의 숫자카드를 한 장 가져감
    # 김싸피의 순서
    if queue_b:
        score_b = queue_b.pop(0)
    if stack_c:
        score_c = stack_c.pop()
    return score_b + score_c  # 만약 두 개의 덱이 모두 비어있다면 0을 리턴함


for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 카드의 수와 김싸피의 순서
    cards_a = list(map(lambda c: int(c) if c.isdigit() else c, input().split()))  # a 카드덱
    queue_b = []  # b 카드덱
    stack_c = []  # c 카드덱
    setting()  # 입력받은 카드를 규칙에 따라 덱에 옮기기
    print(f'#{tc} {score()}')
