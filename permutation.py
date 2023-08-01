cards = [4,4,4,3,4,5]
per = []

for a in range(0, 5 + 1):
    for b in range(0, 5 + 1):
        for c in range(0, 5 +1):
            for d in range(0, 5 + 1):
                for e in range(0, 5 + 1):
                    for f in range(0, 5 + 1):
                        if a != b and b != c and c != d and d != e and e != f:
                            a_list = [cards[a], cards[b], cards[c], cards[d], cards[e], cards[f]]
                            per.append(a_list)

print(per)