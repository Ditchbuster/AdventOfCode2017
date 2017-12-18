with open('input.txt') as f:
    content = f.readlines()
cmds = []
regA = {}
regB = {}
for line in content:
    parts = [x for x in line.split()]
    cmds.append(parts)
    if parts[1] not in regA:
        regA[parts[1]] = 0
        regB[parts[1]] = 0
    if len(parts) > 2 and parts[2].isalpha() and parts[2] not in regA:
        regA[parts[1]] = 0
        regB[parts[1]] = 0

regA['p'] = 0
regB['p'] = 1
mesA = []
mesB = []
posA = 0
posB = 0
revA = False
revB = False
count = 0
while True:
    if revA and revB:
        break
    if not revA and posA < len(cmds):
        cmd = cmds[posA]
        if cmd[1].isalpha():
            x = regA[cmd[1]]
        else:
            x = int(cmd[1])
        if len(cmd) == 3:
            if cmd[2].isalpha():
                y = regA[cmd[2]]
            else:
                y = int(cmd[2])

        if cmd[0] == 'snd':
            mesB.append(x)
            revB = False
        elif cmd[0] == 'set':
            regA[cmd[1]] = y
        elif cmd[0] == 'add':
            regA[cmd[1]] += y
        elif cmd[0] == 'mul':
            regA[cmd[1]] = x * y
        elif cmd[0] == 'mod':
            regA[cmd[1]] = x % y
        elif cmd[0] == 'rcv':
            if len(mesA) == 0:
                revA = True
                posA -= 1
            else:
                regA[cmd[1]] = mesA.pop(0)

        elif cmd[0] == 'jgz':
            if x > 0:
                posA += y-1

        posA += 1

    if not revB and posB < len(cmds):
        cmd = cmds[posB]
        if cmd[1].isalpha():
            x = regB[cmd[1]]
        else:
            x = int(cmd[1])
        if len(cmd) == 3:
            if cmd[2].isalpha():
                y = regB[cmd[2]]
            else:
                y = int(cmd[2])

        if cmd[0] == 'snd':
            mesA.append(x)
            revA = False
            count += 1
        elif cmd[0] == 'set':
            regB[cmd[1]] = y
        elif cmd[0] == 'add':
            regB[cmd[1]] += y
        elif cmd[0] == 'mul':
            regB[cmd[1]] = x * y
        elif cmd[0] == 'mod':
            regB[cmd[1]] = x % y
        elif cmd[0] == 'rcv':
            if len(mesB) == 0:
                revB = True
                posB -= 1
            else:
                regB[cmd[1]] = mesB.pop(0)

        elif cmd[0] == 'jgz':
            if x > 0:
                posB += y - 1

        posB += 1

print(count)