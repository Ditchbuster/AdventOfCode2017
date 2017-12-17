with open('input.txt') as f:
    content = f.readlines()
count = 0
for line in content:
    parts = [int(x) for x in line.split()]
    s = parts[0]
    buf = [0,1]
    p = 1
    for i in range(2,2018):
        p = (p+s)%len(buf)+1
        buf.insert(p,i)
        print(i,buf[:2])
    print(buf[buf.index(2017)+1])