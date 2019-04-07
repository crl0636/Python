class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict = {}

        if not list1 or not list2:
            return []

        for item in list1:
            if item in list2:
                dict[item] = list1.index(item) + list2.index(item)

        return [key for key, value in dict.iteritems() if value == min(dict.values())]