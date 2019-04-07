class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        index1 = m-1
        index2 = n-1
        index3 = m+n-1

        while index3 >=0 and index1 >=0 and index2 >=0:
            if nums1[index1] > nums2[index2]:
                nums1[index3] = nums1[index1]
                index1 -= 1
            else:
                nums1[index3] = nums2[index2]
                index2 -= 1

            index3 -= 1

        if index2 >= 0:
            nums1[: index2 + 1] = nums2[: index2 + 1]