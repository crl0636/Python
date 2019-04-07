class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        if not s:
            return []

        res = []

        left = 0
        s_list = list(s)
        while left < len(s_list) - 1:
            if s_list[left] == '+' and s_list[left] == s_list[left + 1]:
                s_list[left] = s_list[left + 1] = '-'
                res. append(s[:left] + s_list[left] + s_list[left + 1] + s[left + 2:])
                s_list[left] = s_list[left + 1] = '+'

            left += 1

        return res

if __name__ == '__main__':
    so = Solution()
    print so.generatePossibleNextMoves('---+++-+++-+')