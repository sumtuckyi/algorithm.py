arr1 = [
    [3, 3, 5, 3, 1],
    [2, 2, 4, 2, 6],
    [4, 9, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 3, 5, 9, 2]
]


dx = [-1, 1, -1, 1]
dy = [-1, 1, 1, -1]

# 배열 내 모든 좌표에 대해 대각선 방향의 4칸에 위치한 값을 모두 더하였을 때 최대값이 되는 경우의 좌표를 구하라.


def cal_sum(arr):
    max_v = 0  # 최대값
    x1, y1 = 0, 0  # 최대값이 되는 경우의 좌표
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            x, y = i, j  # 기준점
            result = 0  # 각각의 기준점에서의 대각선 합
            direction = 0  # 방향전환 인덱스
            while direction < 4: # 4번의 방향탐색이 끝나면 반복문이 종료
                if 0 <= x + dx[direction] < 5 and 0 <= y + dy[direction] < 5:  # 이동 후의 좌표가 맵 내부인 경우에만 코드 실행
                    result += arr[x + dx[direction]][y + dy[direction]]
                    direction += 1  # 방향 전환
                else:
                    direction += 1  # 해당 방향이 맵 밖인 경우에는 방향만 전환
                    continue
            if max_v < result:  # 4번의 덧셈이 끝난 결과값이 역대 최대값인지 확인
                max_v = result
                x1, y1 = i, j  # 해당 기준점의 좌표 저장
    print(x1, y1)






cal_sum(arr1)