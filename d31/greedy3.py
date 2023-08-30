# 6장을 채우기 전에 먼저 run(연속인 숫자가 3개 이상)이나 triple(같은 숫자가 3개 이상)이 되면 승리한다.
# 12장의 카드가 주어지고, 가져가는 순서는 정해져있다.
# 무승부일 수도 있다.(0을 출력)

# 선수1과 선수2의 카드 리스트를 각각 만든다.
# 일단 각자의 카드를 저장해놓고 3번째 카드를 가져오는 시점부터 승패여부를 검토한다.
# 3장을 받은 경우라면 2번만 비교


# def check1(lst, e):  # e장의 카드를 받은 경우
#     #triple 판별
#     cnt = 1
#     for i in range(e-1):
#         if lst[i] == lst[i+1]: # 연속한 두 수가 같은 경우
#             cnt += 1
#             if cnt == 3:
#                 return True
#         else:
#             cnt = 1
#     return False

def check2(lst, e):  # e장의 카드를 받은 경우
    v = [0] * 10
    cnt = 0
    for i in range(e):  # 카드를 숫자별로 카운트
        v[lst[i]] += 1
    # run 판별 - 1 2 2 3인 경우도 포함
    for i in range(len(v)):  # 카운트 배열에서 3연속 0이 아닌 경우가 존재하는지 확인
        if v[i]:
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 0
    # triple 판별
    for i in range(len(v)):
        if v[i] == 3:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    s1 = []
    s2 = []
    win = 0  # 무승부로 초기화
    for i in range(12):  # 플레이어에게 카드 분배
        if not i % 2:
            s1.append(cards[i])
        else:
            s2.append(cards[i])
    # 베이비진 여부 판별
    for i in range(3, 6+1):  # 3번째부터 6번째 카드를 가져가는 경우
        r1 = check2(s1, i)
        r2 = check2(s2, i)
        if r1:  # 1번이 먼저 달성한 경우
            win = 1
            break
        elif r2:  # 1번은 실패하고 2번은 성공한 경우
            win = 2
            break
    print(f'#{tc} {win}')


#
# def check_win(cards):
#     cnt = [0] * 10
#     for num in cards:
#         cnt[num] += 1
#     if 3 in cnt:
#         return True
#     for i in range(8):
#         if 0 not in cnt[i:i+3]:
#             return True
#     return False
#
# for i in range(6):
#     p1.append(cards[i * 2])
#     if len(p1) > 2 and check_win(p1):
#         winner = 1
#         break
#     p2.append(cards[i * 2 + 1])
#     if len(p2) > 2 and check_win(p2):
#         winner = 2
#         break
# print(f'#{tc} {winner}')
