from btree import BinaryTreeNode, traverse_inorder, do_print

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if self.root == None:
            self.root = BinaryTreeNode(item)
        else:
            parent = None
            current = self.root
            path = None
            while current != None:
                parent = current
                if item < current.item:
                    current = current.left
                    path = 0
                elif item > current.item:
                    current = current.right
                    path = 1

            node = BinaryTreeNode(item)
            if path == 0:
                parent.left = node
            else:
                parent.right = node

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(1)
    bst.insert(2)
    bst.insert(11)
    bst.insert(12)
    bst.insert(13)
    bst.insert(3)
    traverse_inorder(bst.root, do_print)
