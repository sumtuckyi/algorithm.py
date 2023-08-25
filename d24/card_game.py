# 동일한 카드를 가지고 있으면 오류 출력, 카드 종류 별로 몇 장이 더 필요한 지 구하라
# 카드 식별자는 늘 3자리 -> 문자열의 길이는 최대 3000
# 0-2/3-5/6-8..으로 입력값을 앞에서부터 순차적으로 길이 3만큼 잘라서 검토 / 인덱스를 0, 3, 6으로, 인덱스의 범위는 문자열의 길이가 결정
# 12이면 3*i일 때 i는 0부터 3까지 12//4
# 3자리씩 검토하다가 중복카드가 등장하면 바로 return

# 중복카드 여부를 확인할 때 set()를 만들어서 입력받은 카드 수와 세트의 길이를 비교하여 중복여부를 거를 수 있음
def check(data):  # 중복카드가 있는지 확인
    for i in range(n // 3):  # 카드의 수만큼 확인
        if data[i*3:i*3+3] in dup:
            return 0
        else:
            dup.append(data[i*3:i*3+3])
    return 1


T = int(input())
for tc in range(1, T + 1):
    cards = input()
    n = len(cards)
    dup = []
    # 초기화시 d = {'S': 13, 'D': 13, 'H': 13, 'C': 13}으로 하면 카드 체크시마다 빼주면 됨
    d = {'S': 0, 'D': 0, 'H': 0, 'C': 0}
    if check(cards):  # 중복 카드가 없으면
        for card in dup:
            d[card[0]] += 1
        print(f'#{tc}', 13 - d['S'], 13 - d['D'], 13 - d['H'], 13 - d['C'])
    else:
        print(f'#{tc} ERROR')