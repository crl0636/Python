class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        for i in range(1, len(num) - 1):
            first = num[:i]
            if len(first) > 1 and first[0] == '0':
                continue
            for j in range(i + 1, len(num)):
                second = num[i:j]
                third = num[j:]
                # print first + " a" + second + " b" + third
                if (len(second) > 1 and second[0] == '0') or (len(third) > 1 and third[0] == '0'):
                    continue
                elif int(first) + int(second) == int(third):
                    return True
                elif self.checkValid(first, second, third):
                    if True and self.isAdditiveNumber(num[i:]):
                        return True
        return False

    def checkValid(self, one, two, three):
        return three.startswith(str(int(one) + int(two)))

if __name__ == '__main__':
    so = Solution()
    print so.isAdditiveNumber('1023')