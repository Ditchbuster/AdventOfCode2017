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
print(len(u))
