#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+": stack.append(stack.pop() + stack.pop())
            elif t == "-": stack.append(-stack.pop() + stack.pop())
            elif t == "*": stack.append(stack.pop() * stack.pop())
            elif t == "/": stack.append(int(1 / (stack.pop()) * stack.pop()))
            else: stack.append(int(t))
        return stack[0]

# @lc code=end

