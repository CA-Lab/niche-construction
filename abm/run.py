from model import Universe
from pprint import pprint
import random

u = Universe(width=50, height=30)
v = Universe(width=50, height=30)
u.randomize_greeness(r=random.random(), k=random.random())
u.plot("t00.png")
for t in range(1,11):
    v.g = u.g.copy()
    for p in v.g.nodes():
        p.update_greeness(u.g.neighbors(p))
    u.g = v.g.copy()
    u.plot("t%02i.png" % t)
    #pprint( u.grid)
