# 1은 가위, 2는 바위, 3은 보
# 몇 번째 카드를 집은 학생이 최종 승자인지 출력
# 카드의 번호가 동일한 경우 번호가 작은 학생이 승자인 걸로

T = int(input())
draw = [(1, 1), (2, 2), (3, 3)]
win_s = [(1, 3), (3, 1)]
win_r = [(1, 2), (2, 1)]
win_p = [(2, 3), (3, 2)]
def winner(arr, start, end):
    if (end - start) <= 1:  # 탐색 구간의 길이가 1또는 2인 경우
        if end == start:  # 구간의 길이가 1인 경우
            return [arr[end],end]  # 카드에 적힌 숫자와 학생의 번호를 리턴
        else:  # 구간의 길이가 2인 경우
            a, b = arr[start], arr[end]

    # if len(arr) <= 2:  # 가장 작은 그룹으로 나뉘어졌을 때
    #     if len(arr) == 1:  # 그룹의 크기가 1인 경우
    #         return arr[0]
    #     else:  # 그룹의 크기가 2인 경우
    winner(arr, start, (1+end)//2)
    winner(arr, (1+end)//2+1, N)


for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    winner(cards, 1, N)