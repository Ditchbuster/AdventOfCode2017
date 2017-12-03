#### just did the math on part 1, no code

import math
#with open('test.txt') as f:
input = 361527
dir = 0 # east, 1 north, 2 west, 3 south
size = 10
grid = []
for i in range(size):
    grid.append([0]*size)
x = int((size-1)/2)
y = x
grid[y][x] = 1
sum = 0
while sum < input:
    sum = 0
    if dir == 0:
        x += 1
        if grid[x][y-1] == 0:
            dir = (dir + 1) % 4
    elif dir == 1:
        y -= 1
        if grid[x-1][y] == 0:
            dir = (dir + 1) % 4
    elif dir == 2:
        x -= 1
        if grid[x][y+1] == 0:
            dir = (dir + 1) % 4
    elif dir == 3:
        y += 1
        if grid[x+1][y] == 0:
            dir = (dir + 1) % 4
    for i in range(-1,2):
        for j in range(-1,2):
            sum += grid[x+i][y+j]
    grid[x][y]=sum

for r in grid:
    print(r)

print(sum)