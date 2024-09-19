#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        triangle = [[1]]
        for i in range(1, numRows):
            prevRow, newRow = triangle[-1], [1, 1]
            for j in range(1, len(prevRow)):
                newRow.insert(-1, prevRow[j-1] + prevRow[j])
            triangle.append(newRow)
        return triangle


# @lc code=end

