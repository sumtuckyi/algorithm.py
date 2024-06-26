# 스택을 이용하여 특정한 규칙이 있는 연산 수행하기
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
    else:  # 반복문 중간에 return되지 않았다면 실행되는 코드
        if len(stack) == 1:
                ans = stack.pop()
                return int(float(ans))
        else:  # 연산자의 수가 모자란 경우
            return 'error'
for tc in range(1, T + 1):

    expression = list(map(lambda x: int(x) if x not in operators else x, input().split()))
    result = forth(expression)
    print(f'#{tc} {result}')


# try, except로 형식이 잘못된 경우를 처리하기
T = int(input())
for tc in range(1, T + 1):
    forth = list(input().split())
    stack = []
    error = False
    for i in range(len(forth)-1):  # '.'은 탐색 안 함
        if forth[i].isdigit():  # 토큰이 숫자일 경우
            stack.append(forth[i])
        else:  # 토큰이 연산자인 경우
            try:
                b = int(stack.pop())
                a = int(stack.pop())
                if forth[i] == '+':
                    ans = a + b
                elif forth[i] == '-':
                    ans = a - b
                elif forth[i] == '*':
                    ans = a * b
                else:
                    ans = a // b
                stack.append(ans)
            except:  # 스택에서 연속적으로 2개의 숫자를 꺼낼 수 없는 경우
                error = True
    if error or len(stack) != 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {stack.pop()}')
