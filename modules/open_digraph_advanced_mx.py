class open_digraph_advanced_mx:
  
  def inverse(self):
    res = self.copy()
    for id in res.get_node_ids():
      res.nodes[id] = res.nodes[id].inverse()
    res.inputs, res.outputs = res.outputs, res.inputs
    return res

  def DFS(self,node,see,act,dict,toSee): 
    dict[node] = act
    see[node] = True
    toSee.remove(node)
    for i in self.get_node_by_id(node).get_children_ids():
      if(not see[i]):
        self.DFS(i,see,act,dict,toSee)
    for i in self.get_node_by_id(node).get_parents_ids():
      if(not see[i]):
        self.DFS(i,see,act,dict,toSee)
    
  def connected_components(self): #renvoie le nombre de composantes connexes, et un dictionnaire qui associe `a chaque id de noeuds du graphe un int qui correspond `a une composante connexe
    dict = {}
    see = {}
    act = 0
    nbcc = 0
    toSee = self.get_node_ids().copy()
    for i in toSee:
      see[i] = False
    while(toSee != []):
      self.DFS(toSee[0],see,act,dict,toSee)
      act += 1
      nbcc += 1
    return dict

  def dijkstra(self,src,direction=None, tgt=None):
    Q = [src]
    dist = {src:0}
    prev = {}
    while Q != []:
      u = min(Q , key = lambda x : dist[x])
      Q.remove(u)
      if u == tgt:
        return dist, prev
      if(direction==-1):
        neighbours = self.get_node_by_id(u).get_parents_ids() 
      elif(direction== 1):
        neighbours = self.get_node_by_id(u).get_children_ids() 
      else:
        neighbours =  self.get_node_by_id(u).get_parents_ids()+self.get_node_by_id(u).get_children_ids() 
      for v in neighbours:
        if not v in dist.keys():
          Q.append(v)
        if (not v in dist.keys()) or (dist[v] > dist[u]+1):
          dist[v] = dist[u]+1
          prev[v] = u
    return dist,prev

  def shortest_path(self, u, v):
    if(u == v):
      return [u]
    dist, prev = self.dijkstra(u, tgt=v)
    node = prev[v]
    path = [v]
    while node != u:
      path = [node] + path
      node = prev[node] 
    return [u] + path

  def common_ancestors_dist(self, node1, node2):
    dist1, prev1, = self.dijkstra(node1, direction = -1)
    dist2, prev2, = self.dijkstra(node2, direction = -1)
    res = {}
    for ancestor in dist1.keys():
      if ancestor in dist2.keys():
        res[ancestor] = (dist1[ancestor], dist2[ancestor])
    return res

  def tri_topologique(self):#renvoie un tableau de tableaux d'id des noeuds
    g = self.copy()
    cpt = 0
    res = []
    while(g.get_nodes() != []):
      tmp = []
      for node in g.get_nodes():
        if(node.indegree() == 0):
          tmp.append(node.get_id())
      g.remove_node_by_ids(tmp)
      if tmp == []:
        raise NameError('ERROR : g is cyclic')
      res.append(tmp)
      cpt += 1
    return res

  def node_prof(self, node):#prend en paramètre un noeud et renvoie sa profondeur (int)
    tmp = self.tri_topologique()
    for i in range(len(tmp)):
      if node.get_id() in tmp[i]:
        return i
    raise NameError('ERROR : node not in graph')

  def graph_prof(self):
    return len(self.tri_topologique()) - 1
  
  def longest_path(self, u, v):
    if(u == v):
      return 0, [u]
    i = self.node_prof(self.nodes[u])
    n = self.graph_prof()
    dist = {u: 0}
    prev = {}
    tri_topologique = self.tri_topologique()
    lk = tri_topologique[i]
    for j in range(i+1, n+1):
      for w in tri_topologique[j]:
        tmp = -1
        biggestancestor = None
        for parent in self.nodes[w].get_parents_ids():
          if parent in dist.keys():
            if dist[parent]> tmp:
              tmp = dist[parent]
              biggestancestor = parent
        if tmp > -1:
          dist[w] = tmp + 1
          prev[w] = biggestancestor
        if w == v:
          break
    if v in dist.keys():
      res = dist[v]
      node = prev[v]
      path = [v]
      while node != u:
        path = [node] + path
        node = prev[node] 
      return dist[v], [u] + path
    else:
      raise NameError('ERROR : v not in dist.keys()')


