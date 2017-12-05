with open('input.txt') as f:
    content = f.readlines()
inst = []
for line in content:
    inst.append(int(line))
print(inst)
i=0
count = 0
while i >= 0 and i < len(inst):
    #print(i)
    oldI = i
    i = i+inst[i]
    if inst[oldI] >= 3:
        inst[oldI] -= 1
    else:
        inst[oldI] += 1

    count += 1

print(count)
