from modules.utils import *

class open_digraph_getters_setters_mx:
  #get
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
  
  #set
  def set_input_ids(self, ids): #@param : entiers représentant les ID (int list)
    self.inputs = ids 

  def set_output_ids(self, ids): #@param : entiers représentant les ID (int list)
    self.outputs = ids
