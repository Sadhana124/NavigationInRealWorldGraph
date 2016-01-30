import networkx as nx
import matplotlib.pyplot as plt
import sudlibn

def copy(l):
        newl=[]
        for a in l:
               newl.append(a)
        return newl

        

def maketree(g,T,ww,sortedgel):
	for e in sortedgel:
		if len(T.edges())<(n-1):
                        try: 
                             nx.shortest_path_length(T,*e)
                        except:

                             T.add_edge(*e)
			    
			     
		else:
                      	break

	if(len(T.edges())!=n-1):
           print "Oh no of the no no !!!"

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

g=nx.barabasi_albert_graph(500,6)

l=nx.all_pairs_shortest_path_length(g)
ww=fun(g,l)
ww,sortedgel=sudlibn.graph_points(ww,g.edges())
sortedgel.reverse()
#ww.sort()
x=[]
y=[]

for s in ww:
	y.append(ww.count(s))
	x.append(s)
plt.plot(x,y)
plt.show()
#print ww
n=len(g.nodes())
T=nx.Graph()

maketree(g,T,ww,sortedgel)
nx.draw(T,nx.graphviz_layout(T,'neato'))
plt.show()
print "Weight method carcass"
r=sudlibn.the_carcass(g, T)
print r

'''r1=[]
for v in g.nodes():
	t=sudlibn.spanning_tree(g,v)
	tree=sudlibn.und(t)
	r1.append(sudlibn.the_carcass(g,tree))
	 
print "All BFS Trees"
print min(r1)'''
