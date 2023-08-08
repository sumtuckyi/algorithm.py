T = int(input())

for tc in range(1, T + 1):
    s1 = input()
    s2 = input()

    max_v = 0
    for i in range(len(s1)):
        cnt = 0
        for j in range(len(s2)):
            if s2[j] == s1[i]:
                cnt += 1
        if max_v < cnt:
            max_v = cnt

    print(f'#{tc} {max_v}')


# count()사용
T = int(input())

for tc in range(1, T + 1):
    s1 = input()
    s2 = input()
    cnt_list = []

    for i in s1:
        cnt_list.append(s2.count(i))

print(f'#{tc} {max(cnt_list)}')