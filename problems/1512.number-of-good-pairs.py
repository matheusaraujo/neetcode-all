#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = defaultdict(int
        result = 0

        for num in nums:
            result += frequency[num]
            frequency[num] += 1

        return result



# @lc code=end

