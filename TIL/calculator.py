def check(form):  # 수식 중에 괄호에 해당하는 경우만 짝이 올바르게 쓰였는지 체크
    stack = []
    for tk in form:
        if tk in ['{', '(']:
            stack.append(tk)
        elif tk == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif tk == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0

    return 0 if stack else 1


# 괄호 문제가 있는 경우는 미리 걸러내므로 더이상 고려할 필요가 없음
def op(form):
    stack = []
    for tk in form:
        if tk == ')':
            temp = 0
            while stack and stack[-1] != '(':
                temp += int(stack.pop())
            stack.pop()
            stack.append(temp)
        elif tk == '}':
            temp = 1
            while stack and stack[-1] != '{':
                temp *= int(stack.pop())
            stack.pop()
            stack.append(temp)
        else:  # 숫자나 여는 괄호이면 스택에 추가
            stack.append(tk)
    return -1 if len(stack) != 1 else stack[0]


T = int(input())
for tc in range(1, T + 1):
    form = input()
    ans = -1
    if check(form):  # 괄호 규칙이 잘못된 경우에는 아예 연산을 할 필요가 없음(이 경우 -1이 출력됨)
        ans = op(form)
    print(f'#{tc} {ans}')