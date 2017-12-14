from functools import reduce

def knot(line):
    ln = 256
    if len(line) == 1:
        parts = []
    else:
        parts = [ord(x) for x in line.split('\n')[0]]
    parts.extend([17,31,73,47,23])
    #print(parts)
    p = 0
    s = 0
    l = list(range(ln))
    for _ in range(64):
        for x in parts:
            temp = l + l
            r = temp[p:p+x]
            r.reverse()
            for i in range(x):
                l[(p+i)%ln] = r[i]
            p = (p + x + s)% ln
            s += 1

    dh = []

    for i in range(16):
        dh.append(reduce(lambda k, j: k ^ j, l[i*16:(i+1)*16]))
    out = ''
    #day14.pyprint(dh)
    for x in dh:
        out += '{0:02x}'.format(x)
    return(out)

input = 'ugkiagan'
size = 128
grid = []
sum = 0
for i in range(size):
    p = input + '-' + str(i)
    hash = knot(p)
    b = bin(int(hash,16))[2:]
    grid.append(b)
    for c in b:
        if c == '1':
            sum += 1

print(sum)









