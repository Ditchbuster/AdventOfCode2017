from collections import deque

with open('input.txt') as f:
    content = f.readlines()
count = 0
for line in content:
    parts = [int(x) for x in line.split()]
    s = parts[0]
    p = 1
    l = 2
    for i in range(2,50000001):
        p = (p+s)%l+1
        if p == 1:
            out = i
        l += 1
    print(out)