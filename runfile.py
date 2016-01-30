import networkx as nx
import sudlibn
import matplotlib.pyplot as plt
import pdb

#pdb.set_trace()
#g=nx.barabasi_albert_graph(40,10)
g=nx.grid_2d_graph(7,7)
#print g.edges()
#g=nx.hypercube_graph(3)
a=[]
r=[]
vv=[]
#print a
l=sudlibn.graph_betweenessE(g)
#print l
for v in g.nodes():
	t=sudlibn.spanning_tree(g,v)
	tree=sudlibn.und(t)
	r.append(sudlibn.the_carcass(g,tree))
	a.append(sudlibn.bet_tree(g,tree,l))
	
	#print "Vertex",v,":",r[(g.nodes()).index(v)]

	
print min(r),"Vertex",r.index(min(r))
print max(a),"Vertex",a.index(max(a))
'''Baboo=nx.Graph()
Baboo.add_edge((0,0,0),(1,0,0))
Baboo.add_edge((1,0,0),(1,1,0))
Baboo.add_edge((1,1,0),(0,1,0))
Baboo.add_edge((0,1,0),(0,1,1))
Baboo.add_edge((0,1,1),(1,1,1))
Baboo.add_edge((1,1,1),(1,0,1))
Baboo.add_edge((1,0,1),(0,0,1))
nx.draw(Baboo)
plt.show()
rfin=sudlibn.the_carcass(g,Baboo)
print "please be right:",rfin'''



vv=sudlibn.graph_betweenessV(g)
x,y=sudlibn.graph_points(vv,a)
          
#print zz,'\n'
#print a,"helloooooooooooo"
plt.plot(x,y)
plt.show()
x,y=sudlibn.graph_points(vv,r)
plt.plot(x,y)
plt.show()
x,y=sudlibn.graph_points(a,r)
plt.plot(x,y)
plt.show()

#t=sudlibn.spanning_tree(g,a.index(max(a)))
#tt=sudlibn.und(t)
#nx.draw(tt)
#plt.show()
