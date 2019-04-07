import collections
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue  = collections.deque()
        self.helper(nestedList)

    def helper(self, nestedList):
        for i in len(nestedList):
            if nestedList[i].isInteger():
                self.queue.append(nestedList[i])
            else:
                self.helper(nestedList[i].getList())


    def next(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.popleft()


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0