#!/usr/bin/env python
# -*- coding: utf-8 -*-

import igraph as G
import random

g = G.GraphBase.Erdos_Renyi(400, 1)

deleted = 0
while G.mean(g.degree()) > 1:
    deleted += 1
    g.delete_edges(random.randint(0, g.ecount() - 1))

print "Removed", deleted, "edges"
