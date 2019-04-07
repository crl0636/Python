class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost:
            return -1

        if sum(gas) < sum(cost):
            return -1

        diff = 0
        idx = 0

        for i in range(len(gas)):
            if gas[i] + diff < cost[i]:
                idx = i + 1
                diff = 0
            else:
                diff += gas[i] - cost[i]
        return idx