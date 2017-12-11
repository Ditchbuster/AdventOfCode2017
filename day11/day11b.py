import math
with open('input.txt') as f:
    content = f.readlines()
count = 0
size = 100
grid = []
for i in range(size):
    grid.append([])
    for j in range(size):
        if (j % 2 == 0 and i % 2 == 0) or (j % 2 == 1 and i % 2 == 1):
            grid[i].append(0)
        else:
            grid[i].append(-1)
for line in content:
    x = 0
    y = 0
    hx = [0]
    hy = [0]
    md = 0
    parts = [x for x in line.replace('\n','').split(',')]
    for p in parts:
        if p == 'ne':
            x += 1
            y -= 1
        if p == 'nw':
            x -= 1
            y -= 1
        if p == 'n':
            y -= 2
        if p == 'se':
            x += 1
            y += 1
        if p == 'sw':
            x -= 1
            y += 1
        if p == 's':
            y += 2
        if x<=y:
            d = (abs(y)-abs(x))/2+abs(x)
        else:
            d = (abs(x))
        md = max(d,md)
    print(x,y,(abs(y)-abs(x))/2+abs(x),md)
