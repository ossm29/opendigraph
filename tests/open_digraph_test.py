#Oussama Konate, Thomas Delépine
import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.open_digraph import *

class InitTest(unittest.TestCase):

  def test_init_node(self):
    n0 = node(0, 'i', [], [1])
    self.assertEqual(n0.id, 0)
    self.assertEqual(n0.label, 'i')
    self.assertEqual(n0.parents, [])
    self.assertEqual(n0.children, [1])
    self.assertIsInstance(n0, node)

  def test_init_graph(self):
    n0 = node(0, 'i', [], [1])
    n1 = node(1, 'j', [0], [])
    g = open_digraph([0], [1], [n0, n1])
    self.assertEqual(g.inputs, [0])
    self.assertEqual(g.outputs, [1])
    self.assertEqual(g.nodes[0], n0)
    self.assertEqual(g.nodes[1], n1)

if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run
  
