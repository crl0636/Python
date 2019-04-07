class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if offset == 0:
            return str

        return str[-offset:] + str[:-offset]

if __name__ == '__main__':
    solution = Solution()
    print solution.rotateString('abcdefg', 3)