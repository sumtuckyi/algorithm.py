# 이중 for문 대신 투 포인터를 사용
# 투 포인터를 이용하면 loop마다 두 포인터 중 하나만 값이 바뀜
# 포인터를 한 번 이동시킬 때마다 조건을 만족하는지 검토
# 문제의 조건에 따라 포인터의 초기 위치가 달라짐
'''
https://programmers.co.kr/learn/courses/30/lessons/67258
https://www.acmicpc.net/problemset?sort=ac_desc&algo=80
'''

N, M = map(int, input().split())
seq = list(map(int, input().split()))

start, end = 0, 0
int_sum = seq[0]
cnt = 0
while True:
    # 현재 구간합이 M보다 크거나 같은 경우 -> 범위 축소
    if int_sum >= M or end == N:
        int_sum -= seq[start]
        start += 1
    # 현재 구간합이 M보다 작은 경우 -> 범위 확장
    elif int_sum < M:
        int_sum += seq[end]
        end += 1
    # 현재 구간합이 M과 같은 경우 카운트
    if int_sum == M:
        cnt += 1
    if end == N:
        break
print(cnt)
