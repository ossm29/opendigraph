#Oussama Konate, Thomas Delépine, groupe 8
import operator

import sys
sys.path.append('../')
import random
import bisect  #module pour insérer element dans liste triée
from modules.utils import *

from modules.open_digraph_tools_mx import *
from modules.open_digraph_getters_setters_mx import *
from modules.open_digraph_advanced_mx import *
from modules.open_digraph_degree_mx import *
from modules.open_digraph_composition_mx import *


class node():

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

class open_digraph(open_digraph_tools_mx,open_digraph_getters_setters_mx,open_digraph_advanced_mx,open_digraph_degree_mx,open_digraph_composition_mx): # for open directed graph

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
      return open_digraph(self.inputs.copy(),self.outputs.copy(),[node.copy() for node in self.nodes.values()])

  def add_node(self, label='', parents=[],children=[]):#ajoute un noeud (avec label) au graphe avec un nouvel id
    newid = self.new_id()
    n0 = node(newid, label, [], [])
    self.nodes[newid] = n0
    for element in parents:
      self.add_edge(element,newid)
    self.add_edges(newid,children)
    return newid

  
  def new_id(self): #renvoie un id non utilisé dans le graphe.(choisit le + petit)
    liste = self.get_node_ids()
    if(len(liste)==0):
      return 0
    liste.sort()
    if (liste[len(liste)-1] == len(liste)-1):
      return len(liste)
    tmp = 0
    for i in liste:
      if i == tmp:
        tmp += 1
      else:
        return tmp

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

  def is_cyclic(self): #test de cyclicité
    if(self.get_nodes() == []):
        return False
    else:
      g = self.copy()
      flag = False
      for node in self.get_nodes():
        if(node.outdegree() == 0):
          flag = True
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


  def fusion(self, a, b):#a, b : deux id de noeuds à fusionner
    newid = a
    nodeA = self.get_node_by_id(a)
    nodeB = self.get_node_by_id(b)
    if nodeA.get_label() == nodeB.get_label():
      newlabel = nodeA.get_label()
    else:
      newlabel = ""
    self.nodes[a] = node(newid, newlabel, nodeA.parents + nodeB.parents, nodeA.children + nodeB.children)
    for i in range(len(self.nodes[a].children)):
      if(self.nodes[a].children[i] == b):
        self.nodes[a].children[i] = a
    for i in range(len(self.nodes[a].parents)):
      if(self.nodes[a].parents[i] == b):
        self.nodes[a].parents[i] = a

    for nodeID in self.nodes[b].parents:
      for i in range(len(self.nodes[nodeID].children)):
        if self.nodes[nodeID].children[i] == b:
          self.nodes[nodeID].children[i] = a
    for nodeID in self.nodes[b].children:
      for i in range(len(self.nodes[nodeID].parents)):
        if self.nodes[nodeID].parents[i] == b:
          self.nodes[nodeID].parents[i] = a
    if(not a in self.inputs):
      for i in range(len(self.inputs)):
        if(self.inputs[i] == b):
          self.inputs[i] = a
    if(not a in self.outputs):
      for i in range(len(self.outputs)):
        if(self.outputs[i] == b):
          self.outputs[i] = a
    self.remove_node_by_id(b)







          




















