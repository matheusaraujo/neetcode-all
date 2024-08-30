#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, slow2, fast = nums[0], 0, nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

# @lc code=end

