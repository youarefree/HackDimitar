import unittest
from tree import Node
from tree import Tree


class treeTest(unittest.TestCase):

    def setUp(self):
        n = Node(5, parent=None)
        self.tree = Tree(n)
        self.tree.add_child(parent=5, child=4)
        self.tree.add_child(parent=5, child=3)
        self.tree.add_child(parent=4, child=2)

    def test_get_element(self):
        self.assertEqual(self.tree.get_element(5, start=self.tree.root).data, 5)

    # def test_find(self):
    #     self.assertTrue(self.tree.find(3))

    def test_count_nodes(self):
        self.assertEqual(self.tree.count_nodes(), 4)

    def test_height(self):
        self.assertEqual(self.tree.height(self.tree.root), 3)

    def test_walk(self):
        self.assertEqual(self.tree.walk(self.tree.root), [])


if __name__ == '__main__':
    unittest.main()

