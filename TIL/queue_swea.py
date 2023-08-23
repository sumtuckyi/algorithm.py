# 화덕피자
T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕의 크기와 피자의 개수
    pies = list(map(int, input().split()))
    cq = [0]*(N)  # 화덕
    index = N  # 다음에 들어갈 피자의 번호
    baked = []
    for i in range(N):  # 처음에 화덕 채우기
        cq[i] = [pies[i], i]
    while len(baked) != M:
        for i in range(N):
            if cq[i] == [0, 0]:
                continue
            else:  # 피자가 있는 경우
                cq[i][0] = cq[i][0]//2  # 녹인다.
                if cq[i][0] == 0:  # 치즈가 다 녹았다면
                    baked.append(cq[i])  # 꺼낸 피자를 순서대로 담는다.
                    if index == M:  # 더 이상 넣을 피자가 없는 경우
                        cq[i] = [0, 0]  # 비워놓기
                    else:
                        cq[i] = [pies[index], index]  # 새 피자 넣기
                        index += 1  # 다음에 들어갈 피자 번호 갱신

    print(f'#{tc} {baked[-1][1]+1}')

#
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕의 크기와 피자의 개수
    pies = list(map(int, input().split()))
    # 피자 인덱스와 치즈의 양을 저장할 리스트
    # enumerate(list)는 인덱스와 값을 tuple로 반환함
    pizzas = [[i+1, p] for i, p in enumerate(pies)]
    oven = pizzas[:N]  # 화덕에 처음 넣는 피자들
    remain = pizzas[N:]

    while len(oven) > 1:  # 화덕에 한 개의 피자만 남을 때까지 반복
        now = oven.pop(0)  # 화덕에서 피자꺼내기
        now[1] //= 2  # 치즈의 양을 반으로 줄이기
        if now[1] == 0:  # 치즈가 모두 녹았다면 해당 피자를 꺼내고
            if remain:  # 남은 피자가 있다면
                oven.append(remain.pop(0))  # 피자를 차례로 화덕에 넣기
        else:  # 아직 다 녹지 않은 경우 화덕에 다시 넣기(큐의 후단으로 들어감)
            oven.append(now)

    print(f'#{tc} {oven[0][0]}')  # 가장 마지막에 화덕에 남는 피자의 번호 출력
