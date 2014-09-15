from linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.llist = LinkedList()

    def enqueue(self, item):
        self.llist.append(item)

    def dequeue(self):
        item = iter(self.llist).next()
        self.llist.remove(item)
        return item
