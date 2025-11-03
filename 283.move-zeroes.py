#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

        # left = 0
        # right = 1

        # nums_len = len(nums)

        # while right < nums_len:
        #     if nums[left] == 0 and nums[right] != 0:
        #         nums[right], nums[left] = nums[left], nums[right]
        #         left += 1
        #         right += 1
        #     elif nums[left] == 0 and nums[right] == 0:
        #         right += 1
        #     else:
        #         left += 1
        #         right += 1

        # return nums
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.moveZeroes([0,1,0,3,12])
    print(res)
