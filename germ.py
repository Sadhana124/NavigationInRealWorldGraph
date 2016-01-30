import networkx as nx
import matplotlib.pyplot as plt
import sudlibn

def copy(l):
        newl=[]
        for a in l:
               newl.append(a)
        return newl

def noloop(T,e):
	v1,v2=*e
        

def maketree(g,T,ww,sortedgel):
	for e in sortedgel:
		if T.edges()<(n-1):
                        if noloop(T,e):
				T.add_edge(*e)

def fun(g,l):
	weight=[]
	for e in g.edges():
		g.remove_edge(*e)
		l1=nx.all_pairs_shortest_path_length(g)
		g.add_edge(*e)
		count=0	
		for v in g.nodes():
			for v1 in g.nodes():
				for v2 in g.nodes():
					if (l[v][v1]>l[v][v2] and l1[v][v1]<=l1[v][v2]) or (l[v][v1]<l[v][v2] and l1[v][v1]>=l1[v][v2]) or (l[v][v1]==l[v][v2] and l1[v][v1]!=l1[v][v2]):
						count+=1

		weight.append(count)
		
	return weight
#g=nx.grid_2d_graph(5,5)

g=nx.barabasi_albert_graph(50,6)

l=nx.all_pairs_shortest_path_length(g)
ww=fun(g,l)
ww,sortedgel=sudlibn.graph_points(ww,G.edges())
sortedgel.reverse()
#ww.sort()
x=[]
y=[]

for s in ww:
	y.append(ww.count(s))
	x.append(s)
plt.plot(x,y)
plt.show()
print ww

T=[]
n=len(G.nodes())


