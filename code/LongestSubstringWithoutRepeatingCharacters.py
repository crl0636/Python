class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        hash_set = set()
        j = 0
        for i in range(len(s)):
            if s[i] in hash_set:
                j += 1
                hash_set.remove(s[j])
            else:
                hash_set.add(s[i])
                res = max(res, len(hash_set))
        return res

if __name__ == '__main__':
    so = Solution()
    so.lengthOfLongestSubstring('abcabcbb')