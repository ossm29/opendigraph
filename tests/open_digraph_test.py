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

class NodeTest(unittest.TestCase):

  def setUp(self):
    self.n0 = node(0, 'i', [], [1])
    self.n1 = node(1, 'j', [0], [])

  def test_copyNode(self):
    n2 = self.n0.copy()
    self.assertEqual(n2.label, self.n0.label)
    self.assertEqual(n2.id, self.n0.id)
    self.assertIsNot(n2, self.n0)

class GraphTest(unittest.TestCase):

  def setUp(self):
    self.n0 = node(0, 'i', [], [1])
    self.n1 = node(1, 'j', [0], [])
    self.g = open_digraph([0], [1], [self.n0, self.n1])
  
  def test_copyGraph(self):
    g2 = self.g.copy()
    self.assertEqual(g2.inputs ,self.g.inputs)
    self.assertEqual(g2.outputs ,self.g.outputs)
    self.assertEqual(g2.nodes ,self.g.nodes)
    self.assertIsNot(g2,self.g)

class gettersTest(unittest.TestCase):

  def setUp(self):
    self.n0 = node(0, 'i', [], [1])
    self.n1 = node(1, 'j', [0], [])
    self.g = open_digraph([0], [1], [self.n0, self.n1])

  def test_nodeGetters(self):
    self.assertEqual(self.n0.get_id(), 0)
    self.assertEqual(self.n1.get_id(), 1)
    self.assertEqual(self.n0.get_label(), 'i')
    self.assertEqual(self.n1.get_label(), 'j')
    self.assertEqual(self.n0.get_parents_ids(), [])
    self.assertEqual(self.n1.get_parents_ids(), [0])
    self.assertEqual(self.n0.get_parents_ids(), [])
    self.assertEqual(self.n1.get_parents_ids(), [0])
if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.

  
