new_list = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0] * 5
temp = [0] * len(new_list)

for i in new_list:
    counts[i] += 1

for i in range(1, len(counts)):
    counts[i] += counts[i - 1]

# for j in reversed(new_list):
#     counts[j] -= 1
#     temp[counts[j]] = j

for j in range(len(temp) - 1, -1, -1):
    counts[new_list[j]] -= 1
    temp[counts[new_list[j]]] = new_list[j]

print(temp)