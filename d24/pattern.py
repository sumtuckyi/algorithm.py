# 패턴에서 반복되는 부분의 최소 길이를 구하라
'''
마디의 길이를 1에서부터 카운트 : i = 1
r = arr[:i+1] # 마디
ans = 0
if pattern[i:2*i] == r:  # 마디의 길이가 i일 때, 반복되는지 확인
    ans = i
'''
T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    i = 1
    while True:
        r = pattern[:i]  # 마디의 길이는 1부터 시작
        if pattern[i:2*i] == r:
            ans = i
            break
        else:
            i += 1
    print(f'#{tc} {ans}')

# 동일한 토큰이 한 마디 내에서 반복되는 경우도 고려하기
# 1부터 10일 때까지 모두 검토하고 반복되는 마디의 길이가 2개 이상인 경우에는
# 재귀함수 이용
