import math

inval_ids = set()
with open('input') as file:
    for line in file:
        pairs = line.split(',')

for pair in pairs:
    first, last = pair.split('-')
    firstlen, lastlen = len(first), len(last)

    half = first[0:len(first)//2]
    if firstlen%2 != 0:
        lower = 10**len(str(half))
    else:
        lower = int(half)

    upper = int(last[0:-max(1, math.ceil(firstlen//2))])

    for i in range(lower, upper+1):
        baseiter = str(i)
        for j in range(len(baseiter)):
            dupl = baseiter[0:j+1]

            for k in range(2, lastlen+1):
                if len(dupl)*k < firstlen or len(dupl)*k > lastlen:
                    continue
                checknum = int(dupl*k)
                if int(first) <= checknum and checknum <= int(last):
                    inval_ids.add(checknum)

print("Answer: "+str(sum(inval_ids)))