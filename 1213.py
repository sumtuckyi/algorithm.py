T = 10

for tc in range(1, 10 + 1):
    c_num = int(input())
    pattern = input()
    text = input()
    # m = len(pattern)
    # n = len(text)

    def find_string(p, t):
        cnt = 0
        for i in range(len(t)-len(p)+1):
            if t[i:i+len(p)] == p:
                cnt += 1
        return cnt

    result = find_string(pattern, text)
    print(f'#{tc} {result}')