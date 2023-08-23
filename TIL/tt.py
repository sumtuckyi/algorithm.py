def solution(players, callings):

    map = {i: 0 for i in players}
    for i in callings:
        map[i] += 1
    for i in map:
        players.insert(players.index(i) - map[i], players.pop(players.index(i)))
    return players


players1 =['m', 's', 'p', 'k', 'mi']
callings1 = ['k', 'k', 'mi', 'mi']

print(solution(players1, callings1))