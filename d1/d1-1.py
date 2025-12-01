cur = 50
zerocount = 0

for line in open("input"):
    direct = {'L': -1, 'R': 1}[line[0]]
    num = int(line[1:])

    cur = (cur + direct*num)%100
    if cur == 0: zerocount += 1

print("Final number: "+str(zerocount))
