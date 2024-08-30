#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        empty = ListNode(0, head)
        groupPrev = empty

        while True:
            kth = self.__getKth(groupPrev, k)
            if not kth: break

            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev, curr = curr, tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return empty.next

    def __getKth(self, curr, k):
        while curr and k > 0:
            curr, k = curr.next, k - 1
        return curr



# @lc code=end

