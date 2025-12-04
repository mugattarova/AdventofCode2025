batteries = []
for line in open('input'):
    line = list(line)
    out = ''
    mx, mxind = 0, 0
    for i in range(len(line)-11,len(line)+1):
        mx = max(line[mxind : i])
        mxind = line.index(mx, mxind) + 1
        out += mx
    batteries.append(int(out))
    
print("Answer: "+str(sum(batteries)))