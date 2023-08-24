# from itertools import permutations
#
#
# def right(idx, N):  # 해당 인덱스를 기준으로 오른쪽 탐색
#     visited[idx] = 1
#     k = 1
#     while True:
#         if idx + k <= N - 1:  # 탐색 중인 풍선이 리스트 범위 내인 경우
#             if not visited[idx + k]:  # 오른쪽에 아직 터지지 않은 풍선이 있다면
#                 rb = scores[idx + k]
#                 return rb
#             elif visited[idx + k]:  # 이미 터진 풍선인 경우
#                 k += 1  # 한 칸 더 이동
#                 continue  # 다음 반복으로
#         else:  # 탐색 위치가 리스트를 벗어난 경우
#             return 0  # 오른쪽에 남은 풍선이 없음
#
#
# def left(idx, N):
#     visited[idx] = 1
#     k = -1
#     while True:
#         if idx + k > 0:  # 탐색 중인 풍선이 리스트 범위 내인 경우
#             if not visited[idx + k]:  # 왼쪽에 아직 터지지 않은 풍선이 있다면
#                 lb = scores[idx + k]
#                 return lb
#             elif visited[idx + k]:  # 이미 터진 풍선인 경우
#                 k -= 1  # 한 칸 더 이동
#                 continue  # 다음 반복으로
#         else:  # 탐색 위치가 리스트를 벗어난 경우
#             return 0  # 왼쪽에 남은 풍선이 없음
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())  # 풍선의 개수 = 사격 횟수
#     scores = list(map(int, input().split()))
#     cases = list(permutations(range(0, N), N))
#
#     max_v = 0
#     for case in cases:  # 풍선을 터뜨리는 순서 집합마다
#         visited = [0] * N
#         total = 0
#         for num in case:  # 터뜨리는 풍선마다
#             cb = num  # 현재 터진 풍선의 번호
#             rb = right(cb, N)
#             lb = left(cb, N)
#             # print(f'{num}번째 풍선을 터뜨렸고 왼쪽 풍선은{lb}, 오른쪽 풍선은{rb}')
#             if rb and lb:  # 인접풍선이 두 개이면
#                 total += (rb * lb)
#             elif rb or lb:  # 인접풍선이 하나이면
#                 total += (rb + lb)
#             else:  # 마지막 풍선인 경우
#                 total += scores[num]
#         if max_v < total:
#             max_v = total
#
#     print(f'#{tc} {max_v}')




from itertools import permutations


def right(idx, N):  # 해당 인덱스를 기준으로 오른쪽 탐색
    visited[idx] = 1
    k = 1
    while True:
        if idx + k <= N - 1:  # 탐색 중인 풍선이 리스트 범위 내인 경우
            print(f'오른쪽으로 {idx+k}번째 풍선 탐색 중')
            if not visited[idx + k]:  # 오른쪽에 아직 터지지 않은 풍선이 있다면
                rb = scores[idx + k]
                return rb
            elif visited[idx + k]:  # 이미 터진 풍선인 경우
                k += 1  # 한 칸 더 이동
                # continue  # 다음 반복으로
        else:  # 탐색 위치가 리스트를 벗어난 경우
            return 0  # 오른쪽에 남은 풍선이 없음


def left(idx, N):
    visited[idx] = 1
    k = 1
    while True:
        if idx - k >= 0:  # 탐색 중인 풍선이 리스트 범위 내인 경우
            print(f'왼쪽 풍선 탐색 중, {idx - k}번째 풍선')
            if not visited[idx - k]:  # 왼쪽에 아직 터지지 않은 풍선이 있다면
                lb = scores[idx - k]
                return lb
            elif visited[idx - k]:  # 이미 터진 풍선인 경우
                k -= 1  # 한 칸 더 이동
                continue  # 다음 반복으로
        else:  # 탐색 위치가 리스트를 벗어난 경우
            return 0  # 왼쪽에 남은 풍선이 없음


T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 풍선의 개수 = 사격 횟수
    scores = list(map(int, input().split()))
    cases = list(permutations(range(0, N), N))

    max_v = 0
    for case in cases:  # 풍선을 터뜨리는 순서 집합마다
        if case[0] == 0 or case[0] == N-1: # 첫번째나 마지막 풍선을 먼저 터뜨리는 경우는 제외
            continue
        visited = [0] * N
        total = 0
        print('새로운 케이스 시작', case)
        for num in case:  # 터뜨리는 풍선마다
            cb = num  # 현재 터진 풍선의 번호
            print(f'{cb}번째 풍선을 터뜨리는 경우')
            rb = right(cb, N)
            lb = left(cb, N)
            print(f'{num}번째 풍선을 터뜨렸고 왼쪽 풍선은{lb}, 오른쪽 풍선은{rb}')
            print(visited)
            if rb and lb:  # 인접풍선이 두 개이면
                total += (rb * lb)
                print(f'양쪽의 풍선을 터뜨려서 {rb*lb}점을 얻음')
            elif rb or lb:  # 인접풍선이 하나이면
                total += (rb + lb)
                print(f'한쪽의 풍선을 터뜨려서 {rb + lb}점을 얻음')
            else:  # 마지막 풍선인 경우
                total += scores[num]
                print(f'마지막 풍선을 터뜨려서 {scores[num]}점을 얻음')
        if max_v < total:
            max_v = total

    print(f'#{tc} {max_v}')




