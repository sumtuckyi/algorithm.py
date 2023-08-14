exp = '(6+5*(2-8)/2)'
exp2 = '2+3*4/5'
# exp = '2+3*4/5'

'''
입력 받은 중위 표기식에서 토큰을 읽는다.
토근이 연산자이면 토큰을 출력한다. 
토큰이 연산자(괄호 포함)일 때,
만약 스택이 비어있지 않다면
스택의 최상단 값과 비교하여 그보다 우선순위가 높으면 스택에 삽입하고 
그렇지 않다면(우선순위가 동일한 경우도 포함) 토큰의 우선순위가 높을 때까지
스택에서 pop을 반복한 뒤에 토큰을 스택에 삽입한다. 
최상단에 연산자가 없다면 그냥 바로 삽입한다.
만약 토큰이 오른쪽 괄호이면 스택 최상단에 왼쪽 괄호가 올 때까지
pop연산을 수행하고 pop한 연산자를 출력한다. 왼쪽 괄호를 만나면
pop연산만 하고 출력은 하지 않는다.
중위표기식을 다 읽었다면 중지하고 그렇지 않다면 위의 작업을 반복한다.
스택에 남아있는 연산자를 모두 pop하고 출력한다.
'''


operator = ['(', '*', '/', '+', '-']
# value의 숫자가 클수록 우선순위가 높음
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}  # 스택 안에 있는 경우의 우선순위

def to_postfix(exp):
    stack = [0] * 100
    top = -1
    susik = ''
    for i in range(len(exp)):
        if exp[i] in operator:  # 토큰이 연산자라면
            if not stack:  # 스택이 비어있거나 스택 연산자의 우선순위가 현재 연산자의 우선순위보다 낮다면
                # 해당 연산자를 스택에 삽입
                top += 1
                stack[top] = exp[i]
            elif stack and isp[stack[top]] < icp[exp[i]]:
                top += 1
                stack[top] = exp[i]
            else:  # 스택 연산자의 우선순위가 토큰의 우선순위보다 낮지 않은 경우(크거나 동일)
                while top > -1 and isp[stack[top]] >= icp[exp[i]]: # 스택이 비어있지 않고 스택 연산자의 우선순위가 높은 한
                    # 스택 최상단의 연산자를 출력
                    susik += stack[top]
                    top -= 1
                top += 1
                stack[top] = exp[i]
        elif exp[i] == ')':  # 토큰이 오른쪽 괄호라면
            while stack[top] != '(':  # 스택 최상단의 값이 '('이 될 때까지
                # 스택 최상단의 값을 출력
                susik += stack[top]
                top -= 1
            top -= 1 # 왼쪽 괄호를 스택에서 제거
        else:  # 토큰이 피연산자라면
            susik += exp[i]
    print(susik)

def read_exp(exp):  # 수식문자열을 읽어서 피연산자는 바로 출력하고 연산자는 우선순위가 높은 순으로 피연산자 이후에 출력
    stack = []
    for i in range(len(exp)):
        if exp[i] not in operator:
            print(exp[i], end=' ')
        else:
            stack.append(exp[i])
    while stack:
        print(stack.pop(), end=' ')


# append, pop대신 top변수를 이용해서 스택 구현해보기
'''
pop()은 
stack[top] = a
top -= 1 
로 구현
append()는
top += 1
stack[top] = b 
로 구현
'''
def cal(exp):  # 후위표기식을 입력받아 계산한 뒤 답을 출력
    stack = []
    for i in range(len(exp)):
        if exp[i] not in operator:  # 토큰이 피연산자인 경우
            stack.append(int(exp[i]))
        else:  # 토큰이 연산자인 경우
            a, b = stack[-2], stack[-1]
            if exp[i] == '+':
                temp = a + b
            elif exp[i] == '-':
                temp = a - b
            elif exp[i] == '/':
                temp = a / b
            else:
                temp = a * b
            # temp = stack[-2] + exp[i] + stack[-1]
            for _ in range(2):
                stack.pop()
            # eval()을 사용하지 못 하는 경우
            stack.append(temp)
            # stack.append(str(eval(temp)))
            # print(stack)
    print(stack.pop())


to_postfix(exp)  # 중위표기식을 후위표기식으로 변환

print()
read_exp(exp2)  # 괄호 없는 중위표기식을 후위표기식으로 변환
print()
cal('6528-*2/+')  # 후위표기식을 계산한 결과
cal('2345/*+')