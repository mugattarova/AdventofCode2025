import operator as op
import functools as ft

inp = open('input').read().split('\n')
ops = inp.pop().split()
work = [list(z) for z in zip(*[list(l) for l in inp])]

vertwork = []
temp = []
for col in work:
    if all([x==' ' for x in col]):
        vertwork.append([*map(int, temp)])
        temp = []
    else: 
        temp.append(''.join(col))
vertwork.append([*map(int, temp)])
print(sum(ft.reduce(lambda x,y: {'+': op.add, '*': op.mul}.get(ops[i])(x, y), vertwork[i]) for i in range(len(vertwork))))
