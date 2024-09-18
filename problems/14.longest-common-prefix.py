#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i, c in enumerate(strs[0]):
            for s in strs:
                if i == len(s) or s[i] != c:
                    return result
            result += c
        return result

# @lc code=end
