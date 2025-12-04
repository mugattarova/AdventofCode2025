import itertools as it

def torem(x: int, y: int, neighbors=0) -> bool:
    if grid[y][x] != '@': return False
    for i, j in it.product((-1, 0, 1), (-1, 0, 1)):
        if i==0 and j==0: continue
        nx, ny = x+i, y+j
        if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == '@':
            neighbors += 1
    if neighbors < 4:
        return True
    return False
    
grid = list(list(line.strip()) for line in open('input'))
rows, cols = len(grid), len(grid[0])

rems = 0
while True:
    destruct = []
    for y in range(rows):
        for x in range(cols):
            if torem(x, y): 
                rems += 1
                destruct.append((x, y))
    for x, y in destruct:
        grid[y][x] = '.'
    rems += len(destruct)
    if len(destruct) == 0: break

print(rems/2)
