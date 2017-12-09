with open('input.txt') as f:
    content = f.readlines()
for line in content:
    depth = 0
    score = 0
    garCount = 0
    gar = False
    bang = False
    for c in line:
        if bang == True:
            bang = False
            continue
        if c == '!':
            bang = True
            continue
        if c == '<' and gar == False:
            gar = True
            continue
        if c == '>' and gar == True:
            gar = False
            continue

        if gar == False:
            if c == '{':
                depth += 1
            elif c == '}':
                score += depth
                depth -= 1
        else:
            garCount += 1
    print(score,garCount)