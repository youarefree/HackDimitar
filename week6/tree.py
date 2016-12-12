import deque


class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.children = []

    def not_empty(self):
        return self.children != []


class Tree:
    def __init__(self, root):
        self.root = root
        self.counter = 1
        # tree_list = []

    def walk(self, node):
        return [self.root] + self.concat([self.walk(child) for child in self.root.children])

    def concat(xs):
        result = []
        for x in xs:
            result.append(x)
            return result

    def add_child(self, root, parent_value, child_value):
        stop_recursion = False
        root = self.root

        def inner_recursion(root, parent_value, child_value):

            if stop_recursion:
                return

        if root.value == parent_value:
            root.children.append(Node(child_value))
            stop_recursion = True
            return

        for child in root.children:
            inner_recursion(child, parent_value, child_value)

    inner_recursion(root, parent_value, child_value)


                        # def add_child_stack(self, root, value):
                        #     stack = deque()
                        #     root = self.root
                        #     stack.append(root)

                        #     while len(stack) != 0:



    def add_child(self, parent, child=None):
        n = Node(data=4, parent=parent)
        self.get_element(parent).children.append(n)
        self.counter += 1

    def get_element(self, element, start=None):
        if start is None:
            start = self.root
        if start.data == element:
            return start
        if start.not_empty():
            for i in start.children:
                return self.get_element(element, i)

    def find(self, x):
        # return True if self.get_element(x) else False
        stack = deque()
        stack.append(self.__root)

        while len(stack) != 0:
            current_node = stack.pop()

            if current_node.data == x

    def height(self, root):
        if not root.children:
            return 1
        else:
            return max(self.height(c) for c in root.children) + 1

    def count_nodes(self):
        return self.counter

    def tree_levels(self):
        pass

    def get_tree_levels(self, level, tree):
        queue = deque()
        queue.append((0, self._root))

        result = {0: [self.root.data]}

        while len(queue) != 0:
            level, current_node = queue.popleft()

            if level not in result:
                result[level] = [current_node.data]
            else:
                result[level].append(current_node.data)

            for child in current_node.children:
                queue.append((level + 1, child))

        return result





