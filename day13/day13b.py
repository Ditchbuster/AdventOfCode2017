with open('input.txt') as f:
    content = f.readlines()
wall = {}
scanner = {}
for line in content:
    parts = [int(x) for x in line.replace(':','').split()]
    wall[parts[0]] = parts[1]
    scanner[parts[0]] = [1,1] # pos, dir


delay = 1
trig = 100
while True:
    if delay == trig:
        print(delay)
        trig = trig * 10
    for w,d in wall.items():
        if 0 == (delay+w)%((d-1)*2):
            delay += 1
            break
    else:
        print(delay)
        break
