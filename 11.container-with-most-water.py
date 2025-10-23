#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        height_len = len(height)
        max_area = 0
        i = 0
        j = height_len - 1

        while i < j:
            max_area = max(max_area, (j-1)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                right -= 1

        return max_area
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    max_area = s.maxArea([1, 2, 1])
    print(max_area)
