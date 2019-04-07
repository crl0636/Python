class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        # Write your code here

        if length ==  0:
            return None

        ans = [0] * length

        for i in range(len(updates)):
            ans[updates[i][0]] += updates[i][2]
            if updates[i][1] < length - 1:
                ans[updates[i][1] + 1] -= updates[i][2]

        sum = 0
        for i in range(length):
            sum += ans[i]
            ans[i] = sum
        return ans

if __name__ == '__main__':
    so = Solution()
    print so.getModifiedArray(5, [
[1,  3,  2],
[2,  4,  3],
[0,  2, -2]
])