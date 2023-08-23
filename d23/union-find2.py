from collections import defaultdict

def find(n):
    if par[n] != n:
        par[n] = find(par[n])
    return par[n]


def union(a, b):
    if find(a) != find(b):  # 같은 팀이 아닌 경우
        par[find(a)] = find(b)  # 앞의 노드가 속한 팀을 뒤의 노드의 팀에 합치기
    else:  # 이미 같은 팀인 경우
        return


N = int(input())  # 명령의 수

par = {chr(i): chr(i) for i in range(65,90+1)}
# for i in range(1, 26+1):
#     par[i] = i

for i in range(N):
    n1, n2 = input().split()  # 서로 다른 그룹일 경우 합칠 두 노드
    union(n1, n2)

# 조직된 팀의 개수 구하기
count = [0]*27
cnt = 0  # 조직된 팀의 개수
g = 0  # 개인연주자를 포함한 그룹의 수
new = defaultdict(int)
for value in par.values():
    new[value] += 1
for value in new.values():
    if value > 1:
        cnt += 1
for key, value in par.items():
    if key == value:
        g += 1
print(cnt)
print(g-cnt)

