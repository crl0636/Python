class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        results = set()
        if not nums1 or not nums2:
            return []
        for num in nums2:
            if num in nums1:
                results.add(num)

        return list(results)