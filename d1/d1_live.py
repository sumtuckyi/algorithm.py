4366
2817
1861
10966

# 4366문
'''
주어진 n자리의 이진수(0번째 비트부터 n-1번째 비트까지)에서 값이 틀린 자리가 무조건 1개이므로
n가지 경우를 모두 생성(0이거나 1이거나)
주어진 m자리의 3진수도 마찬가지이므로
m*2가지 경우를 모두 생성(0이거나 1이거나 2)

가능한 모든 경우를 어떻게 생성?
-> 비트 연산을 이용한다면,
XOR 활용하여 이진수의 비트만큼 반복하여 한 자리씩 비트를 반전시키면
가능한 n가지 경우를 모두 도출할 수 있음
int(input(), 2)로 입력을 받음

3진수의 m*2가지 경우 생성하기
0 : 1을 더한 뒤 %3, 2를 더한 뒤 %3 -> 1과 2로 변환가능
1 : 
2 :

'''

T = int(input())
for tc in range(1, T + 1):
    A = input()  # 2진수
    B = list(map(int, input()))  # 3진수
    ans = 0
    N = len(A)
    M = len(B)
    binary = int(A, 2)  # 2진수를 정수로 변환
    bin_list = [0] * N  # 각 비트를 반전시킨 N개의 수 저장
    # 0에서 n-1비트 순으로 2진수를 한 자리씩 비트 반전시키기
    for i in range(N):
        bin_list[i] = binary ^ (1<<i)
    # 0에서 m-1비트 순으로 3진수에 대해서도 동일한 작업
    for i in range(M): #3진수의 i번째 비트에 대한 작업
        num1 = 0  # (B[i]+1)%3
        num2 = 0  # (B[i]+2)%3
        for j in range(M):
            if i != j:
                num1 = num1*3 + B[j]
                num2 = num1*3 + B[j]
            else:
                num1 = num1*3 + (B[j]+1)%3
                num2 = num2*3 + (B[j]+2)%3
        # 각 비트의 작업이 끝날 때마다 일치하는 수가 있는지 확인
        if num1 in bin_list:
            ans = num1
            break
        if num2 in bin_list:
            ans = num2
            break
    print(f'#{tc} {ans}')

# 2817문
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(1<<N):
        s = 0  # 부분집합의 합
        for j in range(N):  # j번째 비트
            if i&(1<<j):  # i의 j번째 비트가 0이 아니라면
                s += arr[j]
        if s == K:
            cnt += 1

# 1861문
'''
풀이 1)
맵에서 시작점을 지정
시작점을 기준으로 4방향 탐색 
조건을 만족하는 칸이 있다면
해당 칸으로 이동하고(시작점 갱신) 이동횟수를 카운트 -> 반복문 종료 -> 이동횟수 최대값과 비교하여 갱신
반복문이 중단되지 않고 끝까지 돈 경우에는 조건을 만족한 경우가 없다는 것이므로
'가장 작은 방번호 1'을 출력
=> 이 방법 만으로는 중복된 연산이 발생함. 
중복 연산을 줄이기 위해서는 각 칸에서 출발하는 경우에 갈 수 있는 최대 이동횟수를 
dp배열에 저장해놓고 재방문시 dp배열을 갱신 

풀이 2)
중복된 숫자가 없다는 문제의 조건을 이용
(N*N+1)길이의 카운트 배열을 만들어서 해당 인덱스를 값으로 가지는 칸이 연결된 방에 해당되면
1로 값을 바꿔준다.
반복문 종료 후에 카운트 배열을 탐색하여 연속한 1의 개수가 최대가 되는 경우와
그 경우의 시작 인덱스를 확인
(이때 배열을 뒤에서부터 탐색하면 최대 길이가 되는 경우의 방의 번호의 최솟값을 바로 구할 수 있다)
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * (N*N+1)
    for i in range(N):
        for j in range(N):
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0<= arr[i+di][j+dj] < N and arr[i][j] + 1 == arr[i+di][j+dj]:
                    cnt[arr[i][j]] += 1

    max_cnt = 0  # 연결된 방의 최대 개수
    max_start = 0  # 연결된 방의 개수가 최대일 때 시작점의 번호
    cnt2 = 0
    for k in range(N*N, 0, -1):
        if cnt[k]:  # 카운트배열의 k번째 값이 1이면
            cnt2 += 1
            if max_cnt < cnt2:
                max_cnt = cnt2
                max_start = k
            elif max_cnt == cnt2:  # 연결된 방의 개수가 최댓값과 동일한 경우
                max_start = k  # 시작점 방번호만 갱신
        else:  # 카운트배열의 k번째 값이 1이면
            cnt2 = 0

    print(f'#{tc} {max_start} {max_cnt+1}')

# 10966문
'''
땅인 지점 각각에서 물로 이동하는 최단거리를 구하라
1.2차원 dp배열 이용하여 땅인 각 칸에서 물로 가는 최단 거리를 dp배열에 저장
2중 for문을 이용하여 dp배열을 채우고 
2중 for문으로 완성된 dp배열을 돌면서 최단거리를 출력
2.물인 지점을 기준으로 너비 우선탐색을 실시 -> 탐색 중 방문한 땅인 지점이 이미 방문된 곳이라면 물로부터의 최소거리와 현재 물인 지점으로부터의 거리를 비교하여 더 작은 값으로 갱신

'''
from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 지도의 행과 열
    b = [list(input()) for _ in range(N)]
    w = []
    q = deque()
    cnt = [[0 for _ in range(M)] for _ in range(N)]
    v = [[0 for _ in range(M)] for _ in range(N)]
    # 물인 지점을 저장
    for i in range(N):
        for j in range(M):
            if b[i][j] == 'W':
                w.append((i, j))
    # 물인 칸을 기준으로 탐색
    # 물인 칸을 모두 큐에 넣기
    for i, j in w:
        q.append((i, j))
    while q:
        x, y = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if b[x+di][y+dj] == 'L' and v[x+di][y+dj] == 0:  # 땅인 칸을 발견한 경우 아직 방문하지 않았다면
                cnt[x+di][y+dj] = cnt[x][y] + 1  # 물로부터의 거리
                v[x+di][y+dj] = 1
                q.append((x+di, y+dj))
    print(cnt)
    print(v)



