#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []

        def dfs(i: int):
            if i >= len(nums):
                result.append(subset.copy())
            else:
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
                dfs(i + 1)
        dfs(0)
        return result

# @lc code=end

