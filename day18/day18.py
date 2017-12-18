with open('input.txt') as f:
    content = f.readlines()
cmds = []
reg = {}
for line in content:
    parts = [x for x in line.split()]
    cmds.append(parts)
    if parts[1] not in reg:
        reg[parts[1]] = 0
    if len(parts) > 2 and parts[2].isalpha() and parts[2] not in reg:
        reg[parts[1]] = 0
snd = 0
pos = 0
while pos < len(cmds):
    cmd = cmds[pos]
    if cmd[1].isalpha():
        x = reg[cmd[1]]
    else:
        x = int(cmd[1])
    if len(cmd) == 3:
        if cmd[2].isalpha():
            y = reg[cmd[2]]
        else:
            y = int(cmd[2])

    if cmd[0] == 'snd':
        snd = x
    elif cmd[0] == 'set':
        reg[cmd[1]] = y
    elif cmd[0] == 'add':
        reg[cmd[1]] += y
    elif cmd[0] == 'mul':
        reg[cmd[1]] = x * y
    elif cmd[0] == 'mod':
        reg[cmd[1]] = x % y
    elif cmd[0] == 'rcv':
        if x != 0:
            print(snd)
            break
    elif cmd[0] == 'jgz':
        if x > 0:
            pos += y-1

    pos += 1