#!/usr/bin/env python
# -*- coding: utf-8 -*-

import igraph as G
import numpy as np

# Build the graph
p2 = G.Graph([(0,1),(0,2),(1,2),(2,3),(3,4),(3,5),(4,5)])

laplacian_matrix = p2.laplacian()
w, v             = np.linalg.eig(p2.laplacian()) # Eigen values (w) and eigen vectors (v)
fiedler_value    = sorted(w)[1] # Fiedler value is the second smallest eigenvalues
fiedler_vector   = v[:, np.where(w == fiedler_value)[0]].T[0] # grab the n-th column of the eigenvectors, where n is the index of the Fiedler Value

print "Matriz Laplaciana:"
print np.array(laplacian_matrix)

print "Valores Propios", [round(x, 3) for x in sorted(w)]
print "Valor de Fiedler:", round(fiedler_value,4)
print "Vector de Fiedler:", [round(i, 3) for i in fiedler_vector]

# Plot the graph
p2.vs["label"] = [str(j) + "\n" + str(round(i, 3)) for  j, i in enumerate(fiedler_vector)]
p2.vs["color"] = ["lightblue" if x <= 0 else "green" for x in fiedler_vector]
G.plot(p2, layout=p2.layout("kk"), vertex_size=50, bbox=(600,600), margin=40)
