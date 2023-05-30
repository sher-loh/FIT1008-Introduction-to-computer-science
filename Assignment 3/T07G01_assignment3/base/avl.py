""" avl.py: Contains the class AVLTree """
__author__ = "Abdul Harith Abdul Halim, Nurin Damia, Loh Jing Wei, Chen Xin Hui"
""" AVL Tree implemented on top of the standard BST. """

__author__ = 'Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from bst import BinarySearchTree
from typing import TypeVar, Generic
from node import AVLTreeNode

K = TypeVar('K')
I = TypeVar('I')


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ Self-balancing binary search tree using rebalancing by sub-tree
        rotations of Adelson-Velsky and Landis (AVL).
    """

    def __init__(self) -> None:
        """
        Initialises an empty Binary Search Tree
        :complexity: O(1)
        """
        BinarySearchTree.__init__(self)

    def get_height(self, current: AVLTreeNode) -> int:
        """
        Get the height of a node. Return current.height if current is
        not None. Otherwise, return 0.
        :complexity: O(1)
        """
        if current is not None:
            return current.height
        return 0

    def get_balance(self, current: AVLTreeNode) -> int:
        """
        Compute the balance factor for the current sub-tree as the value
        (right.height - left.height). If current is None, return 0.
        :complexity: O(1)
        """
        if current is None:
            return 0
        return self.get_height(current.right) - self.get_height(current.left)

    def insert_aux(self, current: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
         A method to insert an item into the tree
         Approach : which uses the Key to insert it.After insertion, performs sub-tree rotation whenever it becomes
                    unbalanced and returns the new root of the subtree.
         :param self:
         :param current:
         :param key:
         :param item:
         :returns: the new root of a tree post insertion of an item via a key
         complexity: best = worst = O(log(n)), n is the number of nodes in tree
         pre-condition: key does not exist in tree (no duplicate)
         post-condition: All nodes on right subtree of the inserted tree node has a bigger key whereas
                         all nodes on left subtree of the inserted tree node has a smaller key.
         invariant: Nodes on current's left subtree has smaller key than current.key and
                    nodes on current's right subtree has bigger key than current.key
         """
        acceptable_difference = {-1, 0, 1}
        # Find the correct location and insert the node
        if current is None:
            current = AVLTreeNode(key, item)
            self.length += 1
            current.right_count = 0
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right_count += 1
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')

        # update the height
        current.height = 1 + max(self.get_height(current.left),
                                 self.get_height(current.right))

        # Update the balance factor and attempt to balance the tree via rebalance function
        balance = self.get_balance(current)
        if balance not in acceptable_difference:
            current = self.rebalance(current)

        return current

    def delete_aux(self, current: AVLTreeNode, key: K) -> AVLTreeNode:
        """
        A method  to delete an item from the tree
        Approach : it uses the Key to determine the node to delete. After deletion,
                   performs sub-tree rotation whenever it becomes unbalanced.
                   returns the new root of the subtree.
        :param self:
        :param current:
        :param key:
        :returns: the new root of a tree post deletion of an item via a key
        complexity: best = worst = O(log(n)), n is the number of nodes in tree
        pre-condition: key can be found in tree
        post-condition: node with key is removed from tree
        invariant: Nodes on current's left subtree has smaller key than current.key and
                   nodes on current's right subtree has bigger key than current.key
        """
        acceptable_difference = {-1, 0, 1}

        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right_count -= 1
            current.right = self.delete_aux(current.right, key)
        else:  # we found our key => do actual deletion (key == current.key)
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
            current.right_count -= 1
            current.key = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

        # update the height
        current.height = 1 + max(self.get_height(current.left),
                                 self.get_height(current.right))

        # Update the balance factor and attempt to balance the tree via rebalance function
        balance = self.get_balance(current)
        if balance not in acceptable_difference:
            current = self.rebalance(current)

        return current

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
        Perform left rotation of the sub-tree.
        Right child of the current node, i.e. of the root of the target
        sub-tree, should become the new root of the sub-tree.
        returns the new root of the subtree.
        Example:

             current                                       child
            /       \                                      /   \
        l-tree     child           -------->        current     r-tree
                  /     \                           /     \
             center     r-tree                 l-tree     center

        complexity: O(1)
        pre-condition: current is a node in AVL tree
        post-condition: current subtree is rotated to the left
        """
        # Store temporary variable
        r_child = current.right
        c_tree = r_child.left

        # Rotation
        current.right_count = current.right_count - (r_child.right_count + 1)
        current.right = c_tree
        r_child.left = current

        # Update heights
        current.height = 1 + max(self.get_height(current.left),
                                 self.get_height(current.right))
        r_child.height = 1 + max(self.get_height(r_child.left),
                                 self.get_height(r_child.right))

        # Return the new root
        return r_child

    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
        Perform right rotation of the sub-tree.
        Left child of the current node, i.e. of the root of the target
        sub-tree, should become the new root of the sub-tree.
        returns the new root of the subtree.

        Example:

                   current                                child
                  /       \                              /     \
              child       r-tree     --------->     l-tree     current
             /     \                                           /     \
        l-tree     center                                 center     r-tree

        complexity: O(1)
        pre-condition: current is a node in AVL tree
        post-condition: current subtree is rotated to the right
        """

        # Temporary variable
        i_child = current.left
        c_tree = i_child.right

        # Rotation
        i_child.right_count = i_child.right_count + current.right_count + 1
        current.left = c_tree
        i_child.right = current

        # Update heights
        current.height = 1 + max(self.get_height(current.left),
                                 self.get_height(current.right))
        i_child.height = 1 + max(self.get_height(i_child.left),
                                 self.get_height(i_child.right))

        # Return the new root
        return i_child

    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate
            returns the new root of the subtree.
        """
        if self.get_balance(current) >= 2:
            child = current.right
            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)
            return self.left_rotate(current)

        if self.get_balance(current) <= -2:
            child = current.left
            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)
            return self.right_rotate(current)

        return current

    def kth_largest(self, k: int) -> AVLTreeNode:
        """
        A method that returns the kth largest element in the tree.
        k = 1 would return the largest.
        :param self
        :param k:
        :returns : Returns the kth largest element in the tree
        complexity: O(log(n)), n is total number of nodes in the tree
        pre-condition: k is an integer greater than or equal to 1
        post-condition: function will return a node that is kth largest in tree
        """
        return self.kth_largest_aux(k, self.root)

    def kth_largest_aux(self, k: int, current: AVLTreeNode):
        """
        An auxiliary method to find the kth largest element in the tree.
        Approach : From the property of BST, we know that any node stored in right subtree of a
                   particular node is larger than the particular node.
                   From the property of BST, we know that any node stored in the right subtree of a particular
                   node is larger than the particular node. Using the count of the nodes on the
                   right subtree of a particular node (right_count),we can rank this particular node.
                   For example, if there are 7 nodes on the right subtree of the node,the node is 8th largest.
                   Hence, to find the kth largest node, this node would have a right_count of k-1.
                   When k == (current.right_count + 1),we will return the current node which is kth largest
                   in the AVL tree.
                   When k < (current.right_count + 1),the current node has a smaller key than the kth
                   largest node we are finding.
                   (In other words, the current node has a greater rank than the kth largest node).
                   We will search recursively for the nodes on the current node’s right subtree.
                   When k > (current.right_count + 1),the current node has a greater key than the kth largest
                   node we are finding.
                   We will search recursively for the nodes on the current node’s left subtree.
                   Before we do the searching, we will compute the k again by doing k = k - (current.right_count + 1) to
                   find the rank of kth largest node within the left subtree.
                   This is because there are (current.right_count + 1) nodes greater than those in the left subtree
                   (number of nodes of current’s right subtree plus one which is the current node itself).

        :param self:
        :param k:
        :param current:
        :returns : Returns the kth largest node in the tree
        complexity: O(log(n)),  n is total number of nodes in the tree
        pre-condition: k is an integer greater than or equal to 1
        post-condition: returned node is kth largest in tree
        invariant: when k < (current.right_count + 1), kth largest node is in right subtree of current node
                   when k > (current.right_count + 1), kth largest node is in left subtree of current node
        """
        if current is None:
            raise ValueError("Node not found")
        if k == (current.right_count + 1):
            return current
        elif k < (current.right_count + 1):
            return self.kth_largest_aux(k, current.right)
        else:
            k = k - (current.right_count + 1)
            return self.kth_largest_aux(k, current.left)
