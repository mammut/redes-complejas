#!/usr/bin/env python
# -*- coding: utf-8 -*-

import igraph as G
import numpy as np
import random as R
import matplotlib.pyplot as plt

def probability(choice):
    p=R.uniform(0,1)
    pp=1-p
    if(choice==1):
        #return(p,1-p)
        return(p,pp)
    if(choice==2):
        #return(1-p,p)
        return(pp,p)

#Repeticion del experimento
for j in range(10):
    #Grafo Erdos_Renyi
    g=G.Graph.Erdos_Renyi(80,0.2,directed=False)
    #Ahora dirigido
    g.to_directed(False)


    B_1=range(0,40)
    B_2=range(40,80)
    C_1=range(0,20) + range(40,60)
    C_2= range(20,40) + range(60,80)

    #Redirigir particiones
    edges=g.get_edgelist()
    for edge in edges:
        #(B_1,B_2)
        x=edge[0]
        y=edge[1]
        if( (x in B_1) and (y in B_2)):
            weights=probability(1)
            choice=np.random.choice(edge,1,p=weights)
            choice=int(choice[0])
            if(y==choice):
                g.delete_edges([(x,y)])
                g.add_edges([(y,x)])

        #(B_2,B_1)
        if( (y in B_1) and (x in B_2)):
            weights=probability(2)
            choice=np.random.choice(edge,1,p=weights)
            choice=int(choice[0])
            if(y==choice):
                g.delete_edges([(x,y)])
                g.add_edges([(y,x)])

    #Para p =(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)
    p =(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1)

    Mx_1=[[0,0,0,0,0,0,0,0,0,0,0]]
    Mx_2=[[0,0,0,0,0,0,0,0,0,0,0]]


    Curve_1=[]
    Curve_2=[]

    #Curve_1
    for i in p:
        edges=g.get_edgelist()
        for edge in edges:
            x=edge[0]
            y=edge[1]
            #(B_1,B_2)
            if((x in B_1) and (y in B_2)):
                weights=(i,1-i)
                choice=np.random.choice(edge,1,p=weights)
                choice=int(choice[0])
                if(y==choice):
                    g.delete_edges([(x,y)])
                    g.add_edges([(y,x)])
            #(B_2,B_1)
            if((y in B_1) and (x in B_2)):
                weights=(1-i,i)
                choice=np.random.choice(edge,1,p=weights)
                choice=int(choice[0])
                if(y==choice):
                    g.delete_edges([(x,y)])
                    g.add_edges([(y,x)])
        vertexDendrogram=g.community_edge_betweenness()
        Curve_1 += [float(vertexDendrogram.as_clustering().modularity)]
    Mx_1=np.r_[Mx_1,[Curve_1]]

    #Curve_2
    for i in p:
        edges=g.get_edgelist()
        for edge in edges:
            x=edge[0]
            y=edge[1]
            #(C_1,C_2)
            if((x in C_1) and (y in C_2)):
                weights=(i,1-i)
                choice=np.random.choice(edge,1,p=weights)
                choice=int(choice[0])
                if(y==choice):
                    g.delete_edges([(x,y)])
                    g.add_edges([(y,x)])
            #(C_2,C_1)
            if((y in C_1) and (x in C_2)):
                weights=(1-i,i)
                choice=np.random.choice(edge,1,p=weights)
                choice=int(choice[0])
                if(y==choice):
                    g.delete_edges([(x,y)])
                    g.add_edges([(y,x)])
        vertexDendrogram=g.community_edge_betweenness()
        Curve_2 += [float(vertexDendrogram.as_clustering().modularity)]
    Mx_2=np.r_[Mx_2,[Curve_2]]



Mx_1=Mx_1[1:]
Mx_2=Mx_2[1:]
#Promedio
Mx_1_avg=Mx_1.sum(axis=0)/11.
Mx_2_avg=Mx_2.sum(axis=0)/11.


plt.plot(Mx_1_avg)
plt.plot(Mx_2_avg)
plt.legend(['(B_1,B_2)', '(C_1,C_2)'], loc='upper left')
plt.show()
