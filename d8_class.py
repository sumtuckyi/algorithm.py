# eval() 구현하기
s = input().split('+')  # 100+100-50+30

result = 0
for i in s:
    if i.isdecimal():  # '+'기준으로 나눈 결과에 기호가 포함되지 않는 경우(즉, 덧셈인 경우)
        result += int(i)
    if not i.isdecimal():  # '+'기준으로 나눈 결과에 기호가 포함되는 경우(맨 앞에 오는 수가 음수이거나 -연산자로 연결된 피연산자들)
        sub = i.split('-')
        if sub[0] != '':
            result += int(sub[0])
            for i in range(1, len(sub)):
                result -= int(sub[i])
        else:
            result -= int(sub[1])
print(result)

# # eval()내장함수 사용
# print(eval(input()))
# # 다른 풀이
# ex = input()
# if ex[0] == '-':  # 표현식 맨 앞의 수가 음수인 경우 전처리
#     ex = '0' + ex
#
# word = ex.split('+')
# ans = 0
# for w in word:
#     w = w.split('-')
#     inner_ans = int(w[0])
#     for i in range(1, len(w)):
#         inner_ans -= int(w[i])
#     ans += inner_ans
# print(ans)