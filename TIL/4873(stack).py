# 중복 문자열 제거
T = int(input())

for tc in range(1, T + 1):
    sent = input()
    stack = []
    idx = 1  # 현재값
    stack.append(sent[0]) # 문자열의 첫번째 요소를 스택에 넣고 시작
    while idx < len(sent): # 문자열의 길이 만큼 반복문 수행
        # if stack and stack[-1] == sent[idx]:  # 스택이 비어있지 않고 최상단 값과 현재값이 동일한 경우
        #     stack.pop()  # 스택 최상단 값을 삭제
        # elif stack and stack[-1] != sent[idx]: # 스택이 비어있지 않고 최상단 값과 현재값이 일치하지 않는 경우
        #     stack.append(sent[idx])
        if stack:  # 스택이 비어있지 않은 경우
            if stack[-1] == sent[idx]:  # 최상단값과 현재값이 동일한 경우
                stack.pop()
            else:  # 동일하지 않은 경우
                stack.append(sent[idx])
        else:  # 스택이 비어있는 경우
            stack.append(sent[idx])
        idx += 1
    print(f'#{tc} {len(stack)}')


# 다른 풀이
T = int(input())

for tc in range(1, T + 1):
    sent = input()
    stack = []
    for char in sent:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    print(f'#{tc} {len(stack)}')
