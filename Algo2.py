T = int(input())
# 소괄호 안의 값은 모두 더하고, 중괄호 안의 값은 모두 곱한다.
# 괄호의 짝이 맞지 않는 경우엔 -1을 출력한다. 그 외에는 연산 결과값을 출력한다.
for tc in range(1, T + 1):
    exp = input()
    stack = []
    operators = ['(', ')', '{', '}']

    total = 0  # 연산 결과를 저장

    def cal():  # 입력받은 수식을 규칙대로 연산할 함수
        global total
        temp = 0
        for i in exp:  # 문자열의 길이 만큼 반복
            # 여는 괄호인 경우 스택에 추가
            if i == '(':
                stack.append(i)
            elif i == '{':
                stack.append(i)
            elif i == ')':  # 닫는 소괄호인 경우
                temp = 0
                while stack[-1] != '(':  # 스택의 최상단에 여는 소괄호가 올 때까지
                    if stack[-1] not in operators:  # 스택 최상단에 있는 값이 숫자인 경우
                        temp += int(stack.pop())  # 계산하고 숫자를 스택에서 지운다.
                    elif stack[-1] == '{':  # 괄호가 규칙을 벗어난 경우
                        total = -1  # 잘못된 수식
                        return
                if stack[-1] == '(':  # 반복문 종료 후에 여는 소괄호가 오는 경우
                    stack.pop()  # 연산이 끝난 여는 소괄호를 스택에서 지우고
                    stack.append(temp)  # 연산결과를 스택에 삽입
                    temp = 0
            elif i == '}':  # 닫는 중괄호인 경우
                temp = 1
                while stack[-1] != '{':  # 스택의 최상단에 여는 중괄호가 올 때 까지
                    if stack[-1] not in operators:  # 스택 최상단에 있는 값이 숫자인 경우
                        temp *= int(stack.pop())  # 계산하고 숫자를 스택에서 지운다.
                    elif stack[-1] == '(':  # 괄호가 규칙을 벗어난 경우
                        total = -1  # 잘못된 수식
                        return
                if stack[-1] == '{':  # 반복문 종료 후에 여는 중괄호가 오는 경우
                    stack.pop()  # 연산이 끝난 중괄호를 스택에서 지우고
                    stack.append(temp)  # 연산 결과를 스택에 삽입
                    temp = 1
            else:  # 숫자인 경우 스택에 추가
                stack.append(i)
        # 모든 연산이 끝난 후에
        if len(stack) == 1:  # 수식이 정상적이라면 최종 결과만 스택에 있어야 한다.
            total = stack[0]
        else: # 그렇지 않다면 잘못된 수식
            total = -1

    cal()
    print(f'#{tc} {total}')
