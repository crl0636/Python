class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        results = []
        dict = {}

        if not nums1 or not nums2:
            return []

        for num in nums1:
            dict[num] = dict.get(num, 0) + 1

        for num in nums2:
            if num in dict and dict[num] != 0:
                results.append(num)
                dict[num] -= 1

        return results