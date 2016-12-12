class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_element(self, data):
        if not self.head:
            self.head = data
            self.tail = self.head
        elif self.tail == self.head:
            self.tail = data
            self.head.next = self.tail
        else:
            curr_node = data
            self.tail.next = curr_node
            self.tail = curr_node

    def __get_node(self, index):
        curr_node = self.head
        counter = 0
        while curr_node:
            if counter == index:
                return curr_node
            curr_node = curr_node.next
            counter += 1

    def index(self, index):
        return self.__get_node(index)

    def size(self):
        curr_node = self.head
        if not curr_node:
            size = 1
        else:
            size = 0
        while curr_node:
            curr_node = curr_node.next
            size += 1
        return size

    def remove(self, index):
        self.__get_node(index - 1).next = self.__get_node(index + 1)

    def pprint(self):
        if self.head is None:
            return "[]"
        res = "["
        cur_node = self.head
        while cur_node:
            res = str(cur_node.data) + "->"
            cur_node = cur_node.next
        return res + str(cur_node.data)

    def to_list(self):
        list_ll = []
        cur_node = self.head
        while cur_node:
            list_ll.append(cur_node.data)
            cur_node = cur_node.next
        return list_ll

    def add_at_index(self, index, data):
        data.next = self.index(index + 1)
        self.index(index - 1).next = data

    def add_first(self, data):
        data.next = self.head
        self.head = data

    def add_list(self, list_1):
        for i in list_1:
            self.tail.next = Node(i)
            self.tail = Node(i)

    def add_linked_list(self, ll):
        current_node = ll.head
        while current_node:
            self.tail.next = current_node
            self.tail = current_node
            current_node = current_node.next

    def ll_from_to(self, start_index, end_index):
        start_el = self.index(start_index)
        end_el = self.index(end_index)
        ll = LinkedList()
        while start_el.next != end_el.next:
            ll.add_element(start_el)
            start_el = start_el.next
        return ll

    def pop(self):
        curr_node = self.head
        while curr_node:
            curr_node = curr_node.next
        self.remove(curr_node)
        return curr_node

    # def reduce_to_unique(self):
    #     curr_node = self.head
    #     while curr_node:
