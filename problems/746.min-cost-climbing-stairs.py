#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])
        return min(cost[len(cost)-1], cost[len(cost)-2])

# @lc code=end

