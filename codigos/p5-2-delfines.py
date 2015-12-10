#!/usr/bin/env python
# -*- coding: utf-8 -*-

import igraph as G
import random

def pickRandom(g):
    return random.randint(0, g.vcount() - 1)

def pickDegree(g):
    b = g.degree()
    return b.index(max(b))

def pickBetweenness(g):
    b = g.betweenness()
    return b.index(max(b))

g_safe  = G.Graph.Read_GML("../archivos/delfines.gml")
total   = g_safe.vcount()
half    = g_safe.components().giant().vcount()/2.0

for method in [pickRandom, pickDegree, pickBetweenness]:
    g = g_safe.copy()
    deleted = 0
    while g.components().giant().vcount() > half:
        deleted += 1
        g.delete_vertices(method(g))

    print method.__name__ + ": ", round(deleted*100.0/total, 3)

