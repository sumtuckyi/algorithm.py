# 문자열에서 알파벳과 숫자 구분하여 추출하기 - import re 사용하기

import re
sent = 'AB110CDEF11G4H5'
name_list = re.findall("[a-zA-Z]+", sent)
num_list = re.findall(r'\d+', sent)

result = []
for i, j in zip(name_list, num_list):
    ans = i + '#' + str(int(j) + 17)
    result.append(ans)
print(*result, sep='\n')



# 인덱스 에러 해결
# sent = input()
# names = []
# numbers = []
# for i in range(len(sent)):
#     temp = ''
#     index = i + 1
#     if sent[i].isalpha():
#         while not sent[index].isdecimal():
#             temp += sent[i]
#             index += 1
#         names.append(temp)
#     elif sent[i].isdecimal():
#         while not sent[index].isalpha():
#             temp += sent[i]
#             index += 1
#         numbers.append(temp)
#
# print(names, numbers)

# stack 이용
sent = 'AB110CDEF11G4H5'
left = []
names = []
numbers = []

start = 0
end = len(sent) - 1
while start <= end:
    left.append(sent[start])
    start += 1
    if sent[start - 1].isalpha():  # 스택 최상단 문자열이 대문자일 때
        if sent[start].isdecimal():  # 스택에 쌓일 데이터가 숫자라면
            for i in range(len(left)): # 스택에 있는 데이터를 옮기고 삭제
                temp = []
                temp.append(left[i])
                names.append(temp)
                left.clear()
    elif sent[start - 1].isdecimal():  # 스택 최상단 문자열이 숫자일 때
        if sent[start].isalpha():  # 스택에 쌓일 데이터가 대문자라면
            for i in range(len(left)):  # 스택에 있는 데이터를 옮기고 삭제
                temp = []
                temp.append(left[i])
                numbers.append(temp)
                left.clear()
    if start == end:
        numbers.append(left)

print(names, numbers)

