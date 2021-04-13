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
    b4 = node(4,"|",[0,3],[8])
    s1 = node(8, "sortie", [4], [])
    c = bool_circ(open_digraph([5,6,7], [4], [b0,b1,b2,b3,b4,c1,c2,c3,s1]))

  def test_generation(self):
    g = parse_parentheses("((x0)&((x1)&(x2)))|((x1)&(~(x2)))", "((x0)&(~(x1)))|(x2)")
    self.assertEqual(g, ([12, 14, 15], {10: node(10, "|", [11, 16], []), 11: node(11, "&", [12, 13], [10]), 2: node(2, "x0", [], [11, 1]), 13: node(13, "&", [14, 15], [11]), 4: node(4, "x1", [], [13, 16, 3]), 5: node(5, "x2", [], [13, 18, 0]), 16: node(16, "&", [14, 18], [10]), 18: node(18, "~", [15], [16]), 0: node(0, "|", [1, 15], []), 1: node(1, "&", [12, 3], [0]), 3: node(3, "~", [14], [1])}, [10, 0]))
    self.assertEqual(g.starters, {12: 'x0', 14: 'x1', 15: 'x2'})


    

if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
              
