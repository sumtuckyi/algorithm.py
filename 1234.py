# 리스트에서 중복 문자열을 순차적으로 지우기


'''
for i in range(문자열의 길이):
    if 스택이 비어있거나 최상단 값과 다른 경우:
        현재값 쌓기
    else: 스택이 비어있지 않지만 최상단 값과 현재값이 같은 경우
        pop()
'''


for tc in range(1, 10+1):
    str_N, str_S = input().split()
    N = int(str_N)
    stack = [0] * N
    top = -1

    for i in str_S:
        if top == -1 or stack[top] != i:
            top += 1
            stack[top] = i
        else:
            top -= 1  # 스택 최상단 인덱스를 표시
    print(f'#{tc}', ''.join(stack[:top+1]))