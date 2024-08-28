#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
class Solution:
    def createAdjList(self, points: List[List[int]]) -> dict:
        n = len(points)
        adj = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        return adj

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = self.createAdjList(points)

        result, visited, minHeap = 0, set(), [[0, 0]]

        while len(visited) < len(points):
            cost, nextPoint = heapq.heappop(minHeap)
            if nextPoint in visited: continue

            result += cost
            visited.add(nextPoint)

            for nextCost, neighbor in adj[nextPoint]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, [nextCost, neighbor])

        return result


# @lc code=end

