class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        list1 = version1.split('.')
        list2 = version2.split('.')
        m, n = len(list1), len(list2)

        if m > n:
            list2 += [0] * (m - n)
        else:
            list1 += [0] * (n - m)

        for i in range(len(list1)):
            if int(list1[i]) < int(list2[i]):
                return -1
            elif int(list1[i]) > int(list2[i]):
                return 1
            else:
                continue

        return 0

if __name__ == '__main__':
    so =  Solution()
    so.compareVersion('1', '1.1')
