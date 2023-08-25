# 포장할 수 없으면 -1(한 상자에 들어가는 당근의 수가 전체 당근 과반인 경우)
# 포장하는 경우에도 상자별 당근의 개수 차이가 최소가 되게끔 해야한다.
# 대, 중, 소는 상대적으로 당근의 크기를 오름차순으로 정렬하여 판단
# 당근의 개수는 최소 3개에서 최대 1000개이다.
# 당근의 크기는 1부터 30이다.
# 당근의 크기가 동일한 경우 반드시 같은 상자에 들어있어야 한다 -> 한 상자에 들어가는 당근 수의 최댓값을 결정
# 당근을 크기별로 정렬해서 상자의 가능한 구분점별로 포장조건을 만족하는지를 확인(이때 가능한 구분점의 탐색 순서는 상자별 개수 차이가 작은 경우부터)

# 포장 가능 여부를 판단
# def possible(lst):
#     for i in lst:
#         size[i] += 1
#     for i in size:
#         if i > N//2:  # 특정 사이즈의 당근이 전체 당근 수의 과반인 경우
#             return 0
#     return 1
#
# # 포장이 가능하다면 최소 몇 개의 차이로 포장이 가능한지 확인
#     if possible(carrots):


#
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 최소 3개에서 최대 1000개
    ci = list(map(int, input().split()))
    ci.sort()
    can = []  # 당근의 포장조건을 만족하는 개수 차이
    # 포장조건을 만족하는 모든 경우를 탐색
    # 당근이 담긴 리스트의 인덱스는 0부터 N-1까지
    for i in range(1, N-1):
        for j in range(i+1, N):
            a = ci[:i]  # 최소길이 1
            b = ci[i:j]  # 최소길이 1
            c = ci[j:]  # 최소길이 1
            if a[-1] == b[0] or b[-1] == c[0]:  # 같은 크기의 당근이 다른 상자에 담긴 경우
                continue
            # if len(a)*len(b)*len(c) == 0:  # 빈 상자가 있는 경우 -> 빈 상자가 있는 경우가 없는 듯..
            #     continue
            if len(a) > N//2 or len(b) > N//2 or len(c) > N//2:  # 한 상자가 과반인 경우
                continue
            # 상자 간 당근 개수의 차이가 상이한 경우에는 최댓값을 선정
            can.append(max(abs(len(a)-len(b)), abs(len(b)-len(c)), abs(len(a)-len(c))))
    try:
        print(f'{tc} {min(can)}')  # 각 경우마다 구해지는 당근 개수의 차이 중에서는 최솟값을 출력
    except:
        print(f'{tc} -1')