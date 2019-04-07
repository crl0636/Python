class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}

        for i in range(len(s)):
            character_s = s[i]
            character_t = t[i]

            if character_s in dict:
                if dict[character_s] == character_t:
                    continue
                else:
                    return False
            else:
                if not character_t in dict.values():
                    dict[character_s] = character_t
                else:
                    return False


        return True