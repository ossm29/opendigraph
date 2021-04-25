#Oussama Konate, Thomas Delépine, groupe 8
import sys
sys.path.append('../') # allows us to fetch files from the project root
import math
import unittest
from modules.bool_circ import *
import time

class boolTest(unittest.TestCase):
  def test_init(self):
    n0 = node(0, 'i', [], [1])
    n1 = node(1, 'j', [0], [])
    g = open_digraph([0], [1], [n0, n1])
    c1 = bool_circ(g)
    c2 = bool_circ(g)
    self.assertEqual(c1, c2)
  
  def test_is_well_formed(self):
    c1 = node(5, '1', [], [0])
    c2 = node(6, '0', [], [1])
    c3 = node(7, '1', [], [2])
    b0 = node(0,'&',[1,5],[4])
    b1 = node(1,"",[6],[0,2])
    b2 = node(2,"|",[1, 7],[3])
    b3 = node(3,"∼",[2],[4])
    b4 = node(4,"|",[0,3],[])
    c = bool_circ(open_digraph([5,6,7], [4], [b0,b1,b2,b3,b4,c1,c2,c3]))
    self.assertEqual(c, c)

  def test_generation(self):
    bc = parse_parentheses("(((x0)&((x1)&(x2)))|((x1)&(~(x2))))", "(((x0)&(~(x1)))|(x2))")
    self.assertEqual(bc, bool_circ(open_digraph([14,16,17], [11, 0], [node(11, '', [12], []), node(12, '|', [13,18],[11]), node(13, '&',[14,15],[12]), node(14, 'x0',[],[13,2]), node(15, '&', [16, 17],[13]), node(16, 'x1', [],[15,18,4]), node(17, 'x2', [], [15, 20, 1]), node(18, '&', [16, 20], [12]), node(20, '~', [17], [18]), node(0, '', [1], []), node(1, '|', [2,17], [0]), node(2, '&', [14, 4], [1]), node(4, '~', [16], [2]) ])))

  def test_random_bool_circ(self):
    h = random_bool_circ(8)
    #print(h)

  def test_rule(self):
    n0 = node(0, '1', [], [1]) #input
    n1 = node(1, '', [0], [2]) #output
    n2 = node(2, '~', [1], []) #output
    b = bool_circ(open_digraph([0], [1,2], [n0,n1,n2]))
    node_res = b.apply_copy_rule(0, 1)
    self.assertEqual(node_res, [3, 4])
    self.assertEqual(b, bool_circ(open_digraph([], [3, 2], [node(2, '~', [4], []), node(3, '1', [], []), node(4, '1', [], [2])])))
    b.apply_not_rule(4, 2)
    self.assertEqual(b, bool_circ(open_digraph([], [3,2], [node(2, '0', [], []), node(3, '1', [], [])])))





if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
              
