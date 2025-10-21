#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# checking the current i and previous i
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        res = set()
        nums = sorted(nums)
        for i in range(nums_len-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = nums_len - 1

            while k != j:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else: 
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    if nums[k] == nums[k-1]:
                        k -= 1
                    elif nums[j] == nums[j-1]:
                        j += 1
                    else:
                        k -= 1
        
        print([list(ele) for ele in res])
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.threeSum([-2,0,1,1,2])
    print(res)
