T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕의 크기와 피자의 개수
    pies = list(map(int, input().split()))
    cq = [0]*(N+1)  # 화덕
    index = N  # 다음에 들어갈 피자의 번호
    baked = []
    for i in range(N):  # 처음에 화덕 채우기
        cq[i] = [pies[i], i]  # 치즈의 양과 피자의 번호
    while len(baked) != M:  # 새로운 피자를 넣는 작업
        for i in range(N):  # 한바퀴 돈 피자의 치즈양 확인하기
            if cq[i] == [0, 0]:  # 자리가 비어있는 경우
                continue
            else:  # 피자가 있는 경우
                cq[i][0] //= 2  # 녹인다.
                if cq[i][0] == 0:  # 치즈가 다 녹았다면
                    baked.append(cq.pop(i))  # 꺼낸 피자를 순서대로 담는다.
                    if index == M:  # 더 이상 넣을 피자가 없는 경우
                        cq[i] = [0, 0]  # 비워놓기
                    else:
                        cq[i] = [pies[index], index]  # 새 피자 넣기
                        index += 1  # 다음에 들어갈 피자 번호 갱신

    print(f'#{tc} {baked[-1][1]}')
