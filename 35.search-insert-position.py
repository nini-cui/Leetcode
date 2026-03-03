#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right >= 0:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[left] < target < nums[right]:
                left += 1
                right -= 1
            elif nums[left] > target:
                return left
            elif nums[right] < target:
                return right + 1
            
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.searchInsert([1, 3, 5, 6], 7)
