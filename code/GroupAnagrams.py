class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}

        for str in strs:
            s = ''.join(sorted(str))
            if s in dict:
                dict[s] += [str]
            else:
                dict[s] = [str]
        return list(dict.values())

if __name__ == '__main__':
    so = Solution()
    so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])