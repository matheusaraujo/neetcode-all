#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        self.ensureHeapSize()

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        self.ensureHeapSize()
        return self.minHeap[0]

    def ensureHeapSize(self):
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

