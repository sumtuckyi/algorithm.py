'''
동맹 -> 같은 서브트리
전쟁 결과 ->
par_idx = [a, b, c, d, e, f]
rank는 Z가 제일 높다
par2 = [c, d, f, d, e, f] # 부모노드를 저장
find(i)로 루트노드를 찾아 루트노드가 같으면 같은 동맹
find 결과 -> [f, d, f, d, e, f] => 동맹 2, 단일국가 1

'''
def find(n): # 루트노드를 찾는 함수
    if par[n] == n:
        return n
    else:
        par[n] = find(par[n])
    return par[n]

def alliance(n1, n2):
    if find(n1) != find(n2):  # 아직 동맹이 아닌 경우
        par[find(n2)] = find(n1)
    else:
        return

def defeat(lst):
    for i in lst:
        pop[i] = 0

def war(n1, n2):
    a1 = find(n1) # 첫번째 동맹의 루트
    a2 = find(n2) # 두번째 동맹의 루트
    alliance1 = []
    alliance2 = []
    p1, p2 = 0, 0 # 각 동맹의 인구
    winner = N
    for i in range(N):
        if find(i) == a1:
            p1 += pop[i]
            alliance1.append(i)
        elif find(i) == a2:
            p2 += pop[i]
            alliance2.append(i)
    if p1 == p2:
        defeat(alliance1)
        defeat(alliance2)
    elif p1 > p2:
        defeat(alliance2)
    else:
        defeat(alliance1)


N = int(input())  # 국가의 수
pop = list(map(int, input().split()))  # 국가별 인구수
T = int(input()) # 행위의 수
# rank = [i for i in range(N)]
par = [i for i in range(N)] # 부모노드 초기화
for _ in range(T):
    aow, c1, c2 = input().split()
    if aow == 'alliance':
        alliance(ord(c1)-65, ord(c2)-65)
    else:
        war(ord(c1)-65, ord(c2)-65)
# 살아남은 국가수
cnt = 0
for i in range(N):
    if pop[i]:
        cnt += 1
print(cnt)