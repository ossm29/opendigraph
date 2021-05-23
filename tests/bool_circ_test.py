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
    n0 = node(0, '1', [], [1]) 
    n1 = node(1, '', [0], [2]) #output
    n2 = node(2, '~', [1], []) #output
    b = bool_circ(open_digraph([0], [1,2], [n0,n1,n2]))
    node_res = b.apply_copy_rule(0, 1)
    self.assertEqual(node_res, [3, 4])
    self.assertEqual(b, bool_circ(open_digraph([], [3, 2], [node(2, '~', [4], []), node(3, '1', [], []), node(4, '1', [], [2])])))
    b.apply_not_rule(4, 2)
    self.assertEqual(b, bool_circ(open_digraph([], [3,2], [node(2, '0', [], []), node(3, '1', [], [])])))

    m0 = node(0, '1', [], [4]) 
    m1 = node(1, '1', [], [4]) 
    m2 = node(2, '0', [], [4]) 
    m3 = node(3, '1', [], [4]) 
    m4 = node(4, '&', [0,1,2,3], []) #output
    b2 = bool_circ(open_digraph([], [4], [m0,m1,m2,m3,m4]))
    b2.apply_and_rule(0,4)
    self.assertEqual(b2, bool_circ(open_digraph([], [4], [node(1, '1', [], [4]), node(2, '0', [], [4]), node(3, '1', [], [4]), node(4, '&', [1, 2, 3], [])])))
    b2.apply_and_rule(1, 4)
    self.assertEqual(b2, bool_circ(open_digraph([], [4], [node(2, '0', [], [4]), node(3, '1', [], [4]), node(4, '&', [2, 3], [])])))
    b2.apply_and_rule(2, 4)
    self.assertEqual(b2, bool_circ(open_digraph([], [4], [node(3, '1', [], [0]), node(4, '0', [], []), node(0,'', [3], [])])))
    
    m0 = node(0, '0', [], [4]) 
    m1 = node(1, '0', [], [4]) 
    m2 = node(2, '1', [], [4]) 
    m3 = node(3, '0', [], [4]) 
    m4 = node(4, '|', [0,1,2,3], []) #output
    b2 = bool_circ(open_digraph([], [4], [m0,m1,m2,m3,m4]))
    b2.apply_or_rule(0,4)
    self.assertEqual(b2, bool_circ(open_digraph([], [4], [node(1, '0', [], [4]), node(2, '1', [], [4]), node(3, '0', [], [4]), node(4, '|', [1, 2, 3], [])])))
    b2.apply_or_rule(1, 4)
    self.assertEqual(b2, bool_circ(open_digraph([], [4], [node(2, '1', [], [4]), node(3, '0', [], [4]), node(4, '|', [2, 3], [])])))
    b2.apply_or_rule(2, 4)
    self.assertEqual(b2, bool_circ(open_digraph([], [4], [node(3, '0', [], [0]), node(4, '1', [], []), node(0,'', [3], [])])))
    
    o0 = node(0, '0', [], [5])
    o1 = node(1, '1', [], [5])
    o2 = node(2, '1', [], [5])
    o3 = node(3, '1', [], [5])
    o4 = node(4, '1', [], [5])
    o5 = node(5, '^', [0,1,2,3,4], []) #output
    b3 = bool_circ(open_digraph([], [5], [o0,o1,o2,o3,o4,o5]))
    b3.apply_xor_rule(0, 5)
    self.assertEqual(b3, bool_circ(open_digraph([], [5], [node(1, "1", [], [5]), node(2, "1", [], [5]), node(3, "1", [], [5]), node(4, "1", [], [5]), node(5, "^", [1, 2, 3, 4], [])])))
    b3.apply_xor_rule(1, 5)
    self.assertEqual(b3, bool_circ(open_digraph([], [0], [node(2, "1", [], [5]), node(3, "1", [], [5]), node(4, "1", [], [5]), node(5, "^", [2, 3, 4], [0]), node(0, '~', [5], [])])))   
    b3.apply_xor_rule(2, 5)
    self.assertEqual(b3, bool_circ(open_digraph([], [0], [node(3, "1", [], [5]), node(4, "1", [], [5]), node(5, "^", [3, 4], [1]), node(0, "~", [1], []), node(1, "~", [5], [0])])))
    
    p0 = node(0, '|', [], [2])
    p1 = node(1, '&', [], [2])
    p2 = node(2, '|', [0,1], []) #output
    b4 = bool_circ(open_digraph([], [2], [p0,p1,p2]))
    b4.apply_neutral_rule(0)
    self.assertEqual(b4, bool_circ(open_digraph([], [2], [node(0, '0', [], [2]), node(1, '&', [], [2]), node(2, '|', [0,1], [])])))
    b4.apply_neutral_rule(1)
    self.assertEqual(b4, bool_circ(open_digraph([], [2], [node(0, '0', [], [2]), node(1, '1', [], [2]), node(2, '|', [0,1], [])])))

  def test_calc(self):
    n0 = node(0, '0', [], [2])
    n1 = node(1, '1', [], [2])
    n2 = node(2, '&', [0,1], [])
    b = bool_circ(open_digraph([], [2], [n0,n1,n2]))
    b.calc_node_value(2)
    self.assertEqual(b, bool_circ(open_digraph([], [2], [node(1, "1", [], [0]), node(2, "0", [], []), node(0,"", [1], [])])))
    
    n0 = node(0, '1', [], [2])
    n1 = node(1, '1', [], [2])
    n2 = node(2, '&', [0,1], [])
    b = bool_circ(open_digraph([], [2], [n0,n1,n2]))
    b.calc_node_value(2)
    self.assertEqual(b, bool_circ(open_digraph([], [2], [node(2, "1", [], [])])))

    n0 = node(0, '1', [], [2])
    n1 = node(1, '1', [], [2])
    n2 = node(2, '|', [0,1], [])
    b = bool_circ(open_digraph([], [2], [n0,n1,n2]))
    b.calc_node_value(2)
    self.assertEqual(b, bool_circ(open_digraph([], [2], [node(1, "1", [], [0]), node(2, "1", [], []), node(0,"", [1], [])])))
    
    n0 = node(0, '0', [], [2])
    n1 = node(1, '0', [], [2])
    n2 = node(2, '|', [0,1], [])
    b = bool_circ(open_digraph([], [2], [n0,n1,n2]))
    b.calc_node_value(2)
    self.assertEqual(b, bool_circ(open_digraph([], [2], [node(2, "0", [], [])])))
    
    n0 = node(0, '0', [], [2])
    n1 = node(1, '0', [], [2])
    n2 = node(2, '^', [0,1], [])
    b = bool_circ(open_digraph([], [2], [n0,n1,n2]))
    b.calc_node_value(2)
    self.assertEqual(b, bool_circ(open_digraph([], [2], [node(2, "0", [], [])])))

    n0 = node(0, '1', [], [2])
    n1 = node(1, '1', [], [2])
    n2 = node(2, '^', [0,1], [])
    b = bool_circ(open_digraph([], [2], [n0,n1,n2]))
    b.calc_node_value(2) 
    self.assertEqual(b, bool_circ(open_digraph([], [0], [node(2, "0", [], [1]), node(0, "~", [1], []), node(1, "~", [2], [0])])))
    
    b.calc_node_value(0)
    self.assertEqual(b, bool_circ(open_digraph([], [0], [node(0, '0', [], [])])))
    
    n0 = node(0, '0', [], [1])
    n1 = node(1, '', [0], [2, 3])
    n2 = node(2, "~", [1], [])
    n3 = node(3, "~", [1], [])
    b = bool_circ(open_digraph([], [2,3], [n0,n1,n2,n3]))
    b.calc_node_value(2)
    b.calc_node_value(3)
    self.assertEqual(b, bool_circ(open_digraph([], [2,3], [node(2, "1", [], []), node(3, "1", [], [])])))

    n0 = node(0, '0', [], [1])
    n1 = node(1, '', [0], [3])
    n2 = node(2, '1', [], [3])
    n3 = node(3, '&', [1,2], [])
    b = bool_circ(open_digraph([], [1,3], [n0, n1, n2, n3]))
    b.calc_node_value(3)
    self.assertEqual(b, bool_circ(open_digraph([], [4,3], [node(3, '0', [], []), node(4, '0', [], [])])))

    n0 = node(0, '1', [], [3])
    n1 = node(1, '1', [], [3])
    n2 = node(2, '1', [], [4])
    n3 = node(3, '^', [0,1], [4])
    n4 = node(4, '^', [2,3], [])
    b = bool_circ(open_digraph([], [4], [n0,n1,n2,n3,n4]))
    b.reduce_eval()
    self.assertEqual(b, bool_circ(open_digraph([], [4], [node(4,'0',[],[])])))

    n0 = node(0, '1', [], [2])
    n1 = node(1, '0', [], [3])
    n2 = node(2, '', [0], [3, 5])
    n3 = node(3, '&', [1,2], [4])
    n4 = node(4, '', [3], [5])
    n5 = node(5, '^', [2, 4], [])
    b = bool_circ(open_digraph([], [4,5], [n0,n1,n2,n3,n4,n5]))
    b.reduce_eval()
    self.assertEqual(b,bool_circ(open_digraph([], [1,2], [node(1, '0', [], []), node(2, '1', [], [])])))

    m1 = node(1, '1', [], [7])
    m2 = node(2, '0', [], [11])
    m3 = node(3, '0', [], [8])
    m4 = node(4, '1', [], [12])
    m5 = node(5, '1', [], [9])
    m6 = node(6, '0', [], [10])
    m7 = node(7, '', [1], [11, 14])
    m8 = node(8, '', [3], [12,17])
    m9 = node(9, '', [5], [12,13,17])
    m10 = node(10, '~', [6], [13])
    m11 = node(11, '&', [2, 7], [15])
    m12 = node(12, '|', [4,8,9], [])
    m13 = node(13, '^', [9,10], [16])
    m14 = node(14, '^', [7, 15], [])
    m15 = node(15, '', [11], [14])
    m16 = node(16, '', [13], [17])
    m17 = node(17, '|', [8,9,16], [])
    b = bool_circ(open_digraph([], [12, 14, 15, 16, 17], [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17]))
    b.reduce_eval()
    self.assertEqual(b, bool_circ(open_digraph([], [12, 2, 7, 17, 5], [node(12, '1', [], []), node(17, '1', [], []), node(2, '0', [], []), node(5, '1', [], []), node(7, '0', [], [])])))


if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
              
