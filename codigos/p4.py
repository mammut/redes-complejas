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
p2.vs["label"] = ["B: " + str(betweenness[i]) + "\nPR: " + str(pageranks[i]) + "\nInD: " + str(indegree[i]) + "\n" + names[i] for i in range(8)]
p2.es["width"] = 1
p2.vs["color"] = "lightblue"
p2.vs["size"] = 80
print sorted([(i, j) for i, j in enumerate(indegree)], key=lambda x: x[1], reverse=True)
print sorted([(i, j) for i, j in enumerate(betweenness)], key=lambda x: x[1], reverse=True)
print sorted([(i, j) for i, j in enumerate(pageranks)], key=lambda x: x[1], reverse=True)
G.plot(p2, "../img/p4-all.png", margin=50)

# plot indegree
p2.vs["label"] = ["InD: " + str(indegree[i]) + "\n" + names[i] for i in range(8)]
p2.vs['size'] = [500.0*i/sum(indegree) for i in indegree]
p2.vs["color"] = "green"
G.plot(p2, "../img/p4-indegree.png", margin=50)

# plot betweenness
p2.vs["label"] = ["B: " + str(betweenness[i]) + "\n" + names[i] for i in range(8)]
p2.vs['size'] = [500.0*i/sum(betweenness) for i in betweenness]
p2.vs["color"] = "yellow"
# G.plot(p2, "../img/p4-betweenness.png", margin=50)

# plot PageRank
p2.vs["label"] = ["PR: " + str(pageranks[i]) + "\n" + names[i] for i in range(8)]
p2.vs['size'] = [500.0*i/sum(pageranks) for i in pageranks]
p2.vs["color"] = "#C0C93F"
# G.plot(p2, "../img/p4-pageranks.png", margin=50)
