# Definition for binary tree with next pointer.
import collections
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):

        if not root:
            return None

        root.next = None

        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                root_ = queue.popleft()
                level.append(root_)
                if root_.left:
                    queue.append(root_.left)
                if root_.right:
                    queue.append(root_.right)

            for i in range(len(level) - 1):
                level[i].next = level[i + 1]