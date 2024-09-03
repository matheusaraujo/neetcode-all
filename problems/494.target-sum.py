#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(i, currSum) -> int:
            if i == len(nums): return 1 if currSum == target else 0
            if (i, currSum) in memo: return memo[(i, currSum)]

            memo[(i, currSum)] = \
                backtrack(i + 1, currSum + nums[i]) + \
                backtrack(i + 1, currSum - nums[i])

            return memo[(i, currSum)]

        return backtrack(0, 0)


# @lc code=end

