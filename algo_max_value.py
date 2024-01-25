class Node:
    """Class that represents a node in the Binary Search Tree."""
    
    def __init__(self, key):
        """
        Initializing a new node.

        Parameters:
        key (int): a key or value stored in the HEI.
        """
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """
    Function for inserting a new node with the specified key into the Binary Search Tree.

    Parameters:
    root (Node): the root node of the tree.
    key (int): the node key to insert.

    Returns:
    Node: the root node of the tree after inserting a new node.
    """
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def max_value_node(node):
    """
    Function for finding the node with the highest value in the Binary Search Tree.

    Parameters:
    node: the node where the search starts.

    Returns:
    Node: the node with the highest value in the tree.
    """
    current = node
    while current.right:
        current = current.right
    return current

# Creating a tree root and adding multiple nodes
root = Node(10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 2)
root = insert(root, 12)
root = insert(root, 18)

# Calling a function to find the smallest value
min_node = max_value_node(root)
print("Highest value in the tree:", min_node.val)
