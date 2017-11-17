import networkx as nx
import random

class Patch:
    def __init__(self, greeness=0.5, r=0.2, k=0.8):
        self.greeness = greeness
        self.r = r
        self.k = k

    def update_greeness(self, neighbors):
        g = [p.greeness for p in neighbors]
        G = sum(g) / len(g)
        deltaG = G * self.greeness * (1 - self.greeness / self.k)
        self.greeness += deltaG

    def __repr__(self):
        return u"%0.2f" % self.greeness

class Universe:

    def __init__(self, width=20, height=20):
        self.height = width
        self.width = height

        self.grid = [[Patch() for i in range(width)]
                     for j in range(height)]

        self.g = nx.Graph()
        self.connect_moore()

    def connect_moore(self):
        """ creates edges in network, connecting Moore neighborhood """
        for x in range(self.width):
            for y in range(self.height):
                patch = self.grid[x][y]
                # connect to neighborhood
                for i in [x-1, x, x+1 if x+1 < self.width else -1]:
                    for j in [y-1, y, y+1 if y+1 < self.height else -1]:
                        self.g.add_edge(patch, self.grid[i][j])

        # remove self loops from graph
        self.g.remove_edges_from(self.g.selfloop_edges())

    def randomize_greeness(self):
        for p in self.g.nodes():
            p.greeness = random.random()
