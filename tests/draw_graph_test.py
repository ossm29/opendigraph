#Oussama Konate, Thomas Delépine, groupe 8
import sys
sys.path.append('../') # allows us to fetch files from the project root
import math
import unittest
from modules.draw_graph import *

import time



class pointtest(unittest.TestCase):
  def test_point(self):
    p1 = point(1, 2)
    p2 = point(5, 5)
    self.assertEqual(p1, p1.copy())
    self.assertIsNot(p1, p1.copy())
    self.assertEqual(p1 + p2, point(6, 7))
    self.assertEqual(p2 - p1, point(4, 3))
    self.assertEqual(2*p1, point(2, 4))

  def test_draw(self):

    width = WIDTH
    height = HEIGHT
    image = Image.new("RGB", (width, height), 'white')
    draw = ImageDraw.Draw(image)
    #graph compliqué:
    
    '''n0 = node(0, 'i', [1, 1, 1], [1, 3, 6])
    n1 = node(1, 'j', [0], [0,0,0, 3, 6])
    n2 = node(2, 'k', [3], [3])
    n3 = node(3, 'l', [0, 1, 2], [2])
    n4 = node(4, "m", [5], [6, 7])
    n5 = node(5, "n", [], [4, 6, 7])
    n6 = node(6, "o", [0, 1, 4, 5], [])
    n7 = node(7, "p", [4, 5], [])
    g = open_digraph([0, 1, 2], [1, 7], [n0, n1, n2, n3, n4, n5, n6, n7])'''
    
    """
    #def g2
    n0 = node(0,'',[],[3])
    n1 = node(1,'',[],[4,5])
    n2 = node(2,'',[],[4])
    n3 = node(3,'',[0],[5,6,7])
    n4 = node(4,'',[1,2],[6])
    n5 = node(5,'',[1,3],[7])
    n6 = node(6,'',[3,4],[8,9])
    n7 = node(7,'',[3,5],[])
    n8 = node(8,'',[1,6],[])
    n9 = node(9,'',[6],[])
    g2 = open_digraph([0,2],[7, 8, 9],[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])
    """
    '''
    #graph simple:
    n0 = node(0,'i', [1], [1])
    n1 = node(1, 'j', [0], [0])
    g = open_digraph([], [], [n0, n1])
    '''

    #g2 = random_bool_circ(5, 3, 4)
    #g2 = int_to_bool_circ(300)

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
    g2 = bool_circ(open_digraph([], [12, 14, 15, 16, 17], [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17]))
    




    node_pos = {}
    node_pos[1] = point(100, 100)
    node_pos[2] = point(200, 200)
    draw.graph(g2, node_pos, [], [],'topologique')
    
    """
    p1 = point(50, 50)
    p2 = point(50, 100)
    draw.arrows(p1, p2)
    p2.rotate(math.pi/4, p1)
    draw.arrows(p1, p2)
    p2.rotate(math.pi/4, p1)
    draw.arrows(p1, p2)
    p2.rotate(math.pi/4, p1)
    draw.arrows(p1, p2)
    p2.rotate(math.pi/4, p1)
    draw.arrows(p1, p2)
    p2.rotate(math.pi/4, p1)
    draw.arrows(p1, p2)
    p2.rotate(math.pi/4, p1)
    draw.arrows(p1, p2)
    p2.rotate(math.pi/4, p1)
    draw.arrows(p1, p2)
    p2.rotate(math.pi/4, p1)
    draw.arrows(p1, p2)
    draw.bezier(point(50, 50), point(75,75), point(50, 100))
    """
    
    image.save("boolean_circuit_printer.jpg")

    #g3 = random_bool_circ(7)

    #draw.graph(g3,node_pos,[],[],'manual')

    #image.save("random_bool_circ.jpg")
  
class test_display(unittest.TestCase):
  def test_layout(self):
    n0 = node(0, 'i', [], [1])
    n1 = node(1, 'j', [0], [])
    n2 = node(2, 'j', [3], [3])
    n3 = node(3, 'j', [2], [2])
    g1 = open_digraph([0, 1], [1], [n0, n1, n2, n3])
    x = random_layout(g1)

class test_fun(unittest.TestCase):
  def test_slope_angle(self):
    p1 = point(100, 100)
    p2 = point(200, 200)
    self.assertEqual(slope_angle(p1, p2), math.pi/4)
    self.assertEqual(slope_angle(p2, p1), math.pi/4)
    p3 = point(100, 300)
    self.assertEqual(slope_angle(p1, p3), math.pi/2)
    self.assertEqual(slope_angle(p3, p1), math.pi/2)
    self.assertEqual(slope_angle(p2, p3), -math.pi/4)
    self.assertEqual(slope_angle(p3, p2), -math.pi/4)
    self.assertEqual(slope_angle(p3, p3), math.pi/2)
    



if __name__ == '__main__': # the following code is called only when
  unittest.main() 










