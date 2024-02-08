import unittest

from task import Node

node_1 = Node(1)
print(node_1)
node_2 = Node(2, node_1)
print(node_2.next)

class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase

        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        self.assertIsNone(node_1.next)  # TODO с помощью метода assertIsNone проверить следующий узел


    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        self.assertEqual(node_2.next, node_1)  # TODO проверить что узлы связались

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        self.assertEqual(print(repr(node_1)), print(node_1))  # TODO проверить метод __repr__ без следующего узла

    @unittest.skip  # TODO пропустить тест с помощью декоратора unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""


    def test_str(self):
        some_value = 5
        node = Node(some_value)

        # TODO проверить строковое представление

        self.assertEqual(print(repr(node)), print(node))

    def test_is_valid(self):
        self.assertRaises(TypeError, Node(), 1, 5)



if __name__ == '__main__':
    unittest.main()
