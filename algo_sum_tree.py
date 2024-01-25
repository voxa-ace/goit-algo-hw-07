class Node:
    """Class that represents a node in the Binary Search Tree."""

    def __init__(self, key):
        """
        Initializing a new node.

        Parameters:
        key (int): The key or value stored in the node.
        """
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """
    Function for inserting a new node with the specified key into the Binary Search Tree.

    Parameters:
    root (Node): The root node of the tree.
    key (int): The key of the node to be inserted.

    Returns:
    Node: The root node of the tree after inserting the new node.
    """
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def sum_of_values(node):
    """
    Function to find the sum of all values in a Binary Search Tree.

    Parameters:
    node (Node): The root node of the tree.

    Returns:
    int: The sum of all values in the tree.
    """
    if node is None:
        return 0
    else:
        return node.val + sum_of_values(node.left) + sum_of_values(node.right)
