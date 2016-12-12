import unittest
from linked_list import LinkedList
from linked_list import Node

# class NodeTest(unittest.TestCase):
#     def setUp(self):
#         self.


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_adding_element(self):
        self.ll.add_element(Node(4))
        self.ll.add_element(Node(3))
        self.ll.add_element(Node(1))
        self.ll.add_element(Node(2))
        self.ll.add_element(Node(4))
        self.ll.add_element(Node(4))
        self.assertEqual(self.ll.size(), 6)

    def test_remove_element(self):
        self.ll.add_element(Node(4))
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)

    def test_print(self):
        self.ll.add_element(Node(3))
        self.assertEqual(self.ll.pprint(), "[3]")

    # def test_index(self):
    #     self.ll.add_element(Node(4))
    #     with self.assertRaises(Exception) as context:
    #         self.ll.index(-10)
    #         self.assertTrue('Out of Range' in context.exception)
    #     # self.assertEqual(self.ll.index(0).value, 4)

    # def test_pprint(self):


if __name__ == '__main__':
    unittest.main()
