# 문자열에서 특정 기호를 만나면 특정 연산을 수행하기
word = input()
result = 0
for i in range(len(word)):
    temp = ''
    # 현재 검사할 문자의 다음 인덱스
    index = i + 1
    if word[i] == '[':
        while word[index] != ']':
            # 임시 문자열 temp 변수에 현재 문자 추가
            temp += word[index]
            index += 1
        result += int(temp)
    elif word[i] == '{':
        while word[index] != '}':
            temp += word[index]
            index += 1
        result *= int(temp)

print(result)