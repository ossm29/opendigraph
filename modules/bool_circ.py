#Oussama Konate et Thomas Delépine :)

from PIL import Image, ImageDraw
import math
from datetime import datetime
from modules.open_digraph import *
from modules.draw_graph import *
from modules.matrix import *

class bool_circ(open_digraph): #class représentant les circuits booléens
  def __init__(self, g):
    inp = g.inputs.copy()
    out = g.outputs.copy()
    ntab = [node.copy() for node in g.get_nodes()]
    super().__init__(inp, out , ntab)
    if(not self.is_well_formed()):
      raise NameError('g is not a well formed boolean circ')
    self.starters = {} #dict {int:str} un id, un nom de variables

  def __eq__(self,other):
    return ((self.get_input_ids() == other.get_input_ids()) and (self.get_output_ids() == other.get_output_ids()) 
    and ( self.get_nodes() == other.get_nodes()))

  def __str__(self):
    return ("("+str(self.inputs)+", "+str(self.nodes)
                +", "+str(self.outputs)+")")

  def __repr__(self):
    return "boolean_circ"+str(self)
  
  def copy_bool_circ(self):
    return bool_circ(self.copy())
  
  def convert(self): #transforme un circuit booléen en graph simple
    return open_digraph(self.inputs, self.outputs, self.nodes)

  def is_well_formed(self): #test si un circuit booléen est bien formé
    tmp = self.copy()
    for node in tmp.get_nodes():
      indegree = node.indegree()
      outdegree = node.outdegree()
      if node.get_id() in self.get_output_ids():
        outdegree += 1
      if((node.label == "&" or node.label == "|" or node.label == "^") and (outdegree != 1)):#noeud est un OU ou un ET
        print(node.id)
        print("code d'erreur a")
        return False
      if((node.label == "∼") and (indegree != 1 or outdegree != 1)):#noeud est un not   
        print(node.id)
        print("code d'erreur b")
        return False
      if(node.label == "" and indegree != 1 ): #noeud est une copie
        print(node.id)
        print("code d'erreur c")
        #return False
      if((node.label == "1" or node.label == "0") and (indegree != 0 or outdegree != 1)): #noeud est une constante    
        print(node.id)
        print("code d'erreur d")
        return False   
    if(tmp.is_cyclic()):
      print("Y")
    return (not tmp.is_cyclic())

  def apply_copy_rule(self, data_node_id, cp_node_id):
    '''
    data_node_id, cp_node_id : int; the ids of the nodes on which to apply the rule
    Applies the "data copy" rule of boolean circuits on the given nodes.
    output : int list; the list of nodes that were created
    '''
    
    data = self.get_node_by_id(data_node_id).get_label()
    assert data in ['0','1'], "wrong data label"
    assert cp_node_id in self.get_node_by_id(data_node_id).get_children_ids(), \
    "the two nodes are not connected"
    return_nodes=[]
   
    # case where the copy node is also an output
    for ind in range(len(self.outputs)):
      if self.outputs[ind] == cp_node_id:
        new_id = self.add_node(data, [],[])
        self.outputs[ind] = new_id
        return_nodes.append(new_id)
    
    # general case
    children = self.get_node_by_id(cp_node_id).get_children_ids()
    for child in children:
      new_id = self.add_node(data, [],[child])
      return_nodes.append(new_id)
    
    self.remove_node_by_ids([data_node_id, cp_node_id])
    
    assert(self.is_well_formed())
    return return_nodes
  
  def apply_not_rule(self, data_node_id, n_node_id):
    """
    data_node_id, n_node_id : int; the ids of the nodes on which to apply the rule
    Applies the "not" rule of boolean circuits on the given nodes.
    output : /
    """
    data = self.get_node_by_id(data_node_id).get_label()
    assert data in ['0','1'], "wrong data label"
    assert n_node_id in self.get_node_by_id(data_node_id).get_children_ids(), \
    "the two nodes are not connected"
    assert self.get_node_by_id(n_node_id).get_label() == '~', 'wrong gate'
    if data == '1':
      self.nodes[n_node_id].label = '0'
    else:
      self.nodes[n_node_id].label = '1'
    self.remove_node_by_id(data_node_id)

  def apply_and_rule(self, data_node_id, and_node_id):
    """
    data_node_id, and_node_id : int; the ids of the nodes on which to apply the rule
    Applies the "and" rule of boolean circuits on the given nodes.
    output : /
    """
    data = self.get_node_by_id(data_node_id).get_label()
    assert data in ['0','1'], "wrong data label"
    assert and_node_id in self.get_node_by_id(data_node_id).get_children_ids(), \
    "the two nodes are not connected"
    assert self.get_node_by_id(and_node_id).get_label() == '&', 'wrong gate'
    if data == "0":
      self.remove_node_by_id(data_node_id)
      for node_id in self.get_node_by_id(and_node_id).get_parents_ids():
        self.remove_edge(node_id, and_node_id)
        self.add_node("", [node_id], [])
      self.nodes[and_node_id].label = "0"
    else:
      self.remove_node_by_id(data_node_id)
        
  def apply_or_rule(self, data_node_id, or_node_id):
    """
    data_node_id, or_node_id : int; the ids of the nodes on which to apply the rule
    Applies the "and" rule of boolean circuits on the given nodes.
    output : /
    """
    data = self.get_node_by_id(data_node_id).get_label()
    assert data in ['0','1'], "wrong data label"
    assert or_node_id in self.get_node_by_id(data_node_id).get_children_ids(), \
    "the two nodes are not connected"
    assert self.get_node_by_id(or_node_id).get_label() == '|', 'wrong gate'
    if data == "1":
      self.remove_node_by_id(data_node_id)
      for node_id in self.get_node_by_id(or_node_id).get_parents_ids():
        self.remove_edge(node_id, or_node_id)
        self.add_node("", [node_id], [])
      self.nodes[or_node_id].label = "1"
    else:
      self.remove_node_by_id(data_node_id)
  
  def apply_xor_rule(self, data_node_id, xor_node_id):
    data = self.get_node_by_id(data_node_id).get_label()
    assert data in ['0', '1'], "wrong data label"
    assert self.get_node_by_id(xor_node_id).get_label() == '^', 'wrong gate'
    assert xor_node_id in self.get_node_by_id(data_node_id).get_children_ids(), \
    "the two nodes are not connected"
    self.remove_node_by_id(data_node_id)
    return_nodes = []
    if (data == "1"):
      if xor_node_id in self.get_output_ids(): #case where xor gate is an output
        self.outputs.remove(xor_node_id)
        new_id = self.add_node("~", [xor_node_id], [])
        self.add_output_id(new_id)
      else: #case were xor gate isn't an output
        children = self.get_node_by_id(xor_node_id).get_children_ids()
        self.nodes[xor_node_id].children = []
        for id in children:
          self.nodes[id].parents = []
        new_id = self.add_node("~", [xor_node_id], children)
        return_nodes = [new_id]

    assert(self.is_well_formed())
    return return_nodes

  def apply_neutral_rule(self, neutral_node_id):#éléments neutres
    data = self.get_node_by_id(neutral_node_id).get_label()
    assert data in ['|', '^', '&'], "wrong data label"
    assert (self.get_node_by_id(neutral_node_id).get_parents_ids() == [] and not neutral_node_id in self.get_input_ids()), "non neutral gate"
    children = self.get_node_by_id(neutral_node_id).get_children_ids()
    if (data == "|" or data == "^"):
      self.nodes[neutral_node_id].label = "0"
    elif (data == "&"):
      self.nodes[neutral_node_id].label = "1"
      
  def calc_simple_boolean_circ(self, start_node_id):
    actual_node = self.get_node_by_id(start_node_id)
    data = actual_node.get_label()
    if not data in ["0", "1"]:
        #recurtion
      for parent in actual_node.get_parents_ids():
        self.calc_simple_boolean_circ(parent)
      if data == "&":
        #reduction
        while(len(self.nodes[start_node_id].parents) > 2): 
          self.apply_and_rule(self.nodes[start_node_id].parents[0], start_node_id)
        #calcul
        if(self.get_node_by_id(start_node_id).get_parents_ids() == []):
          self.apply_neutral_rule(start_node_id)
        else:
          if(self.get_node_by_id(self.get_node_by_id(start_node_id).get_parents_ids()[0]).get_label() == "0" or self.get_node_by_id(self.get_node_by_id(start_node_id).get_parents_ids()[1]).get_label() == "0"):
            self.nodes[start_node_id].label = "0"
          else:
            self.nodes[start_node_id].label = "1"
          parents = self.get_node_by_id(start_node_id).get_parents_ids().copy()
          for parent in parents:
            self.remove_edge(parent, start_node_id)
            self.add_node("", [parent], [])
      elif data == "|":
        #reduction
        while(len(self.nodes[start_node_id].parents) > 2): 
          self.apply_and_rule(self.nodes[start_node_id].parents[0], start_node_id)
        #calcul
        if(self.get_node_by_id(start_node_id).get_parents_ids() == []):
          self.apply_neutral_rule(start_node_id)
        else:
          if(self.get_node_by_id(self.get_node_by_id(start_node_id).get_parents_ids()[0]).get_label() == "0" and self.get_node_by_id(self.get_node_by_id(start_node_id).get_parents_ids()[1]).get_label() == "0"):
            self.nodes[start_node_id].label = "0"
          else:
            self.nodes[start_node_id].label = "1"
          parents = self.get_node_by_id(start_node_id).get_parents_ids().copy()
          for parent in parents:
            self.remove_edge(parent, start_node_id)
            self.add_node("", [parent], [])
      elif data == "^":
        #reduction
        while(len(self.nodes[start_node_id].parents) > 2): 
          self.apply_and_rule(self.nodes[start_node_id].parents[0], start_node_id)
        #calcul
        if(self.get_node_by_id(start_node_id).get_parents_ids() == []):
          self.apply_neutral_rule(start_node_id)
        else:
          if(self.get_node_by_id(self.get_node_by_id(start_node_id).get_parents_ids()[0]).get_label() == "1" and self.get_node_by_id(self.get_node_by_id(start_node_id).get_parents_ids()[1]).get_label() == "1"):
            self.nodes[start_node_id].label = "1"
          if(self.get_node_by_id(self.get_node_by_id(start_node_id).get_parents_ids()[0]).get_label() == "0" and self.get_node_by_id(self.get_node_by_id(start_node_id).get_parents_ids()[1]).get_label() == "0"):
            self.nodes[start_node_id].label = "1"
          else:
            self.nodes[start_node_id].label = "1"
          parents = self.get_node_by_id(start_node_id).get_parents_ids().copy()
          for parent in parents:
            self.remove_edge(parent, start_node_id)
            self.add_node("", [parent], [])
      elif data == "~":
        if self.get_node_by_id(start_node_id).get_label() == "1":
          self.nodes[start_node_id].label = "0"
        else:
          self.nodes[start_node_id].label = "1"
        parents = self.get_node_by_id(start_node_id).get_parents_ids().copy()
        for parent in parents:
          self.remove_edge(parent, start_node_id)
          self.add_node("", [parent], [])
      elif data == "":
        self.apply_copy_rule(self.get_node_by_id(start_node_id).get_parents_ids()[0], start_node_id)
      else:
        assert False, "this label doesn't exist"

  def reduce_eval(self):
    for node_id in self.get_output_ids():
      self.calc_simple_boolean_circ(node_id)

#end of the class

def parse_parentheses(*s, fusion_flag=True):
  graphs = []
  for prop in s:
    #creation du graph
    local = open_digraph([], [0], [node(0, '', [], [])])
    #creations des noeuds et ajouts au graph
    current_node = 0
    s2 = ''
    for char in prop:
      if char == '(':
        local.nodes[current_node].label += s2
        current_node = local.add_node('', [], [current_node])
        s2 = ''
      elif char == ')':
        local.nodes[current_node].label += s2
        current_node = local.nodes[current_node].children[0]
        s2 = ''
      else:
        s2 += char
  #gestion des inputs
    for i in range(len(local.get_nodes())):  
      n_local = local.nodes[i]      #n_local est un node
      label = n_local.get_label()
      if(not label in ["|", "&", "~", ""]):
        if(not n_local.id in local.get_input_ids()):
          local.add_input_id(n_local.get_id())
    graphs.append(local)
  g = graphs[0]
  for i in range(1, len(graphs)):
    g.iparallel(graphs[i])
  if fusion_flag:
    #fusion
    to_fuse = {}
    for n_local in g.get_nodes():
      if(n_local.get_label() in to_fuse.keys()):
        to_fuse[n_local.get_label()].append(n_local.get_id())
      else:
        if(not n_local.get_label() in ["|", "&", "~", ""]):
          to_fuse[n_local.get_label()] = [n_local.get_id()]
    for i in to_fuse.keys():
      if(not i in ["|", "&", "~", ""]):
        for j in range(1,len(to_fuse[i])):
          g.fusion(to_fuse[i][0],to_fuse[i][j])
  res = bool_circ(g)
  for id in res.get_input_ids():
    res.starters[id] = g.nodes[id].get_label()
  #renvoie
  #print(res.starters)
  return res

def random_bool_circ(n, nbInputs = None, nbOutputs = None):
  #step 1 : création du graph
  g = random_graph(n,1,form="DAG")
  
  #step 2 : création des inputs/outputs
  for node in g.get_nodes():
    if( node.parents == []):
      g.inputs.append(node.get_id())
    if(node.children == []):
      g.outputs.append(node.get_id())
  
  #step 2.5 : affinage des inputs/outputs
  allNodes = [g.nodes[i] for i in g.get_node_ids()]
  #inputs:
  if nbInputs != None:
    n = len(g.get_input_ids())
    if n < nbInputs:
      for i in range(nbInputs - n):
        nodeLocal = random.choice(allNodes)
        while(nodeLocal.get_id() in g.get_input_ids()):
          nodeLocal = random.choice(allNodes)
        new_id = g.add_node("value", [], [nodeLocal.get_id()])
        g.add_input_id(new_id)
    elif n > nbInputs:
      for i in range(n-nbInputs):
        idInput1 = random.choice(g.get_input_ids())
        idInput2 = random.choice(g.get_input_ids())
        while(idInput1 == idInput2):
          idInput2 = random.choice(g.get_input_ids())
        new_id = g.add_node("value", [], [idInput1, idInput2])
        g.inputs.remove(idInput1)
        g.inputs.remove(idInput2)
        g.add_input_id(new_id)
  #outputs:
  if nbOutputs != None:
    n = len(g.get_output_ids())
    if n < nbOutputs:
      for i in range(nbOutputs - n):
        nodeLocal = random.choice(allNodes)
        while(nodeLocal.get_id() in g.get_output_ids()):
          nodeLocal = random.choice(allNodes)
        new_id = g.add_node("value", [nodeLocal.get_id()], [])
        g.add_output_id(new_id)
    elif n > nbOutputs:
      for i in range(n-nbOutputs):
        idOutput1 = random.choice(g.get_output_ids())
        idOutput2 = random.choice(g.output())
        while(idOutput1 == idOutput2):
          idOutput2 = random.choice(g.get_output_ids())
        new_id = g.add_node("value", [idOutput1, idOutput2], [])
        g.outputs.remove(idOutput1)
        g.outputs.remove(idOutput2)
        g.add_output_id(new_id)

  #step 3 : renommage des noeuds
  for node in g.get_nodes():
    indegree = node.indegree()
    outdegree = node.outdegree()
    if node.get_id() in g.get_output_ids():
      outdegree += 1
    if(indegree == outdegree and indegree == 1):
      g.nodes[node.get_id()].label = "~"
    if(indegree > 1 and outdegree == 1):
      tmp = random.randint(0,3)
      if (tmp == 1):
        g.nodes[node.get_id()].label = "&" 
      elif (tmp == 2) :
        g.nodes[node.get_id()].label ="|"
      #g.nodes[node.get_id()].label = "&" if tmp == 1 else "|"
      else:
        g.nodes[node.get_id()].label = "^"

    if(indegree > 1 and outdegree > 1):
      tmp = random.randint(0,3)
      if (tmp == 1):
        local = "&" 
      elif (tmp == 2) :
        local = "|"
      else:
        local = "^"
      
      id1 = g.add_node(local,node.get_parents_ids(),[])
      id2 = g.add_node("",[],node.get_children_ids())
      g.add_edge(id1,id2)
      for i in range(len(g.get_input_ids())):
        if(g.get_input_ids()[i] == node.get_id()):
          g.inputs[i] = id1
        
      for i in range(len(g.get_output_ids())):
        if(g.get_output_ids()[i] == node.get_id()):
          g.outputs[i] = id2
      g.remove_node_by_id(node.get_id())

    if(node.indegree() == 1 and node.outdegree() > 1):
      g.nodes[node.get_id()].label = ""
  res = bool_circ(g)
  for i in range(len(res.get_input_ids())):
    res.nodes[res.get_input_ids()[i]].label = 'input ' + str(i)
  #print(res)
  return res

def int_to_bool_circ(n,size = 8):
  b = bool_circ(open_digraph([],[],[]))
  binaire = bin(n)[2:]
  for i in range(size-len(binaire)):
    tmp = b.add_node("0",[],[])
    b.add_output_id(tmp)

  for element in binaire:
    tmp = b.add_node(element,[],[])
    b.add_output_id(tmp)

  return b

      







