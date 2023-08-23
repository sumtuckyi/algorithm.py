# def bfs():
#     q = [(S, 0)]
#     visited = set()
#     while q:
#         cn, cnt = q.pop(0)
#         if cn == D:  # 큐에서 꺼낸 값이 목표값인 경우
#             return cnt
#         if cn not in visited:
#             visited.add(cn)
#             if 0 <= cn//2 <= 100000:
#                 q.append((cn//2, cnt+1))
#             if 0 <= cn*2 <= 100000:
#                 q.append((cn*2, cnt+1))
#             if 0 <= cn + 1 <= 100000:
#                 q.append((cn + 1, cnt+1))
#             if 0 <= cn - 1 <= 100000:
#                 q.append((cn - 1, cnt+1))
#
#
# S = int(input())  # 현재 채널
# D = int(input())  # 목표 채널
#
# bfs()
# print(bfs())


#
def bfs():
    q = [(s,'')]
    visited = set()
    while q:
        cpw, path = q.pop(0)  # cpw는 비밀번호, path는 누적된 동작을 담은 리스트
        if cpw == e:  # 큐에서 꺼낸 패스워드가 목표값과 같은 경우
            return path
        if cpw not in visited:
            visited.add(cpw)
            # D 동작 수행
            q.append(((cpw * 2) % 10000, path+'D'))
            # S
            if 0 <= cpw-1:
                q.append((cpw-1, path+'S'))
            else: # 현재 숫자가 0인 경우
                q.append((9999, path+'S'))
            # L
            q.append(((cpw % 1000) * 10 + (cpw // 1000), path+'L'))
            # R
            q.append(((cpw%10) * 1000 + (cpw // 10), path+'R'))


T = int(input())
for tc in range(1, T+1):
    s, e = map(int, input().split())
    print(bfs())