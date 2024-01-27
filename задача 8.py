v=int(input())
x=[12,3,35,524,364]
g=x.index(v)
print(g)
x.remove(x[g])
print(x)