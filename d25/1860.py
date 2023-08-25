# 손님의 수, 빵을 만드는데 걸리는 시간, 한 번에 만들 수 있는 빵의 개수가 주어짐
# M초가 지날 때마다 빵의 총 개수가 K만큼 증가함
# 손님의 도착 시간이 손님의 수 만큼 주어짐
# 각 시점 별 누적손님의 수와 누적빵의 개수를 비교 -> 시점을 t, 0<= t < M(0*K), M<= t < 2*M(1*K), ...
# 누적손님수 <= cus[i]시점까지의 생산량이면 가능
# 도착시간별 손님의 수를 저장 -> p = [0]*11112, 가능한 도착시간은 0에서 11111

T = int(input())

p = [0]*11112
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    cus = list(map(int, input().split()))
    cus.sort()  # 오름차순으로 원본 리스트를 정렬
    result = 'Possible'
    for i in range(N):  # 누적손님수는 1부터 N까지 가능
        if i+1 > cus[i] // (M*K):  # 누적손님수와 해당시점까지의 생산량을 비교
            result = 'Impossible'
            break
    print(f'#{tc} {result}')
