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
    return open_digraph(self.inputs.copy(), 
           self.outputs.copy(), self.nodes)

