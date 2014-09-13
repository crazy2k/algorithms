class LinkedListNode:
    def __init__(self, item):
        self.item = item
        self.next_node = null

def remove_nodes(head, item):
    last = head
    current = head
    while current != null:
        if current.item == item:
            if last != current:
                last.next_node = current.next_node
                current = last.next_node
            else:
                head = current.next_node
                last = current = head
        else:
            last = current
            current = current.next_node

def print_list(head):
    current = head
    while current != null:
        print current.item
        current = current.next_node
