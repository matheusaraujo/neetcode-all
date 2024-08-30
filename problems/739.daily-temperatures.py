#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result, stack = [0] * len(temperatures), []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                st, si = stack.pop()
                result[si] = i - si
            stack.append((t, i))

        return result

# @lc code=end

