#Oussama Konate, Thomas Delépine, groupe 8
import bisect  #module pour insérer element dans liste triée

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

  def copy(self): #renvoie la copie d'un noeud
    #inputs : node
    #output : copy of the node
    return node(self.id, self.label, 
           self.parents.copy(), self.children.copy())

  #getters
  def get_id(self): #renvoie l'ID d'un noeud (Int)
    return self.id

  def get_label(self): #renvoie le label d'un noeud (String)
    return self.label

  def get_parents_ids(self): #renvoie la liste des ID des parents (int list)
    return self.parents
  
  def get_children_ids(self): #renvoie la liste des ID des enfants (int list)
    return self.children
  
  #getters fin
  #///////////////////////////
  #setters

  def set_id(self, id):
    self.id = id

  def set_label(self, label):
    self.label = label

  def set_parent_ids(self, parent_ids):
    self.parents = parent_ids
  
  def set_children_ids(self, children_ids):
    self.children = children_ids
  
  def add_child_id(self, id):
    bisect.insort(self.children,id)

  def add_parent_id(self, id):
    bisect.insort(self.parents,id)
  #setters fin

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
      return open_digraph(self.inputs,self.outputs,[node.copy() for node in self.nodes.values()])

  #getters
  def get_input_ids(self): #return la liste des ID des noeuds d'entrée (int list)
    return self.inputs

  def get_output_ids(self): #return la liste des ID des noeuds de sortie (int list)
    return self.outputs

  def get_id_node_map(self): #return un dictionnaire donc les clés sont les ID, et les valeurs les noeuds
    return self.nodes        #({int:node})
  
  def get_nodes(self): #return l'ensemble des noeuds d'un graph (node list)
    return [node for node in self.nodes.values()]

  def get_node_ids(self):#return la liste des ID des noeuds du graph (int list)
    return [id for id in self.nodes.keys()]

  def get_node_by_id(self, id):#input : ID (int)
    return self.nodes.get(id)
  
  def get_nodes_by_ids(self, listid): #input : liste d'ID (int list)
                                      #return la liste des noeuds dont l'ID est donné en Input (node List)
    return [self.nodes.get(id) for id in listid]
  #getters fin
  #/////////////////////
  #setters

  def set_input_ids(self, ids): #@param : entiers représentant les ID (int list)
    self.inputs = ids 

  def set_output_ids(self, ids): #@param : entiers représentant les ID (int list)
    self.outputs = ids

  def add_input_id(self, id): #@param:  entier étant l'ID à ajouter (int)
    self.inputs.append(id)

  def add_output_id(self, id): #@param:  entier étant l'ID à ajouter (int)
    self.outputs.append(id)
  #setters fin
  #/////////////////////
  def new_id(self): #renvoie un id non utilisé dans le graphe.(choisit le + petit)
    liste = get_node_ids(self)
    liste.sort()
    result = next(x for x, y in enumerate(liste, 1) if x != y)
    return result

  def add_edge(self, src, tgt): #ajoute une arête du noeud d’id src au noeud d’id tgt /!\ ERREUR ENONCÉ
    src.add_child_id(tgt)#bisect.insort(self.get_node_by_id(src).children,get_id(tgt))
    tgt.add_parent_id(src)#bisect.insort(self.get_node_by_id(tgt).parents,get_id(src)) 

  def add_edges(self, src, list_tgt): #ajoute des arêtes du noeud d’id src aux noeud d’id de la listtgt
    for tgt in list_tgt:
      src.add_child_id(tgt) #bisect.insort(self.get_node_by_id(src).children,get_id(tgt))
      tgt.add_parent_id(src)#bisect.insort(self.get_node_by_id(tgt).parents,get_id(src))

  def add_node(self, label, parents,children):
    newid = self.new_id()
    self.nodes[newid] = node(a, label, parents.copy(), children.copy())
    self.nodes[newid].add_edges(parents,children)
    return newid











  