class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:

    def __init__(self):
        self.top_node = None

    def __str__(self):
        next_node = self.top_node
        stack_str = ''
        while next_node is not None:
            stack_str += str(next_node.value) + " "
            next_node = next_node.next

        return stack_str

    def push(self, value):
        new_top_node = Node(value, self.top_node)
        self.top_node = new_top_node

    def pop(self):
        try:
            if self.top_node.value is not None:
                poped_value = self.top_node.value
                next_node = self.top_node.next
                self.top_node = next_node
                print("this is the poped item:" + str(poped_value))
                return poped_value
        except AttributeError:
            raise Exception('Your list is empty.')

    def find(self, value):
        find_node = self.top_node
        while find_node is not None:
            if find_node.value == value:
                return True
            find_node = find_node.next
        raise Exception("No value has been found.")
        return False

    def count(self):

        count_nodes = 0
        current_node = self.top_node
        while current_node:
            count_nodes += 1
            current_node = current_node.next
        print("You have " + str(current_node) + " items in the list.")
        return count_nodes

    def is_empty(self):
        return self.top_node is not None

    def getmin(self):
        if self.top_node is None:
            raise Exception("Your Stack is empty.")
        min = self.top_node
        current_node = self.top_node
        while current_node is not None:
            if current_node.value < min.value:
                min = current_node
            current_node = current_node.next
        return min