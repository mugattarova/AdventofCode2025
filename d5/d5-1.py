ranges, ids = open('test').read().split('\n\n')
ranges = [[*map(int, r.split('-'))] for r in ranges.split()]
ids = [*map(int, ids.split())]

print(sum(any(l<=num<=u for l, u in ranges) for num in ids))