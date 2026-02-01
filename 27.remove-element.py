#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        left = right = 0

        while right < nums_len:
            if nums[right] == val:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1

        return len(nums[:left])
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.removeElement([0,1,2,2,3,0,4,2], 3)
    print(res)