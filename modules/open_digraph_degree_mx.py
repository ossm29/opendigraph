class open_digraph_degree_mx:
  def max_indegree(self): #retourne le degré entrant maximal du graphe
    return max([node.indegree() for node in self.get_nodes()])

  def max_outdegree(self): #retourne le degré sortant maximal du graphe
    return max([node.outdegree() for node in self.get_nodes()])
  
  def max_degree(self): #retourne le degré maximal du graphe
    return max([node.degree() for node in self.get_nodes()])

  def min_indegree(self):  #retourne le degré entrant minimal du graphe
    return min([node.indegree() for node in self.get_nodes()])

  def min_outdegree(self): #retourne le degré sortant minimal du graphe
    return min([node.outdegree() for node in self.get_nodes()])
  
  def min_degree(self): #retourne le degré  minimal du graphe
    return min([node.degree() for node in self.get_nodes()])