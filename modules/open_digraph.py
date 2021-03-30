#Oussama Konate, Thomas Delépine, groupe 8
import random
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

  def indegree(self): #retourne le degré entrant d'un noeud
    return len(self.get_parents_ids())

  def outdegree(self): #retourne le degré sortant d'un noeud
    return len(self.get_children_ids())

  def degree(self): #retourne le degré d'un noeud (entrant + sortant)
    return len(self.get_parents_ids())+len(self.get_children_ids())
    
  def increment(self,n): #auxilliaire de shift_indices
    for i in range(len(self.children)):
      self.children[i] += n
    for j in range(len(self.parents)):
      self.parents[j] += n
    self.id += n

  def inverse(self):
    res = self.copy()
    res.parents, res.children = res.children, res.parents
    return res

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
    #if(not self.is_well_formed()):
      #raise NameError('the graph isn\'t well formed')

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
    if (liste[len(liste)-1] == len(liste)-1):
      return len(liste)
    return next(x for x, y in enumerate(liste, 1) if x != y)

  def add_edge(self, src, tgt): #ajoute une arête du noeud d’id src au noeud d’id tgt /!\ ERREUR ENONCÉ
    self.get_node_by_id(src).add_child_id(tgt) #bisect.insort(self.get_node_by_id(src).children,get_id(tgt)) #self.get_node_by_id(src).add_child_id(tgt)
    self.get_node_by_id(tgt).add_parent_id(src) #bisect.insort(self.get_node_by_id(tgt).parents,get_id(src))

  def add_edges(self, src, list_tgt): #ajoute des arêtes du noeud d’id src aux noeud d’id de la listtgt
    for tgt in list_tgt:
      self.get_node_by_id(src).add_child_id(tgt) #bisect.insort(self.get_node_by_id(src).children,get_id(tgt))
      self.get_node_by_id(tgt).add_parent_id(src)#bisect.insort(self.get_node_by_id(tgt).parents,get_id(src))

  def add_node(self, label, parents,children):#ajoute un noeud (avec label) au graphe avec un nouvel id
    newid = self.new_id()
    self.nodes[newid] = node(newid, label, [], [])
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

  def adjacency_matrix(self): #graph supposé normalisé
    nodeList = self.get_nodes()
    n = len(nodeList)
    adjMatrix = [[0 for i in range(n)] for j in range(n)]
    for node in nodeList:
      for childId in node.get_children_ids():
        adjMatrix[node.get_id()][childId] = adjMatrix[node.get_id()][childId] + 1
    return adjMatrix

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

  def is_cyclic(self): #test de cyclicité
    if(self.get_nodes() == []):
        return False
    else:
      flag = False
      for node in self.get_nodes():
        if(node.outdegree() == 0):
          flag = True
          g = self.copy()
          g.remove_node_by_id(node.get_id())
          break
      if(flag):
        return g.is_cyclic()
      else:
        return True

  def min_id(self): #retourne l'id min du graphe
    return min(self.get_node_ids())

  def max_id(self): #retourne l'id max du graphe
    return max(self.get_node_ids())

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
  
  def inverse(self):
    res = self.copy()
    for id in res.get_node_ids():
      res.nodes[id] = res.nodes[id].inverse()
    res.inputs, res.outputs = res.outputs, res.inputs
    return res

  def DFS(self,node): 
    res = [False for i in range(len(self.get_nodes()))]

    def aux(node): #auxilliaire
      if(not res[node.get_id()]):
        res[node.get_id()] = True
        for child in node.children:
          aux(self.nodes[child])

    aux(node)
    return res
    


  def connected_components(self): #renvoie le nombre de composantes connexes, et un dictionnaire qui associe `a chaque id de noeuds du graphe un int qui correspond `a une composante connexe
    dict = {}
    for i in self.get_node_ids():
      dict[i] = 0
    nbcc = 0
    #g = self.inverse()
    for i in self.get_node_ids():
      if(dict.get(i)==0):
        tab1 = self.DFS(self.get_node_by_id(i))
        print(tab1)
        #tab2 = g.DFS(g.get_node_by_id(i))
        #print(tab2)
        for j in self.get_node_ids():
          if(tab1[j]): #if(tab1[j] and tab2[j]):
            dict[j] = nbcc
        nbcc+=1
    return dict










