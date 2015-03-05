class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = LinkedListNode(item)
        if self.head == None:
            self.head = node
        else:
            self.tail.next_node = node

        self.tail = node
        self.tail.next_node = None

    def merge(self, other):
        merged = LinkedList()

        self_node = self.head
        other_node = other.head
        while self_node != None and other_node != None:
            if self_node < other_node:
                merged.append(self_node.item)
                self_node = self_node.next_node
            else:
                merged.append(other_node.item)
                other_node = other_node.next_node

        if other_node == None:
            while self_node != None:
                merged.append(self_node.item)
                self_node = self_node.next_node
        else:
            while other_node != None:
                merged.append(other_node.item)
                other_node = other_node.next_node
        return merged

class LinkedListNode:
    def __init__(self, item):
        self.item = item
        self.next_node = None

    def __eq__(self, other):
        return self.item == other.item if other != None else False

    def __lt__(self, other):
        return self.item < other.item

    def __gt__(self, other):
        return self.item > other.item

if __name__ == "__main__":
    l1 = LinkedList()
    l1.append(1)
    l1.append(3)
    l1.append(5)
    
    l2 = LinkedList()
    l2.append(2)
    l2.append(4)
    l2.append(7)
    l2.append(8)
    l2.append(9)

    l3 = l1.merge(l2)
    node = l3.head
    while node != None:
        print node.item
        node = node.next_node
