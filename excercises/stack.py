from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.llist = LinkedList()

    def push(self, item):
        self.llist.insert(0, item)

    def pop(self):
        item = iter(self.llist).next()
        self.llist.remove(item)
        return item
