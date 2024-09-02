#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        total = result = 0

        for i in range(len(gas)):
            total = total + gas[i] - cost[i]
            if total < 0: total, result = 0, i + 1

        return result

# @lc code=end

