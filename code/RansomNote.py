class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_dict = {}
        magazine_dict = {}

        if len(magazine) < len(ransomNote):
            return False

        for letter in ransomNote:
            if letter not in ransomNote_dict:
                ransomNote_dict[letter] = 1
            else:
                ransomNote_dict[letter] += 1

        for letter in magazine:
            if letter not in magazine_dict:
                magazine_dict[letter] = 1
            else:
                magazine_dict[letter] += 1

        result = True
        for letter in ransomNote:
            if letter not in magazine_dict:
                return False
            else:
                result = True if ransomNote_dict[letter] <= magazine_dict[letter] else False
            if not result:
                break
        return result

if __name__ == "__main__":
    solution = Solution()
    solution.canConstruct('fihjjjjei', 'hjibagacbhadfaefdjaeaebgi')
