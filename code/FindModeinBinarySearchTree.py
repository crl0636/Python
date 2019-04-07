# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        dict = {}

        self.helper(root, 0, res)
        for items in res:
            for item in items:
                if item not in dict:
                    dict[item] = 1
                else:
                    dict[item] += 1

        max_num = max(dict.values())
        return [key for key, value in dict.iteritems() if value == max_num]

    def helper(self, root, level, res):
        """

                :type root:  TreeNode
                :param level:
                :TreeNode res: List[List[int]]
                :return:
                """
        if root:
            if len(res) < level + 1:
                res.append([])

            res[level].append(root.val)
            self.helper(root.left, level + 1, res)
            self.helper(root.right, level + 1, res)

if __name__ == '__main__':
    so = Solution()
    so.findMode([1,None,2,2])