number = int(input())
for num in range(1, number + 1):
    num = str(num)
    clap = num.count('3') + num.count('6') + num.count('9')

    if clap == 0:
        print(num, end=' ')
    else:
        print("-" * clap, end=' ')


