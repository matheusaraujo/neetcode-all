#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and gates
#

# @lc code=start
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue, visited = deque(), set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r, c))
        def visit(r, c):
            if (
                r not in range(rows) or
                c not in range(cols) or
                (r, c) in visited or
                grid[r][c] == -1
            ): return
            visited.add((r, c))
            queue.append((r, c))

        dist = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                visit(r + 1, c)
                visit(r - 1, c)
                visit(r, c + 1)
                visit(r, c - 1)
            dist += 1




# @lc code=end

