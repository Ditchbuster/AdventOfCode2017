with open('input.txt') as f:
    content = f.readlines()
csum = 0
for line in content:
    parts = [int(x) for x in line.split()]
    csum += max(parts) - min(parts)
print(csum)