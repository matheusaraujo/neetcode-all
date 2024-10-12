#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        tmp, result = "", ""

        for c in num:
            if tmp == "" or tmp[0] != c: tmp = c
            else: tmp += c

            if len(tmp) == 3 and (result == "" or tmp[0] > result[0]):
                result = tmp

        return result
    # def largestGoodInteger(self, num: str) -> str:
    #     result = ""
    #     for i in range(len(num) - 2):
    #         if num[i] == num[i+1] == num[i+2]:
    #             result = max(result, num[i]*3)
    #     return result

# @lc code=end

