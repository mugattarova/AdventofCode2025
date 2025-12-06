import operator as op
import functools as ft

inp = open('test').read().split('\n')
ops = inp.pop().split()
work = [list(z) for z in zip(*[[*map(int, l.split())] for l in inp])]

print(sum(ft.reduce(lambda x,y: {'+': op.add, '*': op.mul}.get(ops[i])(x, y), work[i]) for i in range(len(work))))
