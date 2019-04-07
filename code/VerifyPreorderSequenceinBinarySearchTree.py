class Solution:
    """
    @param preorder: List[int]
    @return: return a boolean
    """
    def verifyPreorder(self, preorder):
        # write your code here
        ans = []

        min = float('-inf')
        for i in preorder:
            if i < min:
                return False
            while len(ans) > 0 and ans[-1] < i:
                min = ans.pop()
            ans.append(i)
        return True


if __name__ == '__main__':
    so = Solution()
    print so.verifyPreorder([1, 3, 2])