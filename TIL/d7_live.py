'''

'''


def strlen(arr):
    i = 0
    cnt = 0
    while True:
        if arr[i] != '₩0':
            cnt += 1
            i += 1
        else:
            break
    return cnt


a = ['a', 'b', 'c', '₩0']
print(strlen(a))

# 문자열 뒤집기 1
s = 'reverse this strings'
s = s[::-1]
print(s)

def string_reversal(s):
    new_str = ''
    for i in range(len(s) - 1, -1, -1):
        new_str += s[i]
    return new_str


print(string_reversal('Reverse'))


# 문자열 뒤집기 2 : 문자열은 immutable하므로 리스트로 변환해서 swap한다.


def string_reversal2(s):
    new_list = list(s)
    for i in range(len(s) // 2):
        new_list[i], new_list[len(s)-1-i] = new_list[len(s)-1-i], new_list[i]
    return ''.join(new_list)


print(string_reversal2('algorithm'))


# 문자열 비교
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1  # s1[:]의 경우도 마찬가지
s5 = s1[:2] + 'c'
s6 = 'abd'
s7 = 'ABC'
s8 = 'ab'

# print(s1 == s2)
# print(s1 is s2)
# print(s1 == s4)
# print(s1 is s4)
# print(s1 == s5)
# print(s1 is s5)
# print(f's1:{id(s1)}, s2:{id(s2)}, s3:{id(s3)}, s4:{id(s4)}, s5:{id(s5)}')
print(s1 < s6)
print(s1 > s7)
print(s1 < s8)
print(ord('s'), ord('a'), ord('A'), ord(' '))
# 문자-정수 간 변환
# int() 구현하기
# ord('0')은 48

def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')  # i*10을 더해주는 것은 숫자를 뒤로 늘려나가기 때문
    return i


# str() 구현하기


def itoa(x):
    print(type(x))
    s = ''
    while x > 0:
        s += chr(ord('0') + x % 10)  # 1의 자리 숫자의 ascii code값
        x //= 10
    return s[::-1]


print(type(itoa(123)))