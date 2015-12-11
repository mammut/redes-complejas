#!/usr/bin/env python
# -*- coding: utf-8 -*-

import igraph as G

def p7(g):
    # bien pythonesco, tomar los k_cores generados por igraph, filtrar los positivos y armar
    # la lista de tuplas con (n, m)
    k_cores = [(x.vcount(), x.ecount()) for x in filter(lambda x: x.vcount() > 0, g.k_core())]

    for i, (n,m) in enumerate(k_cores):
        print str(i+1) + "-core\t" + "n: " + str(n) + "\tm: ", m

    print "Modularidad", g.community_fastgreedy().as_clustering().modularity
    print "Asortatividad", g.assortativity_degree()

g = G.Graph.Read_GML("../archivos/correos.gml")
p7(g)

# Reconectar la red
print "\nReconectando la red al azar, por favor espere un momento..."
g.rewire(g.ecount()*2)
p7(g)


