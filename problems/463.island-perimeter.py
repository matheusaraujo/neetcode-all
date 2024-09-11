#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0: result += 1
                    if i == m - 1 or grid[i + 1][j] == 0: result +=1
                    if j == 0 or grid[i][j - 1] == 0: result += 1
                    if j == n - 1 or grid[i][j + 1] == 0: result += 1
        return result

# @lc code=end

