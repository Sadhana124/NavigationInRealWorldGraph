import pdb
import networkx as nx
import matplotlib.pyplot as plt
#pdb.set_trace()
numvert=500
#g=nx.erdos_renyi_graph(numvert,0.1)
g=nx.barabasi_albert_graph(numvert,2)
nx.draw(g)
plt.show()
t=nx.Graph()
l1=g.degree()
xx=[]
for x in range(0,len(l1)):
	xx.append(l1[x])
# xx contains the degrees of vertices !!!
m=max(xx)
root=-1
root=xx.index(m)
#for i in range(0,numvert):
	
#	if g.degree(i) == m:
#		root=i
list=g.adjacency_list()
#print list
ne=list[root]
for e in ne:
	t.add_edge(root,e)
nx.draw(t)
plt.show()

def choosemax(bubu):
        deg=[]
  	for e in bubu:
		deg.append(g.degree(e))
		
	pos=deg.index(max(deg))
        
        #print bubu
	#print pos
        return pos

check=1
old=len(t.nodes())
copy=[]
ver=[]
prevne=ne
prevroot=root
while len(t.nodes())<len(g.nodes()):
	pos=-1		
        
        if check!=0:
	  print "hi",ne 
	  pos=choosemax(ne)
	  root=ne[pos]
          #print root
	  ne=list[root]

	else:
	  print "hi1",copy
	  pos=choosemax(copy)
	  root=copy[pos]
	  #print root
	  ne=list[root]

	for e in ne:
		flag=0
                #print e,"jubu"
		for v in t.nodes():
			if e==v:
			    flag=1
			
		if flag==0:
			#print e,"abu catapi"
			t.add_edge(root,e)
	check=len(t.nodes())-old
	if check==0:
		if len(prevne) !=0:
			prevne.remove(root)
		if len(prevne)!=0:
	        	copy=prevne
		
		
	else:
		prevroot=root
		if len(ne)!=0:
			prevne=ne
                #print root,"&&& ",ne
	old=len(t.nodes())	
nx.draw(t)
plt.show()
print len(t.nodes())
