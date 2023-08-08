# pattern matching
# Brute Force : 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교
p = 'is'
t = 'This is a book~!'
M = len(p)
N = len(t)

# p가 t에 존재하는지 여부를 확인
def brute_force(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:  # 일치하지 않는 경우
            i = i -j  # 텍스트의 비교 시작점에서 바로 다음 인덱스(시작점)로 이동
            j = -1  # 패턴의 처음 인덱스로 돌아감
        i = i + 1
        j = j + 1
    if j == M:  # 패턴의 마지막 인덱스까지 비교가 끝난 경우
        return i - M
    else:
        return -1

# 이중 for문으로도 구현

# KMP 알고리즘 : 패턴 내에서 중복되는 구간이 존재하는 경우, 특정 인덱스에서 매칭이 실패하였을 때 패턴 내에서 다시 매칭을 시작할 지점을 따로 저장해둔다.
def kmp(t, p):
    lps = [0] * (M + 1)

    j = 0
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    print(lps)



# 보이어-무어 알고리즘
