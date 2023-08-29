# 샘플을 오름차순으로 정렬
# 샘플의 양 끝에서 탐색을 시작하여, 두 포인터가 교차하게 되면 탐색 종료

N = int(input())  # 샘플의 수(최소 2개)
s = list(map(int, input().split()))
s.sort()  # 샘플을 오름차순으로 정렬
start, end = 0, N-1
min_v = float('inf')  # 가능한 오염도 중 최솟값
min_s1, min_s2 = 0, 0  # 혼합하였을 때 오염도가 가장 낮은 경우 두 샘플
while start < end:
    p = s[start] + s[end]
    temp = abs(p)  # 오염도 계산
    if temp == min_v and (abs(min_s1)+abs(min_s2)) < (abs(s[start])+abs(s[end])):  # 오염도가 같은 경우에는 절대값의 합이 큰 샘플 선택
        min_s1, min_s2 = s[start], s[end]
    elif temp < min_v:  # 오염도가 기존값보다 낮은 경우에는 갱신
        min_s1, min_s2 = s[start], s[end]
        min_v = temp
    # start와 end 인덱스 조정
    if p < 0:
        start += 1
    else:
        end -= 1

print(f'{min(min_s1, min_s2)} {max(min_s1, min_s2)}')

# exit()사용 가능
while start < end:
    p = s[start] + s[end]
    if p == 0:
        print(s[start], s[end])
        exit()  # 파이썬 파일 자체의 실행을 종료하므로 이하코드가 아예 실행되지 않는다.
    if min_v > abs(p):
        min_v = abs(p)
        min_s1, min_s2 = s[start], s[end]
    if p > 0:
        end -= 1
    else:
        start += 1
