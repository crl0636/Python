class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'(':')', '{':'}', '[':']'}
        stack = []

        if not s:
            return True

        for char in s:
            if char in pairs:
                stack.append(pairs.get(char))
            else:
                if not stack or stack.pop() != char:
                    return False

        return True if len(stack) == 0 else False
