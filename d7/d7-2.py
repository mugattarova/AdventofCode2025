inp = [list(line) for line in open('input').read().split('\n')]

beams = {inp.pop(0).index('S'): 1}
for line in inp:
    cpy = beams.copy()
    for beam in cpy.keys():
        if line[beam] != '^':
            continue
        count = beams[beam]
        for b in [beam-1, beam+1]:
            if b in beams:
                beams[b] += count
            else:
                beams[b] = count
        beams.pop(beam)

print(sum(beams.values()))
