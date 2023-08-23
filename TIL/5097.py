T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))

    for i in range(M):
        q.append(q.pop(0))


    print(f'#{tc} {q[0]}')


# front, rear로 해보기

#
