class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_len = min([len(x) for x in strs])

        while min_len > 0:
            prefix = set([x[:min_len] for x in strs])

            if len(prefix) == 1:
                return strs[0][:min_len]
            else:
                min_len -= 1
        return ""

