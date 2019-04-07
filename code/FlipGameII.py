class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def canWin(self, s):
        # write your code here

        if not s:
            return False

        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                tmp  = s[:i] + '--' + s[i+2]

                res = self.canWin(tmp)

                if not res:
                    return True
        return False