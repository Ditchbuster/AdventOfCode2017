def state(parts):
    return ''.join(str(parts))

with open('input.txt') as f:
    content = f.readlines()
count = 0
for line in content:
    parts = [int(x) for x in line.split()]
    states = []
    curState = state(parts)
    count = 0
    while curState not in states:
        states.append(curState)
        blocks = max(parts)
        maxIndex = parts.index(blocks)
        parts[maxIndex] = 0
        for i in range(1,blocks+1):
            parts[(maxIndex+i)%len(parts)] += 1
        curState = state(parts)
        count += 1
    print(count)


