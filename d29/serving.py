# 길이가 R인 윈도우 내에서 중복이 3 이상인 경우 NO를 출력
# R은 1부터 50,000까지
from collections import defaultdict
T = int(input())
for tc in range(1, T + 1):
    N, R = map(int, input().split())
    dishes = list(map(int, input().split()))
    ans = 'YES'


    def dup_check():
        global ans
        for i in range(N):  # 각 자리를 기준으로
            d = defaultdict(int)
            for j in range(i-R, i+R+1):
                if j < 0:
                    j = N-abs(j)
                elif j > N-1:
                    j %= N
                d[dishes[j]] += 1
            for v in d.values():
                if v >= 3:
                    ans = 'NO'
                    return
    dup_check()

    print(f'#{tc} {ans}')

#
foods = list(map(int, input().split()))
arr = foods * 2
DAT = [0] * 201
# 서빙 성공 여부 탐색 구간의 길이 -> 2 * R + 1
start = 0
end = 2 * R
flag = 0  # 서빙 성공 여부
# 첫번째 구간 탐색
for k in range(start, end):
    DAT[arr[k]] += 1
    if DAT[arr[k]] > 2:
        flag = 1
        break
# 슬라이딩 윈도우 기법
# end포인터가 리스트의 끝에 도착하거나, flag가 1이되면 종료
while end < 2 * N and flag == 0:
    DAT[arr[end]] += 1
    if DAT[arr[end]] > 2:
        flag = 1
        break
    # start포인터가 가리키는 요소의 빈도 1감소
    DAT[arr[start]] -= 1
    start += 1
    end += 1
