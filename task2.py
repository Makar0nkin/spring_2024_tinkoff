n, m = [int(i) for i in input().split(' ')]
matrix: list[list[int]] = [[int(num) for num in input().split(' ')] for _ in range(n)]
matrix.reverse()
rotated_matrix: list[list[int]] = [[] for _ in range(m)]

for row in matrix:
    for i, num in enumerate(row):
        rotated_matrix[i].append(num)

for row in rotated_matrix:
    print(*row)