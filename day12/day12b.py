from collections import deque
with open('input.txt') as f:
    content = f.readlines()
count = 0
p = {}
for line in content:
    parts = [x for x in line.replace(',', '').split()]
    p[parts[0]] = []
    for c in parts[2:]:
        p[parts[0]].append(c)


q = deque()
q.append('0')
u = {'0'}
while len(q) != 0:
    pro = q.popleft()
    for c in p[pro]:
        if c not in u:
            q.append(c)
            u.add(c)
count = 1
left = p.keys() - u
while len(left) > 0:
    count += 1
    q = deque()
    f = left.pop()
    q.append(f)
    u = {f}
    while len(q) != 0:
        pro = q.popleft()
        for c in p[pro]:
            if c not in u:
                q.append(c)
                u.add(c)

    left = left - u
print(count)