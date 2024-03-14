arr = [7, 7, 10, 5, 2, 2]

max_diff = 0
indices = []

# Проходим по всем парам чисел
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        diff = abs(arr[i] - arr[j])
        if diff > max_diff:
            max_diff = diff
            indices = [i, j]
        elif diff == max_diff and [i, j] not in indices:
            indices.extend([i, j])

print(indices)
