#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m != 0 and n != 0:
            if nums1[m-1] > nums2[n-1]:
               nums1[m+n-1] = nums1[m-1]
               m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1

        if n != 0:
            nums1[0:n] = nums2[:n]

        return nums1
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    print(res)