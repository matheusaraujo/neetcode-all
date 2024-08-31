#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        elif x > 0: y = int("".join(reversed(list(str(x)))))
        else: y = int("".join(reversed(list(str(x)[1:])))) * (-1)

        return y if (-2)**31 < y < 2**31-1 else 0

# @lc code=end

