# 5행
# 5줄을 리스트로 저장
# 열별로 순서대로 읽되, 이미 끝난 문자열을 만난 경우에는 지나감
# 행별 문자열의 길이는 다를 수 있으며 최소 1, 최대 15 -> 가로 최대 길이에 맞춰 15*15배열을 하나 만들어서 단어를 저장
# 리스트 대신 빈문자열을 두고 순차적으로 더해준 다음 해당 문자열을 출력해도 됨
T = int(input())
for tc in range(1, T + 1):
    words = [input() for _ in range(5)]
    temp = []
    result = []
    for w in words:
        temp.append(len(w))
    max_len = max(temp)  # 가장 긴 단어의 길이
    # 가장 긴 단어의 길이에 맞춰주기
    for i in range(5):
        if len(words[i]) < max_len:
            words[i] += '!'*(max_len-len(words[i]))
    for i in range(max_len):  # 5줄씩 단어의 최장길이만큼 세로로 읽기
        for j in range(5):  # 0 0 / 1 0 / 2 0 / 3 0 / 4 0 // 0 1 / 1 1 / 2 1 /
            if words[j][i] != '!':
                result.append(words[j][i])

    print(f'#{tc}',''.join(result))

