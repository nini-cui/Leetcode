#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums)-1, 2):
            if sorted_nums[i] != sorted_nums[i+1]:
                return sorted_nums[i]
            
        return sorted_nums[-1]

        # res_dict = defaultdict(int)
        # for i in nums:
        #     res_dict[i] += 1

        # for k, v in res_dict.items():
        #     if v == 1:
        #         return k
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([4,1,2,1,2,3,3]))

