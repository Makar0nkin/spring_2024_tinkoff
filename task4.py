n, rotation_direction = input().split(' ')
n = int(n)

matrix: list[list[int]] = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

half: int = n // 2
middle: int = (n + 1) // 2
swap_operations_list: list[list[int]] = []
for i in range(half):
    for j in range(i, middle):
        if rotation_direction == "R":
            swap_operations_list.extend([[i, j, n - j - 1, i],
                                         [n - j - 1, i, n - i - 1, n - j - 1],
                                         [n - i - 1, n - j - 1, j, n - i - 1]])
        else:
            swap_operations_list.extend([[i, j, j, n - 1 - i],
                                         [j, n - 1 - i, n - 1 - i, n - 1 - j],
                                         [n - 1 - i, n - 1 - j, n - 1 - j, i]])

print(len(swap_operations_list))
for swap_operation in swap_operations_list:
    print(" ".join(map(str, swap_operation)))
