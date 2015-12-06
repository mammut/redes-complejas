#!/usr/bin/env python
# -*- coding: utf-8 -*-

import igraph as G
import numpy as np

# Build the graph
p2 = G.Graph.Read_GML("../archivos/redchica.gml")
G.summary(p2)
# Plot the graph

betweenness = p2.betweenness()
pageranks   = [round(i, 3) for i in p2.pagerank()]
indegree    = p2.degree(mode="in")
names = p2.vs["label"]
p2.vs["label"] = ["B: " + str(betweenness[i]) + "\nPR: " + str(pageranks[i]) + "\nInD: " + str(indegree[i]) + "\n" + names[i] for i in range(7)]
p2.es["width"] = 1
p2.vs["color"] = "green"


print sorted([(i, j) for i, j in enumerate(indegree)], key=lambda x: x[1], reverse=True)
print sorted([(i, j) for i, j in enumerate(betweenness)], key=lambda x: x[1], reverse=True)
print sorted([(i, j) for i, j in enumerate(pageranks)], key=lambda x: x[1], reverse=True)

G.plot(p2, vertex_size=80, margin=80)

