T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    bus_stops = [0] * (N + 1)
    cnt = 0
    zeros = 1
    total = 0
    is_possible = True
    for i in stations:
        bus_stops[i] = 1
    print(bus_stops)
    # 종점에 도착할 수 없는 경우
    for i in range(0, N):
        if bus_stops[i] == bus_stops[i + 1] == 0:
            zeros += 1
            if zeros == K and (i + 1) != N:
                is_possible = False
        else:
            zeros = 1

    # 종점에 도착할 수 있는 경우
    if is_possible:
        current = N
        while current > 0:
            print('loop를 시작합니다.')
            if current - K <= 0:
                break
            elif bus_stops[current - K] == 1:
                print(f'{K}칸 이동하니 충전소가 있네요.')
                current -= K
                cnt += 1
                print(f'현재 위치는 {current}입니다.')
            else:
                for i in range(K - 1, 0, -1):
                    if bus_stops[current - i] == 1:
                        print(f'{K}칸 내에서 가장 가까운 충전소입니다.')
                        current -= i
                        cnt += 1
                        print(f'현재 위치는 {current}입니다.')
                        break
    if is_possible:
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc}', 0)