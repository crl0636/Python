class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here

        candidate = 0

        for i in range(n):
            if Celebrity.knowns(candidate, i):
                candidate = i

        for j in range(n):
            if j != candidate:
                if Celebrity.knowns(candidate, j) ||  not Celebrity.knowns(j, candidate):
                    return 1

        return candidate
