import networkx as nx
import numpy

def graph_betweenness(G):
	'''This program returns the average betwenness of the given graph.
	Author: Sudarshan'''
	b=nx.betweenness_centrality(G)
	l=b.values()
	a=numpy.average(l)
	return a

def the_greedy(G,s,d,T,count):
	        '''returns length of longest greedy path between s and d'''
		if s!=d:
			list=G.adjacency_list()
			gp=[]	
		
			adj=list[(G.nodes()).index(s)]
		
			for vert in adj:
				gp.append(nx.shortest_path_length(T,vert,d))
			s=vert[gp.index(min(gp))]
			count+=1
			the_greedy(G,s,d,T,count)
			
		else:
			return count

def the_carcass(g, T):
	
	        		'''Returns the carcass wrt T, REF: paper name'''
				max=0
				#for s in g.nodes():
		  		#for d in g.nodes():	
				s=(1,1,1)
				d=(0,1,0)
				bb=the_greedy(g,s,d,T,0)-nx.shortest_path_length(g,s,d)
				if bb>max:
					max=bb
				return max		



def spanning_tree(G,v):
	'''Returns the BFS spanning tree starting from v in the graph G'''
	return nx.traversal.bfs_tree(G,v)
	
