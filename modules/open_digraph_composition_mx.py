class open_digraph_composition_mx:
  
  def shift_indices (self,n):
    dict = {}
    l = len(self.get_nodes())
    for i in range(1,l+1):
      node = self.get_nodes()[l-i]
      node.increment(n)
      #node.change_id(node.get_id(),node.get_id()+n)
    for i in range(l):
      node = self.get_nodes()[i]
      dict[node.get_id()] = node
    self.nodes = dict
    #incrément de input
    for i in range(len(self.get_input_ids())):
      self.get_input_ids()[i] += n
    #incrément de output
    for i in range(len(self.get_output_ids())):
      self.get_output_ids()[i] += n
  
  def iparallel(self,g): #ajoute g à self (modifie self)
    self.shift_indices(self.max_id()-g.min_id()+1)
    self.inputs += g.inputs
    self.outputs += g.outputs
    self.nodes = {**self.nodes, **g.nodes}
  
  def parallel(self,g): #ajoute g à self (sans modification)
    res = self.copy()
    res.iparallel(g)
    return res

  def icompose(self, g): #composition séquentielle de self et g (modifie self)
    #test
    if(len(self.get_input_ids()) != len(g.get_output_ids())):
      raise NameError('entrée et sortie incompatibles')
    g.shift_indices(self.max_id()-g.min_id()+1)
    self.nodes = {**self.nodes, **g.nodes}
    self.inputs = g.inputs
    for i in range(len(g.outputs)):
      self.add_edge(g.outputs[i],self.inputs[i])
  
  def compose(self,g): #composition séquentielle de self et g (sans modification)
    res = self.copy()
    res.icompose(g)
    return res