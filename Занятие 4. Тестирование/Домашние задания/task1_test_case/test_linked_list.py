import unittest
import coverage
from linked_list import LinkedList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_init_LinkedList_without_next(self):
        linked_list = LinkedList([1, 2, 3])
        linked_list.append(4)
        self.assertEqual(linked_list, [1, 2, 3, 4])

if __name__ == '__main__':
