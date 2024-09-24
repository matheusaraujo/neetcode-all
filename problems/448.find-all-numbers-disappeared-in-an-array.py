#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # return list(set(range(1, len(nums) + 1)) - set(nums))
        result = set(range(1, len(nums) + 1))
        for num in nums:
            if num in result: result.remove(num)
        return list(result)

# @lc code=end

