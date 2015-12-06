#!/usr/bin/env python
# -*- coding: utf-8 -*-

import igraph as G
import numpy as np

p1 = G.Graph([(0,1),(0,2),(1,3),(2,3),(2,4),(4,5),(4,6),(5,7),(6,7),(7,8),(7,9),(8,9)])
colors = ["lightblue", "green"]
p1.vs["color"] = [colors[i] for i in [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
p1.vs["label"] = range(1,11)
G.plot(p1, layout=p1.layout("kk"), bbox=(600,300))
