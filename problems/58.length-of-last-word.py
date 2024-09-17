#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for c in s[::-1]:
            if c == " ":
                if length >= 1: return length
            else: length += 1
        return length


# @lc code=end

