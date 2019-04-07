class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ['a', 'o', 'e', 'u', 'i', 'A', 'O', 'E', 'U', 'I']
        s = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

            if s[start] not in vowels:
                start += 1

            if s[end] not in vowels:
                end -= 1

        return ''.join(s)

if __name__ == '__main__':
    solution = Solution()
    print solution.reverseVowels('A man, a plan, a canal: Panama')