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
    inst[oldI] += 1

    count += 1

print(count)
