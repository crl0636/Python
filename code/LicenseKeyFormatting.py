class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        S = S.replace('-','').upper()
        res = []
        for i in range(len(S), 0, -K):
            if i-K < 0:
                res.append(S[:i])
            else:
                res.append(S[i-K:i])
        return '-'.join(res[::-1])

if __name__ == '__main__':
    so = Solution()
    print so.licenseKeyFormatting("5F3Z-2e-9-w", 4)
    print so.licenseKeyFormatting("2-5g-3-J", 2)

