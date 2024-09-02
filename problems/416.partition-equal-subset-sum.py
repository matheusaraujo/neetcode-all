#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) -1, -1, -1):
            nextDp = set()
            for t in dp:
                if t + nums[i] == target: return True
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        return False

# @lc code=end

