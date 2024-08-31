#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(x: float, n: int):
            if x == 0: return 0
            if n == 0: return 1
            result = solve(x * x, n // 2)
            return x * result if n % 2 else result

        result = solve(x, abs(n))
        return result if n > 0 else 1 / result

# @lc code=end

