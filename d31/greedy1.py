# 최대 M대의 트럭을 한 번만 이용
# 트럭 한 대당 N개의 컨테이너 중에 적재용량에 맞는 것에 한하여 하나를 선택하여 적재할 수 있다
# 이때 M대의 트럭이 운송하는 컨테이너 중량의 합이 최대가 되는 경우를 구하라
# 컨테이너 수와 트럭 수의 대소관계는 정해진 규칙이 없다.
# 용량이 큰 트럭이 먼저 컨테이너를 고른다.
# 컨테이너를 하나도 옮기지 못 하는 경우도 있음 -> 0을 출력
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))
    t.sort(reverse=True)  # 적재용량이 큰 순서대로 정렬
    c.sort(reverse=True)
    s = []  # 운송하는 컨테이너 저장
    j = 0
    for i in range(M):
        while True:
            # 현재 탐색하는 컨테이너가 존재하는지 확인
            if j <= N - 1:
                if t[i] >= c[j]:  # 컨테이너를 싣을 수 있는 경우
                    s.append(c[j])
                    j += 1
                    break  # while문을 종료하고 다음 트럭으로 넘어감
                else:  # 컨테이너를 싣을 수 없는 경우
                    j += 1  # 다음 컨테이너를 확인(트럭은 그대로)
            # 모든 컨테이너를 다 돈 경우
            else:
                break  # 탐색 중지
    if s:  # 하나라도 운송 가능하다면
        ans = sum(s)
    else:  # 운송 가능한 컨테이너가 없다면
        ans = 0
    print(f'#{tc} {ans}')

#
result = 0
j = -1
for i in range(M):
    while j < N - 1:
        j += 1
        # 컨테이너가 현재 트럭의 적재용량보다 작거나 같으면
        if t[i] >= w[j]:
            result += w[j]
            break
print(f'#{tc} {result}')