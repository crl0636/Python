class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) <= 10:
            return []

        dict = {}
        ans = []
        for i in range(len(s)):
            if s[i:i+10] in dict:
                dict[s[i:i+10]] += 1
            else:
                dict[s[i:i+10]] = 1

        for key, val in dict.iteritems():
            if val > 1:
                ans.append(key)

        return ans