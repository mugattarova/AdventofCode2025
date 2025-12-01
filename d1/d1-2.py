import math as m

divnum = 100
cur = 50
newcur = cur
zerocount = 0

for line in open("input"):

    direct = {'L': -1, 'R': 1}[line[0]]
    num = int(line[1:])

    zerocount += num//divnum
    num %= divnum

    newcur = (cur + direct*num)%(divnum)
    if cur != 0 and newcur != 0 and m.copysign(1, cur-newcur) == direct:
        zerocount += 1

    if newcur == 0: zerocount += 1
    cur = newcur
    
print("\nFinal number: "+str(zerocount))
