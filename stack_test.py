import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_str(self):
        self.assertEqual(self.stack.__str__(), '')
        self.stack.push(1)
        self.assertEqual(self.stack.__str__(), '1 ')
        self.stack.push(3)
        self.assertEqual(self.stack.__str__(), '3 1 ')


    def test_push(self):
        with self.assertRaisesRegex(Exception, "No value has been found"):
            self.stack.find(1)
        self.stack.push(1)
        self.assertEqual(self.stack.find(1), True)
        self.stack.push(2)
        self.assertEqual(self.stack.find(2), True)
        self.assertEqual(self.stack.count(), 2)


    def test_pop(self):
        with self.assertRaisesRegex(Exception, "Your list is empty."):
            self.stack.pop()
        self.stack.push(1)
        self.assertEqual(self.stack.find(1), True)
        self.stack.pop()
        with self.assertRaisesRegex(Exception, "No value has been found."):
            self.stack.find(1)

    def test_find(self):
        with self.assertRaisesRegex(Exception, "No value has been found."):
            self.stack.find(1)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.find(1), True)
        self.assertEqual(self.stack.find(2), True)
        with self.assertRaisesRegex(Exception, "No value has been found."):
            self.stack.find(3)


    def test_count(self):
        self.assertEqual(self.stack.count(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.count(), 1)
        self.stack.push(1)
        self.assertEqual(self.stack.count(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.count(), 1)



    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)

    def test_getmin(self):
        with self.assertRaisesRegex(Exception, "Your Stack is empty."):
            self.stack.getmin()
        self.stack.push(2)
        self.assertEqual(self.stack.getmin(), 2)
        self.stack.push(1)
        self.assertEqual(self.stack.getmin(), 1)
        self.stack.push(0)
        self.assertEqual(self.stack.getmin(), 0)