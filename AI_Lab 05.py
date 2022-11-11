graph = {'0':['1','2'], '1':['3','4'],'2':['5','6'],'3':[],'4':[],'5':[],'6':[]} # graph
#printing a graph
def DFS(parent,destination,graph,depth):
    print("The path for this is:: ",parent) # Travesing of tree
    if parent==destination: # Checking whether it is reaching in 1st itteration to goal
        return True
    if depth<=0: # The limit setted was reached to its limit
        return False
    for childs in graph[parent]: # Traversing through childs of parents
        if DFS(childs,destination,graph,depth-1):
            return True
    return False
            # we will call the dfs function for th same functionallity
        # but the parent will be replaced by child node as we are exploring it and depth will become -1 
        # because we are traversing in depth.
def IterativeDeep(parent,destination,graph,depth): # For IDS we will create this
    for i in range(depth): # Travese depending on number of depths
        if DFS(parent,destination,graph,i): # i will traverse from i to maxdepth i.e.0,1.2.3...n
            return True
    return False
if not IterativeDeep('0','6',graph,4):
    print("No path found!! ")
else:
    print("We found a Path!! ")


#Task no: 01
graph = {
        'arad':['sibiu', 'zerind', 'timisoara'],
        'sibiu':['oradea', 'fagaras', 'rimnicu'],
        'zerind':['arad', 'oradea'],
        'timisoara':['arad', 'lugoj'],
        'oradea':['zerind', 'sibiu'],
        'fagaras':['sibiu', 'bucharest'],
        'lugoj':['timisoara', 'mehadia'],
        'mehadia':['lugoj', 'drobeta'],
        'drobeta':['mehadia', 'craiova'],
        'craiova':['drobeta', 'riminica','pitesti'],
        'riminica':['sibui', 'pitesti','craiova'],
        'pitesti':['riminica', 'craiova','bucharest'],
        'bucharest':['fagaras', 'pitesti','urziceni'],
        'urziceni':['bucharest', 'hirsova','vaslui'],
        'hirsova':['urziceni', 'eforie'],
        'vaslui':['isai', 'urzicini'],
        'eforie':['hirsova'],
        'isai':['neamt', 'vaslui'],
        'giurgui':['bucharest'],
        'neamt':['isai']
        }
def DFS(parent,destination,graph,depth):
    print("The path for this is:: ",parent) 
    if parent==destination: 
        return True
    if depth<=0:
        return False
    for childs in graph[parent]: 
        if DFS(childs,destination,graph,depth-1):
            return True
    return False
          
def IterativeDeep(parent,destination,graph,depth): 
    for i in range(depth): 
        if DFS(parent,destination,graph,i): 
            return True
    return False
if not IterativeDeep('arad','bucharest',graph,4):
    print("No path found!! ")
else:
    print("We found a Path!! ")
