with open('input.txt') as f:
    content = f.readlines()
count = 0
for line in content:
    r = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    #r = ['a','b','c','d','e']
    parts = [x for x in line.replace('\n','').split(',')]
    for p in parts:
        if p[0] == 's':
            t = int(p[1:])
            r = r[-t:] + r[:-t]
        elif p[0] == 'x':
            x,y = [int(f) for f in p[1:].split('/')]
            temp = r[x]
            r[x] = r[y]
            r[y] = temp
        elif p[0] == 'p':
            x,y = [f for f in p[1:].split('/')]
            i = r.index(x)
            j = r.index(y)
            temp = r[i]
            r[i] = r[j]
            r[j] = temp

    print(''.join(r))
