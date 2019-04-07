# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if nums is None:
            return None

        root = self.binary_search(nums, 0, len(nums) -1)
        return root

    def binary_search(self, nums, low, high):
        if high < low:
            return None

        mid = (low + high)/2

        root = TreeNode(nums[mid])
        root.left = self.binary_search(nums, low, mid-1)
        root.right = self.binary_search(nums, mid + 1, high)

        return root
