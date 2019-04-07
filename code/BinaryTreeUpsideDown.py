"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here

        return self.helper(root, None)

    def helper(self, p, parent):
        if not p:
            return parent

        root = self.helper(p.left, p)
        if parent:
            p.left = parent.right
        else:
            p.left = None

        p.right = parent

        return root

    def upsideDownBinaryTree2(self, root):
        if not root or not root.left:
            return root

        new_root = self.upsideDownBinaryTree2(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return new_root