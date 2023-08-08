# 문자열에서 알파벳과 숫자 구분하여 추출하기 - import re 사용하기

# import re
# sent = input()
# name_list = re.findall("[a-zA-Z]+", sent)
# num_list = re.findall(r'\d+', sent)
#
# result = []
# for i, j in zip(name_list, num_list):
#     ans = i + '#' + str(int(j) + 17)
#     result.append(ans)
# print(*result, sep='\n')



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






