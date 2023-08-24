# N개의 수가 주어지고 그 중 2개의 수를 곱했을 때, 단조증가를 만족하는 수 중 가장 큰 수를 구하라
# 조합을 구하고 중복을 제거 -> 각 경우마다 최댓값 여부를 확인하여 갱신
# 문자열로 변환, 다음 자리수가 현재 자리수보다 작으면 다음 경우로 넘어감
# 이중 반복문으로 조합 구현 -> 두 숫자의 곱을 구한 다음 함수로 확인 -> 단조증가하는 수라면 최대값과 비교
from itertools import combinations

def check(n):  # n은 곱을 문자열로 변환한 값
    for k in range(len(n) - 1):
        if s[k] > s[k + 1]:
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # comb_generator = combinations(numbers, 2)
    # cases = list(set(comb_generator))
    max_v = -1
    # for i, j in cases:
    for i in range(N - 1):
        for j in range(i + 1, N):
            s = str(numbers[i] * numbers[j])
            if check(s):
                max_v = max(int(s), max_v)

    print(f'#{tc} {max_v}')