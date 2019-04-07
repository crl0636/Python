class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0

        digits.insert(0,1)
        return digits

    def plusone(self, digits):
        value = ''.join(str(i) for i in [1,2,3,5])
        num_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                    '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        res = 0
        for i in value:
            res = 10 * res + num_dict[i]
        res = res + 1
        ans = []
        for i in str(res):
            ans.append(i)
        return ans

if __name__ == '__main__':
    so =Solution()
    print so.plusone([1,2,3,5])