class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, item):
        node = LinkedListNode(item)
        node.next_node = None
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
        self.length += 1

    def insert(self, index, item):
        new_node = LinkedListNode(item)

        last = None
        for i, node in enumerate(self.get_nodes()):
            if i == index:
                if last == None:
                    self.head = new_node
                else:
                    last.next_node = new_node

                new_node.next_node = node
                self.length += 1
                return True
            last = node

        if index == self.length:
            if last == None:
                self.head = new_node
            else:
                last.next_node = new_node

            self.length += 1
            return True

        return False

    def __iter__(self):
        return self.get_items()

    def get_items(self):
        for node in self.get_nodes():
            yield node.item

    def get_nodes(self):
        current = self.head
        while current != None:
            yield current
            current = current.next_node

    def __str__(self):
        s = "["
        for i, node in enumerate(self.get_nodes()):
            if i != 0:
                s += ","
            s += str(node.item)
        s += "]"
        return s

    def remove(self, item):
        last = None
        for node in self.get_nodes():
            if node.item == item:
                if last == None:
                    self.head = node.next_node
                else:
                    last.next_node = node.next_node
                self.length -= 1
                return True
            last = node
        return False

class LinkedListNode:
    def __init__(self, item):
        self.item = item
        self.next_node = None
