import networkx as nx
import numpy

def swap(e) :
   ron=e[0]
   her=e[1]
   pop=(her,ron)
   return pop

def graph_betweenessE(G):
	'''This program returns the average betwenness of the given graph.'''
	b=nx.edge_betweenness_centrality(G)
	l=b.values()
	return l

def graph_betweenessV(G):
	'''This program returns the average betwenness of the given graph.'''
	b=nx.betweenness_centrality(G)
	l=b.values()
	return l

def bet_tree(G,T,l):
	bet=0
	for e in T.edges():
                if (G.edges()).count(e) != 0 :
		   bet+=l[(G.edges()).index(e)]
                else:
                   
                   e=swap(e)
		  
                   bet+=l[(G.edges()).index(e)]
	a=numpy.average(bet)
	return a			

'''def the_greedy(G,s,d,T,count):
	        returns length of longest greedy path between s and d
		#if s!=d:
		list=G.adjacency_list()
		while s!=d:
			
			gp=[]	
			#print (G.nodes()).index(s)
			#print list[(G.nodes()).index(s)]
			adj=list[(G.nodes()).index(s)]
			#print adj
		
			for vert in adj:
				gp.append(nx.shortest_path_length(T,vert,d))
			s=adj[gp.index(min(gp))]
			
			count+=1
			
			
	
		return count'''

def the_greedy(G,s,d,T,count):

    list=G.adjacency_list()
    dist=[]
    minlist=[]
    if s!=d:
       adjlist=list[(G.nodes()).index(s)]
       for dumbledore in adjlist:
             dist.append(nx.shortest_path_length(T,dumbledore,d))
       MIN=min(dist)
       for ginny in range(len(dist)):
            if dist[ginny]==MIN:
               minlist.append(adjlist[ginny])
       count=count+1  
       val=[]
       for hermione in minlist:
             val.append(the_greedy(G,hermione,d,T,count))
       count=max(val)
       
    return count
         
def graph_points(vv,a):
	zz=[]
	x=[]
	y=[]
	for i in range(len(vv)):
		  zz.append([])
		  zz[i].append(vv[i])
		  zz[i].append(a[i])
	zz.sort()    
	for i in zz:
		 x.append(i[0])
		 y.append(i[1])
	return x,y

def the_carcass(g, T):
	
	        '''Returns the carcass wrt T, REF: paper name'''
		max=0
		for s in g.nodes():
		  	for d in g.nodes():	
				bb=the_greedy(g,s,d,T,0)-nx.shortest_path_length(g,s,d)
				if bb>max:
					max=bb
		return max
		
def und(t):
	tree=nx.Graph()
	for e in t.edges():
		tree.add_edge(e[0],e[1])
	

	return tree	
	


def spanning_tree(G,v):
	'''Returns the BFS spanning tree starting from v in the graph G'''
	return nx.traversal.bfs_tree(G,v)
	
