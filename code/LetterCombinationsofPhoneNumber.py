class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.dict = {
            '2':'abc', '3':'def', '4':'ghi',
            '5':'jkl', '6':'mno', '7':'pqrs',
            '8':'tuv', '9':'wxyz'
        }
        res = []
        if not digits:
            return res
        self.helper(digits, '', res)
        return res

    def helper(self, digits, path, res):
        """

        :type root:
        :param path:
        :type res: List[str]
        :return:
        """
        if not digits:
            res.append(path)
            return

        for letter in self.dict[digits[0]]:
            self.helper(digits[1:], path + letter, res)