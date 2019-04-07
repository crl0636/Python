# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
         """
         Initializes an iterator object to the beginning of a list.
         :type nums: List[int]
         """

    def hasNext(self):
         """
         Returns true if the iteration has more elements.
         :rtype: bool
         """

    def next(self):
        """
         Returns the next element in the iteration.
         :rtype: int
         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.flag = False
        self.element = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.flag:
            self.element = self.iterator.next()
            self.flag = True

        return self.element

    def next(self):
        """
        :rtype: int
        """
        if not self.flag:
            return self.iterator.next()

        element = self.element
        self.flag = False
        self.element = None
        return element

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.flag or self.iterator.hasNext()