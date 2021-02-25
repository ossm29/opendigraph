#Oussama Konate, Thomas Delépine, groupe 8
import bisect  #module pour insérer element dans liste triée
from modules.utils import *

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

  def __eq__(self,other):
    return ((self.get_id() == other.get_id()) and (self.get_label() == other.get_label()) and (self.get_children_ids() == other.get_children_ids()) 
    and (self.get_parents_ids() == other.get_parents_ids()))

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
  #removers
  def remove_parent_id(self, id):#supprime la première occurence de l'ID (int) donné en paramètre dans la liste des ID des parents
    if id in self.parents:
      self.parents.remove(id)

  def remove_child_id(self, id):#supprime la première occurence de l'ID (int) donné en paramètre dans la liste des ID des enfants
    if id in self.children:
      self.children.remove(id)

  def remove_parent_id_all(self, id):#supprime toutes les occurences de l'ID (int) donné en paramètre dans la liste des ID des parents
    self.parents = remove_all(self.parents, id)

  def remove_child_id_all(self, id):#supprime toutes les occurences de l'ID (int) donné en paramètre dans la liste des ID des enfants
    self.children = remove_all(self.children, id)


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

  def __eq__(self,other):
    return ((self.get_input_ids()== other.get_input_ids()) and (self.get_output_ids() == other.get_output_ids()) 
    and ( self.get_nodes() == other.get_nodes()))

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
    liste = self.get_node_ids()
    liste.sort()
    result = next(x for x, y in enumerate(liste, 1) if x != y)
    return result

  def add_edge(self, src, tgt): #ajoute une arête du noeud d’id src au noeud d’id tgt /!\ ERREUR ENONCÉ
    self.get_node_by_id(src).add_child_id(tgt) #bisect.insort(self.get_node_by_id(src).children,get_id(tgt)) #self.get_node_by_id(src).add_child_id(tgt)
    self.get_node_by_id(tgt).add_parent_id(src) #bisect.insort(self.get_node_by_id(tgt).parents,get_id(src))

  def add_edges(self, src, list_tgt): #ajoute des arêtes du noeud d’id src aux noeud d’id de la listtgt
    for tgt in list_tgt:
      self.get_node_by_id(src).add_child_id(tgt) #bisect.insort(self.get_node_by_id(src).children,get_id(tgt))
      self.get_node_by_id(tgt).add_parent_id(src)#bisect.insort(self.get_node_by_id(tgt).parents,get_id(src))

  def add_node(self, label, parents,children):#ajoute un noeud (avec label) au graphe avec un nouvel id
    newid = self.new_id()
    self.nodes[newid] = node(newid, label, parents.copy(), children.copy())
    for element in parents:
      self.add_edge(element,newid)
    self.add_edges(newid,children)
    return newid

  def remove_edge(self, src, tgt): #supprime une arête du noeud src au noeud tgt
    self.get_node_by_id(src).remove_child_id(tgt)
    self.get_node_by_id(tgt).remove_parent_id(src)
  
  def remove_node_by_id(self, id):#*
    x = self.nodes.pop(id)
    for element in self.get_node_ids():
      self.get_node_by_id(element).remove_parent_id_all(id)
      self.get_node_by_id(element).remove_child_id_all(id)
    while id in self.get_input_ids():
      self.get_input_ids().remove(id)
    while id in self.get_output_ids():
      self.get_output_ids().remove(id)

  
  def remove_edges(self, listsrctgt):#supprime une arêtes de chaque paire de noeuds (src,tgt) de la liste @param
    for index, tuple in enumerate(listsrctgt):
      self.remove_edge(tuple[0],tuple[1])
  
  def remove_node_by_ids(self,listid):#*
    for id in listid:
      self.remove_node_by_id(id)

  def is_well_formed(self):
    nodeListId = self.get_node_ids()
    nodeList = self.get_nodes()
    for e in self.inputs:
      if not e in nodeListId:
        return False
    for e in self.outputs:
      if not e in nodeListId:
        return False
    for e in nodeList:
      if self.nodes[e.id] != e:
        return False
    for node in nodeList:
      for e in node.parents:
        if e in nodeListId:
          if not count_occurence(node.parents, e) == count_occurence(self.nodes[e].children, node.id):
            return False
        else:
          return False
      for e in node.children:
        if e in nodeListId:
          if not count_occurence(node.children, e) == count_occurence(self.nodes[e].parents, node.id):
            return False
        else:
          return False
    return True

  def change_id(self, node_id, new_id):
    if new_id in self.get_node_ids():
      print("new node already in the graph")
    elif not node_id in self.get_node_ids():
      print("node_id not in the graph")
    else:
      cptInputs = 0
      while node_id in self.inputs:
        self.inputs.remove(node_id)
        cptInputs = cptInputs + 1
      for i in range(cptInputs):
        bisect.insort(self.inputs,new_id)
      cptOutputs = 0
      while node_id in self.outputs:
        self.outputs.remove(node_id)
        cptOutputs = cptOutputs + 1
      for i in range(cptOutputs):
        bisect.insort(self.outputs, new_id)
      newNode = self.nodes[node_id].copy()
      newNode.id = new_id
      for nodeParent in self.get_nodes_by_ids(newNode.parents):
        cptChildren = 0
        while node_id in nodeParent.children:
          nodeParent.children.remove(node_id)
          cptChildren = cptChildren + 1
        for i in range(cptChildren):
          bisect.insort(nodeParent.children, new_id)
      for nodeChildren in self.get_nodes_by_ids(newNode.children):
        cptParents = 0
        while node_id in nodeChildren.parents:
          nodeChildren.parents.remove(node_id)
          cptParents = cptParents + 1
        for i in range(cptParents):
          bisect.insort(nodeChildren.parents, new_id)
      while node_id in newNode.get_parents_ids():
        newNode.get_parents_ids().remove(node_id)
        bisect.insort(newNode.parents, new_id)
      while node_id in newNode.get_children_ids():
        newNode.get_children_ids().remove(node_id)
        bisect.insort(newNode.children, new_id)
      self.nodes.pop(node_id)
      self.nodes[new_id] = newNode

  def change_ids(self, l):
    l = sorted(l, key=lambda l: l[1])
    for i in l:
      self.change_id(i[0], i[1])

  def normalise_ids(self):
    cpt = 0
    for i in self.get_node_ids():
      if i != cpt:
        self.change_id(i, cpt)
      cpt = cpt + 1