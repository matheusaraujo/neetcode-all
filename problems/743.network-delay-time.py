#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap, visited, t = [(0, k)], set(), 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited: continue

            visited.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visited) == n else -1

# @lc code=end

