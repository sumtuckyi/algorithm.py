# 폭발 문자열
s = input()
bs = input()
left = []

start = 0
end = len(s) - 1

while start <= end:  # start = end인 경우는 전체 문자열의 마지막 요소를 스택 최상단에 넣는 경우
    # 스택에 비교할 문자열 차례로 쌓기
    tof = True
    left.append(s[start])
    start += 1  # 리스트의 다음 요소를 스택에 쌓을 준비
    # 스택 상단의 문자열과 찾고자 하는 문자열을 비교
    if len(left) >= len(bs):  # 스택의 길이가 찾고자 하는 문자열의 길이와 같거나 큰 경우에만 비교
        for i in range(len(bs)):  # 매 비교마다 찾는 문자열의 길이만큼 비교작업 발생
            if bs[i] != left[len(left) - len(bs) + i]:  # 비교했으나 일치하지 않는 경우
                tof = False  # 찾는 문자열의 길이만큼 비교를 하는데 하나라도 일치하지 않으면
                break  # 아무것도 지우지 않고 다시 스택 상단에 문자열을 쌓는 단계로 돌아감
            elif tof:  # 문자열을 찾은 경우
                for i in range(len(bs)):  # 찾는 문자열의 길이 만큼
                    left.pop()  # 스택 최상단의 데이터 삭제

if len(left) == 0:
    print('FRULA')
else:
    print(*left, sep='')