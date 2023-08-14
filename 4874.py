T = int(input())

operators = ['+', '-', '*', '/', '.']

def forth(exp):
    stack = []
    temp = 0
    for i in range(len(exp)):
        if exp[i] not in operators:  # 토큰이 피연산자인 경우
            stack.append(exp[i])
        else:  # 토큰이 연산자인 경우
            if len(stack) <= 1:  # 스택이 비어있거나 피연산자가 하나 뿐인 경우
                return 'error'
            else:  # 스택의 길이가 2 이상인 경우
                if exp[i] == '+':
                    temp = stack[-2] + stack[-1]
                elif exp[i] == '-':
                    temp = stack[-2] - stack[-1]
                elif exp[i] == '*':
                    temp = stack[-2] * stack[-1]
                else:
                    temp = stack[-2] / stack[-1]
                for _ in range(2):
                    stack.pop()
                stack.append(temp)
    else:
        if len(stack) == 1:
                ans = stack.pop()
                return int(float(ans))
        else:  # 연산자의 수가 모자란 경우
            return 'error'
for tc in range(1, T + 1):

    expression = list(map(lambda x: int(x) if x not in operators else x, input().split()))
    result = forth(expression)
    print(f'#{tc} {result}')