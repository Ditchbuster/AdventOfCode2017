with open('input.txt') as f:
    content = f.readlines()
count = 0
for line in content:
    r = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    parts = [x for x in line.replace('\n', '').split(',')]
    seen = []
    for i in range(1000000000):
        s = ''.join(r)
        if s in seen:  # cycles are short; no runtime lost for comparing full list instead of s == seen[0]
            print(seen[1000000000 % i],i)
            break
        seen.append(s)
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

    #print(''.join(r))

