# stack - 선형구조, 후입선출
# 문자열 parsing에서 사용하면 문자열 비교와 삭제 과정에서의 시간복잡도를 줄일 수 있다.

# stack 구현
stack = [0] * 10
top = -1

top += 1            #push(1)
stack[top] = 1
top += 1            #push(2)
stack[top] = 2
top += 1            #push(3)
stack[top] = 3

print(stack[top])   #pop()
top -= 1
print(stack[top])   #pop()
top -= 1
print(stack[top])   #pop()
top -= 1

# 괄호 검사 함수
# s = input()
# left = []
# tof = True
#
# start = 0
# end = len(s) - 1
# while start <= end:
#     if s[start] == ')':
#         if len(left) == 0:
#             tof = not tof
#             break
#         else:
#             if left.pop() == '(':
#                 start += 1
#                 continue
#     else:
#         left.append(s[start])
#         start += 1
# if len(left) != 0:
#     tof = not tof
#
# print(tof)

# 리스트를 스택으로 사용하는 것 외에도 함수의 호출 및 복귀를 관장하기 위해 스택 자료구조를 사용함 - 함수 호출 시마다 메모리 영역을 할당받아 동일한 함수라도 호출될 때 마다 각기 다른 메모리 영역을 사용하게 됨
# Memoization - 중복호출로 인한 비효율성을 개선하기 위해 최초 호출 시 별도로 반환값을 저장해놓고 이후 반복해서 호출될 때마다 그 값을 참조하여 사용(재귀호출 횟수를 줄일 수 있음)
# recursion
