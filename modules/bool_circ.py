#Oussama Konate et Thomas Delépine

from PIL import Image, ImageDraw
import math
from datetime import datetime
from modules.open_digraph import *
from modules.draw_graph import *

class bool_circ(open_digraph):
  def __init__(self, g):
    super().__init__(g.inputs.copy(), g.outputs.copy(), [node.copy() for node in g.get_nodes()])

  def __eq__(self,other):
    return ((self.get_input_ids()== other.get_input_ids()) and (self.get_output_ids() == other.get_output_ids()) 
    and ( self.get_nodes() == other.get_nodes()))

  def __str__(self):
    return ("("+str(self.inputs)+", "+str(self.nodes)
                +", "+str(self.outputs)+")")

  def __repr__(self):
    return "boolean_circ"+str(self)
  
  def convert(self):
    return open_digraph(self.inputs, self.outputs, self.nodes)