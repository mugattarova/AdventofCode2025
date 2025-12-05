ranges, _ = open('input').read().split('\n\n')
ranges = [[*map(int, r.split('-'))] for r in ranges.split()]

fresh = []
for lower, upper in ranges:
    found = False
    for i in range(len(fresh)):
        low, up = fresh[i]
        if upper<low or lower>up:
            continue
        found=True
        fresh[i] = [min(lower, low), max(upper, up)]
    if not found:
        fresh.append([lower, upper])

while True:
    found = False
    newfresh = fresh.copy()
    torem = set()
    for lower, upper in fresh:
        for i in range(len(fresh)):
            low, up = fresh[i]
            if upper<low or lower>up or (lower==low and upper==up):
                continue
            found=True
            newfresh[i] = [min(lower, low), max(upper, up)]
            if [lower, upper] in newfresh: 
                torem.add((lower, upper))
    for t in torem:
        if [*t] in newfresh: newfresh.remove([*t])
    fresh = newfresh.copy()
    if not found: break

print(sum(x[1]-x[0]+1 for x in set((x[0], x[1]) for x in fresh)))