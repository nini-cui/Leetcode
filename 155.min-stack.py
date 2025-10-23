#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.res = []

    def push(self, val: int) -> None:
        self.res.append(val)

    def pop(self) -> None:
        del self.res[-1]

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        return min(self.res)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

