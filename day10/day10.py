with open('input.txt') as f:
    content = f.readlines()
p = 0
s = 0
ln = 256
l = list(range(ln))
print(l)
for line in content:
    parts = [int(x) for x in line.split(',')]
    for x in parts:
        temp = l + l
        r = temp[p:p+x]
        r.reverse()
        for i in range(x):
            l[(p+i)%ln] = r[i]
        p = (p + x + s)% ln
        s += 1
print(l)
print(int(l[0])*int(l[1]))