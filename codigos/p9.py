#!/usr/bin/env python
# -*- coding: utf-8 -*-

import igraph as G
import numpy as np
import matplotlib.pyplot as plt

# Build the graph
g = G.read("../archivos/pescado.net",format="pajek")

m = g.ecount() # Arcos
n = g.vcount() # Nodos
a = g.get_adjacency()._get_data()

rho_ = 0
a_   = 0
for i in range(len(a)):
    for j in range(len(a)):
        if i == j: continue
        rho_ += a[i][j]*a[j][i]
        a_   += a[i][j]

a_ = a_ / float(n*(n-1))
rho_ = rho_ / float(m)

print "Rho =", round(  ( rho_ - a_ )/ ( 1 - a_ )  , 4)

# Parte 2
s = np.matrix(g.get_adjacency(attribute="weight")._get_data())
s_in = np.squeeze(np.asarray(s.sum(axis=0, dtype=float)))
s_out = np.squeeze(np.asarray(s.sum(axis=1, dtype=float).T))

n, bins, c = plt.hist(s_in, bins=4)
plt.savefig('../img/p9-s-in.png')
plt.close()
n, bins, c = plt.hist(s_out, bins=9)
plt.savefig('../img/p9-s-out.png')


plt.close()
x = range(len(s_out))
plt.plot(s_in, s_out, '.')
plt.savefig('../img/p9-s-s.png')
plt.close()

# d.
g_undirected = g.as_undirected(mode="collapse", combine_edges=dict(weight=sum))

plt.hist(g_undirected.degree())
plt.savefig('../img/p9-k.png')
plt.close()

s_data = np.matrix(g_undirected.get_adjacency(attribute="weight")._get_data())
s = np.squeeze(np.asarray(s_data.sum(axis=0, dtype=float)))
plt.hist(s)
plt.savefig('../img/p9-s.png')
plt.close()


plt.plot(s, g_undirected.degree(), '.')
plt.savefig('../img/p9-k-vs-s.png')
print g_undirected.degree()
