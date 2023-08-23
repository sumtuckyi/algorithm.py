T = int(input())

for tc in range(1, T + 1):

    s = input()
    left = []
    tof = True

    start = 0
    end = len(s) - 1
    while start <= end:
        if s[start] == ')':  # 오른쪽 소괄호인 경우
            if len(left) == 0:  # 스택이 비어있다면
                tof = not tof
                #print('앞부분에 왼쪽 소괄호 없음')
                break  # 검사 중단
            else:  # 스택이 비어있지 않을 때
                if left.pop() == '(':  # 스택 최상단이 왼쪽 소괄호라면
                    start += 1
                    #print('() match')
                    continue
        elif s[start] == '}':  # 오른쪽 대괄호인 경우
            if len(left) == 0:  # 스택이 비어있다면
                tof = not tof
                #print('앞부분에 왼쪽 중괄호 없음')
                break  # 검사 중단
            else:  # 스택이 비어있지 않은 경우
                if left.pop() == '{':  # 정상인 경우
                    start += 1
                    #print('{} match')
                    continue
        elif s[start] == '(' or s[start] == '{':  # 왼쪽 괄호인 경우
            left.append(s[start])
            start += 1
        else:  # 괄호가 아닌 다른 문자인 경우
            start += 1

    if len(left) != 0:  # 검사를 모두 수행하였는데 스택에 괄호가 남아있는 경우
        tof = not tof

    result = 1 if tof else 0
    print(f'#{tc} {result}')

#
T = int(input())

for tc in range(1, T + 1):
    text = input()
    stack = []
    for i in text:
        if i == '(' or i == '{':
            stack.append(i)
        elif stack and i == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == '}' or i == ')':
            stack.append()

    if stack:
        result = 0
    else:
        result = 1

    print(f'#{tc} {result}')