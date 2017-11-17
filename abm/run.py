from model import Universe
from pprint import pprint

u = Universe(width=5, height=3)
v = Universe(width=5, height=3)
u.randomize_greeness()
pprint( u.grid)
for t in range(4):
    v.g = u.g.copy()
    for p in v.g.nodes():
        p.update_greeness(u.g.neighbors(p))
    u.g = v.g.copy()

    pprint( u.grid)
