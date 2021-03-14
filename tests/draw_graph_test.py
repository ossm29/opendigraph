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
    n0 = node(0, 'i', [1], [1, 3, 6])
    n1 = node(1, 'j', [0], [0])
    n2 = node(2, 'k', [3], [3])
    n3 = node(3, 'l', [1, 2], [2])
    n4 = node(4, "m", [5], [6, 7])
    n5 = node(5, "n", [], [4])
    n6 = node(6, "o", [1, 5], [])
    n7 = node(7, "p", [5], [])
    g = open_digraph([0, 1, 2], [1, 7], [n0, n1, n2, n3, n4, n5, n6, n7])
    node_pos = {}
    node_pos[1] = point(100, 100)
    node_pos[2] = point(200, 200)
    draw.graph(g, node_pos, [], [],'circle')
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
    """
    
    image.save("test.jpg")
  
class test_display(unittest.TestCase):
  def test_layout(self):
    n0 = node(0, 'i', [], [1])
    n1 = node(1, 'j', [0], [])
    n2 = node(2, 'j', [3], [3])
    n3 = node(3, 'j', [2], [2])
    g1 = open_digraph([0, 1], [1], [n0, n1])
    x = random_layout(g1)

if __name__ == '__main__': # the following code is called only when
  unittest.main() 