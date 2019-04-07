class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        secret_dict = {}
        guess_dict = {}


        if not secret or not guess:
            return ''

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] not in secret_dict:
                    secret_dict[secret[i]] = 1
                else:
                    secret_dict[secret[i]] += 1

                if guess[i] not in guess_dict:
                    guess_dict[guess[i]] = 1
                else:
                    guess_dict[guess[i]] += 1

        num = 0
        for key in guess_dict.keys():
            if key in secret_dict:
                num += min(guess_dict[key], secret_dict[key])

        return str(bull) + 'A' + str(num) + 'B'

if __name__ == '__main__':
    so =  Solution()
    print so.getHint('1123', '0111')