#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[:])
            else:
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                backtrack(i + 1, subset)

        backtrack(0, [])
        return result

# @lc code=end

