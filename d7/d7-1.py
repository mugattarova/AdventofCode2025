inp = [list(line) for line in open('input').read().split('\n')]

beams = set([inp.pop(0).index('S')])
splits = 0
for line in inp:
    cpy = beams.copy()
    for beam in cpy:
        if line[beam] != '^':
            continue
        beams.remove(beam)
        beams.add(beam-1, beam+1)
        splits+=1

print(splits)
