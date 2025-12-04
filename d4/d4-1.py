import itertools as it

grid = list(list(line.strip()) for line in open('input'))
rows, cols = len(grid), len(grid[0])

valids = 0
for y in range(rows):
    for x in range(cols):
        neighbors = 0
        if grid[y][x] != '@': continue
        for i, j in it.product((-1, 0, 1), (-1, 0, 1)):
            if i==0 and j==0: continue
            nx, ny = x+j, y+i
            if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == '@':
                neighbors += 1
        if neighbors < 4:
            valids += 1

print(valids)