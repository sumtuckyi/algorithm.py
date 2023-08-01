# 순열 구현하기
from itertools import permutations

cards = [3, 4, 5, 5]
new_list = list(permutations(cards, 3))
new_set = set(new_list) # 중복 제거

print(list(new_set))