# 비트 연산

a = 0x10  # 16진수 -> 2진수 : 00010000(16진수 한자리는 2진수로 나타내면 4자리로 변환됨)
x = 0x01020304
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):  # 1바이트의 이진수를 7번째 비트부터 0번째 비트순으로 탐색
        output += "1" if i & (1 << j) else "0"
    print(output, end=' ')


print("%d = " %a, end ='')
Bbit_print(a)
print()
print("0%X = " %a, end='')
for i in range(0, 4):
        Bbit_print((x >> i*8) & 0xff)  # 오른쪽으로 시프트 -> 마지막 바이트만 처리하고 나머지 바이트는 마스킹(결과적으로 바이트 단위로 수를 역순으로 변환)
p = []
for i in range(0, 4):
    p.append((x >> i*8) & 0xff)
print(p)

# 십진수를 다른 진법의 수로 변환
bit = [0]*8
a = 149  # 변환할 십진수
i = 7
while a > 0:
    bit[i] = a % 2  # 원하는 타진법의 수로 나눈다.
    a //= 2
    i -= 1
# bit[i] = a
print(''.join(map(str, bit)))

# 컴퓨터에서 음의 정수 표현 방법
'''
1의 보수
1. '부호 + 절대값'으로 표현된 값을 부호비트를 제외한 나머지 비트들을 
0은 1로 1은 0으로 변환한다.
2. 최하위 비트에 1을 더한다.
=> 2의 보수로 표기한다. 
'''
#
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

for i in range(-5, 6):
    print("%3d = " % i, end='')
    Bbit_print(i)

# 연습문제
# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력하기
# 입력값 : 01D06079861D79F99F
a = 0x01D06079861D79F99F
