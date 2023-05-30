"""bst.py: Contains the class BSTInOrderIterator."""
from __future__ import annotations

__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"
""" Binary Search Tree ADT.
    Defines a Binary Search Tree with linked nodes.
    Each node contains a key and item as well as references to the children.
"""

__author__ = 'Brendon Taylor, modified by Alexey Ignatiev and Jackson Goerner'
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic
from linked_stack import LinkedStack
from node import TreeNode
import sys


# generic types
K = TypeVar('K')
I = TypeVar('I')
T = TypeVar('T')


class BSTInOrderIterator:
    """ In-order iterator for the binary search tree.
        Performs stack-based BST traversal.
    """

    def __init__(self, root: TreeNode[K, I]) -> None:
        """ Iterator initialiser. """

        self.stack = LinkedStack()
        self.current = root

    def __iter__(self) -> BSTInOrderIterator:
        """ Standard __iter__() method for initialisers. Returns itself. """

        return self

    def __next__(self) -> K:
        """ The main body of the iterator.
            Returns keys of the BST one by one respecting the in-order.
        """

        while self.current:
            self.stack.push(self.current)
            self.current = self.current.left

        if self.stack.is_empty():
            raise StopIteration

        result = self.stack.pop()
        self.current = result.right

        return result.key


class BinarySearchTree(Generic[K, I]):
    """ Basic binary search tree. """

    def __init__(self) -> None:
        """
        Initialises an empty Binary Search Tree
        :complexity: O(1)
        """

        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
        Checks to see if the bst is empty
        :complexity: O(1)
        """
        return self.root is None

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: K) -> bool:
        """
        Checks to see if the key is in the BST
        :complexity: see __getitem__(self, key: K) -> (K, I)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __iter__(self) -> BSTInOrderIterator:
        """ Create an in-order iterator. """
        return BSTInOrderIterator(self.root)

    def __getitem__(self, key: K) -> I:
        """
        Attempts to get an item in the tree, it uses the Key to attempt to find it
        :complexity best: O(CompK) finds the item in the root of the tree
        :complexity worst: O(CompK * D) item is not found, where D is the depth of the tree
        CompK is the complexity of comparing the keys
        """
        return self.get_tree_node_by_key(key).item

    def get_tree_node_by_key(self, key: K) -> TreeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: TreeNode, key: K) -> TreeNode:
        if current is None:  # base case: empty
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:  # base case: found
            return current
        elif key < current.key:
            return self.get_tree_node_by_key_aux(current.left, key)
        else:  # key > current.key
            return self.get_tree_node_by_key_aux(current.right, key)

    def getitem_aux(self, current: TreeNode, key: K) -> I:
        if current is None:  # base case: empty
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:  # base case: found
            return current.item
        elif key < current.key:
            return self.getitem_aux(current.left, key)
        else:  # key > current.key
            return self.getitem_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: TreeNode, key: K, item: I) -> TreeNode:
        """
        Attempts to insert an item into the tree, it uses the Key to insert it
        :complexity best: O(CompK) inserts the item at the root.
        :complexity worst: O(CompK * D) inserting at the bottom of the tree
        where D is the depth of the tree
        CompK is the complexity of comparing the keys
        """
        if current is None:  # base case: at the leaf
            current = TreeNode(key, item)
            self.length += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        return current

    def __delitem__(self, key: K) -> None:
        self.root = self.delete_aux(self.root, key)

    def delete_aux(self, current: TreeNode, key: K) -> TreeNode:
        """
        Attempts to delete an item from the tree, it uses the Key to
        determine the node to delete.
        """

        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left  = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            # general case => find a successor
            succ = self.get_successor(current)
            current.key  = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

        return current

    def get_successor(self, current: TreeNode) -> TreeNode:
        """
        Get successor of the current node.
        It should be a child node having the smallest key among all the
        larger keys.
        Approach: To find the successor, we need to go to the right of current(node) first,
                  because the right of current is larger than current.
                  Then traverse the node from the right of current(current.right)
                  to the left recursively until the left is none. Hence, get_minimal() is used to traverse.
                  This node that which is the minimal node but larger than current is the successor node.
        :param self:
        :param current:
        :return: Returns the successor of the current node
        complexity: O(n), n is the height of the tree
        pre-condition: current is a node of the tree
        post-condition: returned node is the successor of current
        """
        if current.right is None:
            return None
        else:
            return self.get_minimal(current.right)

    def get_minimal(self, current: TreeNode) -> TreeNode:
        """
        Get a node having the smallest key in the current sub-tree.
        Approach: Traverse the node from the current(node) to the left recursively until the left is none,
                  because the left of current is smaller than current.
                  Therefore, this node that the left is none is the minimal node.
        :param self:
        :param current:
        :return: Returns the smallest node in the current sub-tree
        complexity: O(n), n is the height of tree
        pre-condition: current is the node of the tree
        post-condition: returned node is the node with the smallest key
        """
        minimal = current
        if current is not None:
            if current.left is not None:
                minimal = self.get_minimal(current.left)
        return minimal

    def is_leaf(self, current: TreeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """

        return current.left is None and current.right is None

    def draw(self, to=sys.stdout):
        """ Draw the tree in the terminal. """

        # get the nodes of the graph to draw recursively
        self.draw_aux(self.root, prefix='', final='', to=to)

    def draw_aux(self, current: TreeNode, prefix='', final='', to=sys.stdout) -> K:
        """ Draw a node and then its children. """

        if current is not None:
            real_prefix = prefix[:-2] + final
            print('{0}{1}'.format(real_prefix, str(current.key)), file=to)

            if current.left or current.right:
                self.draw_aux(current.left,  prefix=prefix + '\u2551 ', final='\u255f\u2500', to=to)
                self.draw_aux(current.right, prefix=prefix + '  ', final='\u2559\u2500', to=to)
        else:
            real_prefix = prefix[:-2] + final
            print('{0}'.format(real_prefix), file=to)