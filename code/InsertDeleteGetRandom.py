import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set_obj = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.set_obj:
            self.set_obj.add(val)
            return True

        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val in self.set_obj:
            self.set_obj.remove(val)
            return True

        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.sample(self.set_obj(), 1).pop()