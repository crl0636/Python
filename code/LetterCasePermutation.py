class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        self.helper(ans, S, S, 0)
        return ans

    def helper(self, ans, res, S, idx):
        ans.append(res)

        for i in range(idx, len(S)):
            if 'a' <= S[i] <= 'z':
                self.helper(ans, res[:i] + S[i].upper() + res[i+1:], S, i + 1)
            elif 'A' <= S[i] <= 'Z':
                self.helper(ans, res[:i] + S[i].lower() + res[i+1:], S, i + 1)

if __name__ == '__main__':
    so = Solution()
    so.letterCasePermutation('a1b2')