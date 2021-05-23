#from modules.utils import *


class open_digraph_tools_mx: 
   
  def add_input_id(self, id): #@param:  entier étant l'ID à ajouter (int)
    self.inputs.append(id)

  def add_output_id(self, id): #@param:  entier étant l'ID à ajouter (int)
    self.outputs.append(id)

  def add_edge(self, src, tgt): #ajoute une arête du noeud d’id src au noeud d’id tgt /!\ ERREUR ENONCÉ
    self.get_node_by_id(src).add_child_id(tgt) #bisect.insort(self.get_node_by_id(src).children,get_id(tgt)) #self.get_node_by_id(src).add_child_id(tgt)
    self.get_node_by_id(tgt).add_parent_id(src) #bisect.insort(self.get_node_by_id(tgt).parents,get_id(src))

  def add_edges(self, src, list_tgt): #ajoute des arêtes du noeud d’id src aux noeud d’id de la listtgt
    for tgt in list_tgt:
      self.get_node_by_id(src).add_child_id(tgt) #bisect.insort(self.get_node_by_id(src).children,get_id(tgt))
      self.get_node_by_id(tgt).add_parent_id(src)#bisect.insort(self.get_node_by_id(tgt).parents,get_id(src))

  def add_node(self, label='', parents=[],children=[]):#ajoute un noeud (avec label) au graphe avec un nouvel id
    newid = self.new_id()
    n0 = node(newid, label, [], [])
    self.nodes[newid] = n0
    for element in parents:
      self.add_edge(element,newid)
    self.add_edges(newid,children)
    return newid

  def remove_edge(self, src, tgt): #supprime une arête du noeud src au noeud tgt
    self.nodes[src].children.remove(tgt)
    self.nodes[tgt].parents.remove(src)
  
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
