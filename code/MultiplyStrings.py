class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = self.covert_str_num(num1)
        n2 = self.covert_str_num(num2)

        return str(n1 * n2)

    def covert_str_num(self, num):
        num_dict = {'1':1, '2':2, '3':3, '4':4, '5':5,
                    '6':6, '7':7, '8':8, '9':9, '0':0}

        res = 0
        for i in num:
            res = res * 10 + num_dict[i]
        return res

if __name__ ==  '__main__':
    so = Solution()
    print so.multiply('123','234')