# 문자열을 입력받아 경우의 수 출력하기
time = input().split('.')

# 어차피 하나의 함수 내에서 cnt값이 바뀌는 경우가 없으므로 *=을 하지 않아도 상관없음
def year(str):
    cnt_y = 1
    if str == 'XXXX':
        return 1
    else:  # X가 0~3개인 경우
        for i in range(len(str)):
            if i == 0 and str[i] == 'X':  # 연도의 첫번째 자리가 X일 때
                cnt_y *= 9
            elif str[i] == 'X':
                cnt_y *= 10
    return cnt_y


def month(str):
    cnt_m = 1
    if len(str) == 1 and str == 'X':  # 월이 한 자리이면서 X일 때
        cnt_m *= 9
    elif len(str) == 2 and 'X' in str:  # 월이 두 자리이면서 X를 포함할 때
        cnt_m *= 3
    return cnt_m


def day(str):
    cnt_d = 1
    if len(str) == 1 and str == 'X':  # 일이 한자리이면서 X인 경우
        cnt_d *= 9
    elif len(str) == 2 and 'X' in str:  # 두자리 수이면서 X가 포함된 경우
        if str == 'XX':  # XX
            cnt_d *= 31
        elif str[0] != 'X':  # 두자리수이면서 뒷자리에 X가 오는 경우
            if str[0] == 3:
                cnt_d *= 2
            else:
                cnt_d *= 10
        else:  # 두자리수이면서 앞자리에 X가 오는 경우
            if str[1] == 1:
                cnt_d *= 3
            else:
                cnt_d *= 2
    return cnt_d


result = year(time[0]) * month(time[1]) * day(time[2])
print(result)

#
