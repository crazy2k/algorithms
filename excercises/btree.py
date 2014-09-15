class BinaryTreeNode:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

def traverse_inorder(root, func):
    if root.left:
        traverse_inorder(root.left, func)
    func(root.item)
    if root.right:
        traverse_inorder(root.right, func)

def traverse_preorder(root, func):
    func(root.item)
    if root.left:
        traverse_preorder(root.left, func)
    if root.right:
        traverse_preorder(root.right, func)

def traverse_postorder(root, func):
    if root.left:
        traverse_postorder(root.left, func)
    if root.right:
        traverse_postorder(root.right, func)
    func(root.item)

def do_print(s):
        print s

if __name__ == "__main__":
    #               1
    #       2               3
    #   4       5
    one = BinaryTreeNode(1)
    two = BinaryTreeNode(2)
    three = BinaryTreeNode(3)
    four = BinaryTreeNode(4)
    five = BinaryTreeNode(5)
    one.left = two
    one.right = three
    two.left = four
    two.right = five

    print "In-order:"
    traverse_inorder(one, do_print)

    print "Pre-order:"
    traverse_preorder(one, do_print)

    print "Post-order:"
    traverse_postorder(one, do_print)
