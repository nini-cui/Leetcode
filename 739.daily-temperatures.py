#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_len = len(temperatures)
        stack = []
        ans = [0] * temp_len

        for idx in range(temp_len):
            while stack and (temperatures[idx] > temperatures[stack[-1]]):
                ans[stack[-1]] = idx - stack[-1]
                stack.pop()
            else:
                stack.append(idx)

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.dailyTemperatures([30,40,50,60])
