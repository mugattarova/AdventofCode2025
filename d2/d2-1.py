inval_ids = set()
with open('input') as file:
    for line in file:
        pairs=line.split(',')

for pair in pairs:
    first, last = pair.split('-')

    dupl = first[0:len(first)//2]
    if len(first)%2 != 0:
        lower = 10**len(str(dupl))
    else:
        lower = int(dupl)
    upper = int(last[0:-(len(first)-len(dupl))])

    for i in range(lower, upper+1):
        checknum = int(2*i)
        if int(first) <= checknum and checknum <= int(last):
            inval_ids.add(checknum)

print("Answer: "+str(sum(inval_ids)))
