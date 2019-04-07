class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ''
        list = []
        for i in xrange(0, len(s), 2 * k):
            sub_str = s[i:i + 2 * k]
            list.append(sub_str)

        for item in list:
            if 2 * k >= len(item) > k:
                item = item[:k][::-1] + item[k:]
            else:
                item = item[::-1]
            result += item
        return result

if __name__ == '__main__':
    so =Solution()
    print so.reverseStr('abcdefg',2)