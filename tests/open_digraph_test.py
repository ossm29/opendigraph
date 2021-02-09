#Oussama Konate, Thomas Delépine, groupe 8
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

class EqTest(unittest.TestCase):
  def test_eq_node(self):
    self.assertEqual(node(0, 'i', [], [1,2])==node(1, 'j', [0], []), False)
    self.assertEqual(node(0, 'i', [], [1])==node(1, 'j', [0], []), False)
    self.assertEqual(node(2, 'j', [2, 3], [2,3]) == node(2, 'j', [2, 3], [2,3]), True)
    self.assertEqual(node(0, 'i', [], [1])==node(0, 'i', [], [1]), True)
  def test_eq_graph(self):
    n0 = node(0, 'i', [], [1])
    n1 = node(1, 'j', [0], [])
    g = open_digraph([0, 1], [1], [n0, n1])
    self.assertEqual(g==open_digraph([0, 1], [1], [node(0, 'i', [], [1]), node(1, 'j', [0], [])]), True)
    

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
    self.assertEqual(g2.nodes == self.g.nodes, True)
    self.assertIsNot(g2,self.g)


class gettersTest(unittest.TestCase):

  def setUp(self):
    self.n0 = node(0, 'i', [], [1])
    self.n1 = node(1, 'j', [0], [])
    self.g = open_digraph([0, 1], [1], [self.n0, self.n1])

  def test_nodeGetters(self):
    self.assertEqual(self.n0.get_id(), 0)
    self.assertEqual(self.n1.get_id(), 1)
    self.assertEqual(self.n0.get_label(), 'i')
    self.assertEqual(self.n1.get_label(), 'j')
    self.assertEqual(self.n0.get_parents_ids(), [])
    self.assertEqual(self.n1.get_parents_ids(), [0])
    self.assertEqual(self.n0.get_parents_ids(), [])
    self.assertEqual(self.n1.get_parents_ids(), [0])

  def test_graphGetters(self):
    self.assertEqual(self.g.get_input_ids(), [0, 1])
    self.assertEqual(self.g.get_output_ids(), [1])
    self.assertEqual(self.g.get_id_node_map(), {0 : self.n0, 1 : self.n1})
    self.assertEqual(self.g.get_nodes(), [self.n0, self.n1])
    self.assertEqual(self.g.get_node_ids(), [0, 1])
    self.assertEqual(self.g.get_node_by_id(1), self.n1)
    self.assertEqual(self.g.get_nodes_by_ids([0, 1]), [self.n0, self.n1])

class settersTest(unittest.TestCase):

  def setUp(self):
    self.n0 = node(0, 'i', [], [1])
    self.n1 = node(1, 'j', [0], [])
    self.g = open_digraph([0, 1], [1], [self.n0, self.n1])
  
  def test_nodeSetters(self):
    n2 = self.n0.copy()
    n2.set_id(10)
    n2.set_label('k')
    n2.set_parent_ids([0,1,2])
    n2.set_children_ids([4,5,6])
    n2.add_parent_id(3)
    n2.add_child_id(7)
    self.assertEqual(n2.id, 10)
    self.assertEqual(n2.label, 'k' )
    self.assertEqual(n2.parents, [0,1,2,3])
    self.assertEqual(n2.children, [4,5,6,7])

  def test_graphSetters(self):
    g1 = self.g.copy()
    g1.set_input_ids([0,1,2])
    g1.add_input_id(3)
    g1.set_output_ids([4,5,6])
    g1.add_output_id(7)
    self.assertEqual(g1.inputs, [0,1,2,3])
    self.assertEqual(g1.outputs, [4,5,6,7])

class removersTest(unittest.TestCase):
  def test_removersNodes(self):
    n0 = node(0, 'i', [2,3,4,5,4,4], [1])
    n0.remove_parent_id(4)
    self.assertEqual(n0.parents, [2,3,5,4,4])
    n0.remove_parent_id_all(4)
    self.assertEqual(n0.parents, [2,3,5])
    n1 = node(1, 'j', [0], [8,4,8,5,6,6,8])
    n1.remove_child_id(8)
    self.assertEqual(n1.children, [4,8,5,6,6,8])
    n1.remove_child_id_all(8)
    self.assertEqual(n1.children, [4,5,6,6])
    #remove_node_by_id
    l0 = node(0, 'i', [], [1,2])
    l1 = node(1, 'j', [0], [2])
    l2 = node(2, 'k', [0, 1], [])
    l3 = node(3, 'l', [0],[])
    g2 = open_digraph([0], [2], [l0, l1, l2,l3])
    g2.remove_node_by_id(2)
    self.assertEqual(g2.get_nodes(), [l0,l1,l3])
    #remove_nodes_by_ids
    g2.remove_node_by_ids([1,3])
    self.assertEqual(g2.get_nodes(), [l0])

  def test_removersEdges(self):
    k0 = node(0, 'i', [], [1])
    k1 = node(1, 'j', [0], [])
    g = open_digraph([0, 1], [1], [k0, k1])
    g.remove_edge(0,1)
    gcomp = open_digraph([0, 1], [1], [node(0, 'i', [], []), node(1, 'j', [], [])])
    self.assertEqual(g,gcomp)
    #remove_edges
    l0 = node(0, 'i', [], [1,2])
    l1 = node(1, 'j', [0], [2])
    l2 = node(2, 'k', [0, 1], [])
    g2 = open_digraph([0], [2], [l0, l1, l2])
    g2.remove_edges([(0,1),(1,2)])
    gcomp = open_digraph([0],[2], [node(0, 'i', [], [2]),node(1, 'j', [], []),node(2, 'k', [0], [])])
    self.assertEqual(g2,gcomp)
    
class addersTest(unittest.TestCase):
  def test_addersEdges(self):
    k0 = node(0, 'i', [], [])
    k1 = node(1, 'j', [], [])
    g = open_digraph([0, 1], [1], [k0, k1])
    g.add_edge(0,1)
    gcomp = open_digraph([0, 1], [1], [node(0, 'i', [], [1]), node(1, 'j', [0], [])])
    self.assertEqual(g,gcomp)
    #add_edges
    l0 = node(0, 'i', [], [])
    l1 = node(1, 'j', [], [2])
    l2 = node(2, 'k', [1], [])
    g2 = open_digraph([0], [2], [l0, l1, l2])
    g2.add_edges(0, [1,2])
    gcomp = open_digraph([0], [2], [node(0, 'i', [], [1,2]), node(1, 'j', [0], [2]), node(2, 'k', [0,1], [])])
    self.assertEqual(g2, gcomp)

  def test_addersNodes(self):
    u0 = node(0, 'i', [], [])
    g = open_digraph([0],[],[u0])
    g.add_node('j',[0],[])
    
class wellFormed(unittest.TestCase):
  def test_is_well_formed(self):
    n0 = node(0, 'i', [], [1])
    n1 = node(1, 'j', [0], [])
    n2 = node(2, 'j', [2, 3], [2,3])
    n3 = node(3, 'j', [2], [2])
    g1 = open_digraph([0, 1], [1], [n0, n1])
    self.assertEqual(g1.is_well_formed(), True)
    g2 = open_digraph([0, 1, 2], [1], [n0, n1])
    self.assertEqual(g2.is_well_formed(), False)
    g3 = open_digraph([0, 1, 2], [1], [n0, n1, n2, n3])
    self.assertEqual(g3.is_well_formed(), True)
    g4 = open_digraph([], [], [])
    self.assertEqual(g4.is_well_formed(), True)
    g5 = open_digraph([0], [0], [n0, n2, n3])
    self.assertEqual(g5.is_well_formed(), False)

if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.

  
