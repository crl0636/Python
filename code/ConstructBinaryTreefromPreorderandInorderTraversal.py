# Definition for a binary tree node.
class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        preorder:[3,9,20,15,7]
        inorder:[9,3,15,20,7]
        """

        if not inorder:
            return None

        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+pos], inorder[:pos])
        root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
        return root