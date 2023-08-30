# P가 출발점
# K를 모두 방문해야함
# 루트에 있는 지점 중 최고 고도와 최저고도만 알면 됨
from collections import deque
N = int(input())
b = [list(input()) for _ in range(N)]  # 마을지도
alt = [list(map(int, input().split())) for _ in range(N)]  # 각 지점의 고도
tp_lst = []
print(b)
for i in range(N):
    for j in range(N):
        tp_lst.append((i, j, alt[i][j], b[i][j]))
# 고도 정렬하기
tp_lst.sort(key=lambda x: x[2])
print(tp_lst)
# 탐색 구간에 속한 노드가 모두 연결되어 있는지 확인하는 함수
def bfs(a, b): #(a, b)좌표에서 시작해서 탐색 구간 내에 있는 모든 좌표에 도달 가능한지
    visited = [[0 for _ in range(N)] for _ in range(N)]
    q = deque([(a, b)])
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(s, e+1):
            if (tp_lst[i][0], tp_lst[i][1]) in [(a-1, b-1), (a-1, b), (a-1, b+1), (a, b-1), (a, b+1), (a+1, b-1), (a+1, b), (a+1, b+1)]:
                q.append((tp_lst[i][0], tp_lst[i][1]))
                visited[tp_lst[i][0]][tp_lst[i][1]] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                cnt += 1
    if cnt == e-s+1:  # 경로가 끊김 없이 완성되면
        return 1

# K, P의 위치 찾기
coord_p = (0,0)
coords_k = []
alts = []  # 반드시 들려야 하는 지점의 고도
result = [] # 가능한 경우의 고도 저장
for i in range(N):
    for j in range(N):
        if b[i][j] == 'P':
            coord_p = i, j
            alts.append(alt[i][j])
        elif b[i][j] == 'K':
            coords_k += [(i, j)]
            alts.append(alt[i][j])
print('alts', alts)
# 탐색 시작점: 마을에서 가장 고도가 낮은 지점
# 탐색 종료점: 집과 우체국 중 가장 고도가 높은 지점
s = 0
e = 0
for i in range(N*N-1, -1, -1):  # 높은 고도부터 탐색
    if tp_lst[i][3] == 'K' or tp_lst[i][3] == 'P':
        e = i
        break

while e < N * N and s < e:
    # 현 구간에 k,p가 모두 포함되는지 확인
    cnt = 0
    for i in range(s, e+1):
        if tp_lst[i][3] == 'K' or tp_lst[i][3] == 'P':
            cnt += 1
            print('cnt', cnt)
        if cnt == len(alts): # 현재 구간에 모든 집과 우체국이 포함되는 경우이면서
            if bfs(tp_lst[s][0], tp_lst[s][1]):  # 현 구간에서 경로가 만들어지는 경우
                print(tp_lst[s][0], tp_lst[s][1])
                result.append(tp_lst[e][2] - tp_lst[s][2])  # 고도 차이 계산
                s += 1  # 범위 좁히기
            else:  # 현 구간에서 경로가 만들어지지 않는 경우
                e += 1  # 범위 늘리기
        else: #현 구간에 모두 포함되지는 않는 경우
            e += 1
print(result)