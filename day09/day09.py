with open('input.txt') as f:
    content = f.readlines()
for line in content:
    depth = 0
    score = 0
    gar = False
    bang = False
    for c in line:
        if bang == True:
            bang = False
            continue
        if c == '!':
            bang = True
            continue
        if c == '<':
            gar = True
            continue
        if c == '>':
            gar = False
            continue

        if gar == False:
            if c == '{':
                depth += 1
            elif c == '}':
                score += depth
                depth -= 1
    print(score)