#Oussama Konate, Thomas Delépine
class node:

  def __init__(self, identity, label, parents, children):
    '''
    identity: int; its unique id in the graph
    label: string;
    parents: int list; a sorted list containing the ids of its parents
    children: int list; a sorted list containing the ids of its children
    '''
    self.id = identity
    self.label = label
    self.parents = parents
    self.children = children

  def __str__(self):
    return ("(" + str(self.id) + ", " + self.label + ", "
    + str(self.parents) + ", " + str(self.children) + ")")

  def __repr__(self):
    return "node"+str(self)

  def copy(self):
    #inputs : node
    #output : copy of the node
    return node(self.id, self.label, 
           self.parents.copy(), self.children.copy())

  #getters
  def get_id(self):
    return self.id

  def get_label(self):
    return self.label

  def get_parents_ids(self):
    return self.parents
  
  def get_children_ids(self):
    return self.children
  
  #getters fin

class open_digraph: # for open directed graph

  def __init__(self, inputs, outputs, nodes):
    '''
    inputs: int list; the ids of the input nodes
    outputs: int list; the ids of the output nodes
    nodes: node list;
    '''
    self.inputs = inputs
    self.outputs = outputs
    self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict

  def __str__(self):
    return ("("+str(self.inputs)+", "+str(self.nodes)
                +", "+str(self.outputs)+")")

  def __repr__(self):
    return "graph : "+str(self)

  def empty():
    #inputs : /
    #outputs : an empty graph
    return open_digraph([], [], [])

  def copy(self):
    #inputs : open_digraph
    #outputs : copy of the open_digraph
    def copy(self):
        '''
        output : open_diagraph; retourne une copie du graphe

        '''
        return open_diagraph(self.inputs,self.outputs,[node.copy() for node in self.nodes.values()])

  #getters
  def get_input_ids(self):
    return self.inputs

  def get_output_ids(self):
    return self.outputs

  def get_id_node_map(self): #dico
    dico = {}
    for node in self.nodes:
      dico[node.id] = node 
    
    return dico
  
  def get_nodes(self):
    return self.nodes

  def get_nodes_ids(self):
    liste = []
    return (liste.append(node.id) for node in self.nodes)

  def get_node_by_id(self, id):
    for node in self.nodes:
      if(node.id == id):
        return node
        break
  
  def get_nodes_by_ids(self, listid):
    liste = []
    return (liste.append(get_node_by_id(id)) for node in listid)

  