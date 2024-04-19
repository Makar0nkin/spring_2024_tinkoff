from itertools import product

def process_input(s: str) -> str:
    new_str: str = ''
    for ch in s.lower():
        match ch:
            case 'w':
                new_str += '-'
            case '.':
                new_str += '='
            case 'c':
                new_str += '+'
    return new_str

n = int(input())
forest: list[str] =  []

for i in range(n):
    forest.append(process_input(input()))

possible_moves_list: list[list[tuple[int, int]]]  = [[] for _ in range(n-1)]
for i in range(n-1):
    for (j_0, cell_0), (j_1, cell_1) in product(*map(enumerate, [forest[i], forest[i+1]])):
        if cell_0 == '-' or cell_1 == '-' or \
                (j_0, j_1) in [(0, 2), (2, 0)]:
            continue

        possible_moves_list[i].append((j_0, j_1))

possible_moves_list = list(filter(lambda l: l != [], possible_moves_list))

possible_ways: list[tuple[tuple[int, int], ...]] = []
for possible_way_candidate in product(*possible_moves_list):
    js_prev = (possible_way_candidate[0])
    for js_curr in possible_way_candidate[1:]:
        if js_prev[1] != js_curr[0]:
            break
        js_prev = js_curr
    else:
        possible_ways.append(possible_way_candidate)

possible_ways_processed: list[list[int]] = [[] for _ in possible_ways]
for i, possible_way in enumerate(possible_ways):
    possible_ways_processed[i].extend(possible_way[0])
    for _, j_1 in possible_way[1:]:
        possible_ways_processed[i].append(j_1)

possible_ways_values: list[int] = [0 for _ in possible_ways_processed]

for way_i, possible_way in enumerate(possible_ways_processed):
    for i, j in enumerate(possible_way):
        value = 1 if forest[i][j] == '+' else 0
        possible_ways_values[way_i] += value

print(max(possible_ways_values or [0]))
