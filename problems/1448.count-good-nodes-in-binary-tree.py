#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], maxVal: int) -> int:
            if not node: return 0
            return (1 if node.val >= maxVal else 0) + \
                dfs(node.left, max(node.val, maxVal)) + \
                dfs(node.right, max(node.val, maxVal))

        return dfs(root, root.val)

# @lc code=end

