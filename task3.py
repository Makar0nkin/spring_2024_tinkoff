def print_dict(d: dict) -> None:
    def _dict_to_str(d: dict, depth: int = 0) -> str:
        s = '\n'
        for k, v in sorted(d.items(), key=lambda kv: int(''.join(map(str, map(ord, kv[0]))))):
            s += '  ' * depth + f'{k}{v if not isinstance(v, dict) else _dict_to_str(v, depth+1)}'
        return s
    print(_dict_to_str(d)[1:])

n = int(input())
directory_tree: dict = {}
for _ in range(n):
    abs_path: list[str] =  input().split('/') 
    dt_link: dict = directory_tree
    for dir in abs_path:
        if not dt_link.get(dir):
            dt_link[dir] = {}
        dt_link = dt_link[dir]
        
print_dict(directory_tree)