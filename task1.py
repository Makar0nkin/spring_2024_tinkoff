from collections import Counter

n = int(input())
marks =  [int(m) for m in input().split(' ')]
res = -1

for i in range(n-7+1):
    sub_marks_d = Counter(marks[i:i+7])
    if sub_marks_d[2] or sub_marks_d[3]:
        continue
    res = sub_marks_d[5] if res < sub_marks_d[5] else res

print(res)