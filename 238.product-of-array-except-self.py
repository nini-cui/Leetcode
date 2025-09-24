#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        # output: [1, 1, 1, 1]
        # input: [2, 3, 4, 5]
        # expected: [1, 2, 6, 24
        # res: [60, 40, 30, 24]
        # 1*1, 1*2, 1*2*3, 1*2*3*4
        left = right = 1

        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output

            
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.productExceptSelf([2, 3, 4, 5])
