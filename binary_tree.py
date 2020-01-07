"""
Author: Kara Meyer
Date: 11-11-2019
Description: Using this program you can create and alter a binary tree.
"""


class node:
    """Node of a binary tree."""

    def __init__(self, data=None):
        """Define how to make a node."""
        self.data = data
        self.left = None
        self.right = None


class binary_tree:
    """Ways to alter the binary tree."""

    head = None

    def __init__(self, data=None):
        """Initialize the tree."""
        self.head = node(data)

    def add_branch(self, parent_data, left_data, right_data):
        """Add a left and right node to the tree."""
        parent_node = self._find_node(parent_data)
        if parent_node is not None:
            parent_node.left = node(left_data)
            parent_node.right = node(right_data)
        else:
            print("The node " + str(parent_data) + " does not exist.")

    def print_tree(self):
        """Print the tree."""
        print(self._print_tree_data(self.head, ""))

    def tree_height(self):
        """Find the height of the tree."""
        height = self._tree_height_data(self.head)
        return height

    def _find_node(self, node_data):
        """Takes node data and returns the node with that data."""
        found_node = self._find_node_data(node_data, self.head)
        return found_node

    def _find_node_data(self, node_data, current_node, found_node=None):
        """Find a node in the tree for the find_node function."""
        if found_node is not None:
            return found_node

        if current_node is None:
            return None

        if current_node.data == node_data:
            found_node = current_node

        found_node = self._find_node_data(node_data, current_node.left, found_node)
        found_node = self._find_node_data(node_data, current_node.right, found_node)
        return found_node

    def _print_tree_data(self, current_node, tree_values):
        """Find the string for the print_tree function."""
        if current_node is not None:
            tree_values += str(current_node.data) + " - "
            tree_values = self._print_tree_data(current_node.left, tree_values)
            tree_values = self._print_tree_data(current_node.right, tree_values)
        return tree_values

    def _tree_height_data(self, current_node):
        """Find the height of the tree for the tree_height function."""
        if current_node is None:
            return 0

        else:
            left_height = self._tree_height_data(current_node.left)
            right_height = self._tree_height_data(current_node.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
