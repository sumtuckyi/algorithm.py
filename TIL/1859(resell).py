'''
ans = 0
max_v = price[N-1] 마지막 날의 매매가로 i+1에서 N-1 구간 최댓값을 초기화
for i : N-2 -> 0
    i번째 값과 i+1부터 마지막 인덱스까지의 구간의 최댓값을 순차적으로 비교
    ans += max-v - price[i] if max_v > price[i] else 0
    max_v = price[i]
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    ans = 0
    max_v = prices[N-1]
    for i in range(N-2, -1, -1):  # 리스트의 N-2번째에서 부터 구간 최댓값과 비교
        if max_v > prices[i]:  # 구간 최댓값이 현재 값보다 큰 경우
            ans += max_v - prices[i]
        else:  # 구간 최댓값이 현재 값보다 작은 경우(되팔기 안 함)
            max_v = prices[i]  # 구간 최댓값을 갱신
    print(f'#{tc} {ans}')
