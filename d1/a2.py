def adj_check(x, y, a, b): # 행 열 행 열 / 현재까지 패스에 추가된 셀에 현재 탐색 셀이 인접하는지 확인
    if x % 2 == 0:  # 셀의 행이 짝수인 경우
        if (a, b) in [(x-1, y), (x, y+1), (y+1, x+1), (x+1, y), (x-1, y-1), (x, y-1)]:
            return 1
    else:
        if (a, b) in [(x-1, y), (x-1, y+1), (x, y+1), (x-1, y), (x, y-1), (x-1, y-1)]:
            return 1
    return 0


def back_tracking(x, y, path, level):  # (x,y)를 첫번째 셀로 패스에 추가했을 때 가능한 모든 경우에서의 사용자 수를 계산
    if level == 3:
        total = 0
        # if path not in p_set: # 아직 나온 적 없는 조합인 경우에만
        #     p_set.add(path)
        for a, b in path:
            total += comb[a][b]
            result.append(total)
        print(path, total)
        return

    visited[x][y] = 1  # 패스에 추가된 셀을 체크
    # 나머지 모든 셀을 탐색
    for i in range(H):
        for j in range(W):
            for l, m in path: # 현재로서 패스에 담겨 있는 셀에 대하여
                if adj_check(l, m, i, j) and visited[i][j] == 0:  # 현재 탐색 셀이 그 중 적어도 하나와 인접하고 아직 추가되지 않았다면
                    back_tracking(i, j, path + [(i, j)], level + 1)  # 추가하고 다음에 포함시킬 셀을 탐색
                    visited[i][j] = 0  # 원상복구


T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    comb = [list(map(int, input().split())) for _ in range(H)]  # 셀별 사용자 수
    result = []  # 4개의 셀을 선택하는 모든 경우에서 각각의 편익
    p_set = set()
    for i in range(H):
        for j in range(W):
            # 한 개의 셀을 시작점으로 선택할 때마다 방문확인 배열 초기화
            visited = [[0 for _ in range(W+1)] for _ in range(H+1)]
            back_tracking(i, j, [(i, j)], 0)

    print(f'#{tc} {max(result)}')