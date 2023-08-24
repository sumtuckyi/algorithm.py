# 동일한 카드를 가지고 있으면 오류 출력, 카드 종류 별로 몇 장이 더 필요한 지 구하라
# 카드 식별자는 늘 3자리 -> 문자열의 길이는 최대 3000
# 0-2/3-5/6-8..으로 입력값을 앞에서부터 순차적으로 길이 3만큼 잘라서 검토 / 인덱스를 0, 3, 6으로, 인덱스의 범위는 문자열의 길이가 결정
# 12이면 3*i일 때 i는 0부터 3까지 12//4
# 3자리씩 검토하다가 중복카드가 등장하면 바로 return


def check(data):  # 중복 확인 함수
    n = len(data)//3
    c_dup = set()  # 중복확인용
    for i in range(n):
        if data[i*3:i*3+3] in c_dup:  # 이미 가진 카드인 경우
            return 0
        else:
            c_dup.add(data[i*3:i*3+3])
    return 1


T = int(input())
for tc in range(1, T + 1):
    cards = input()
    print(check(cards))
