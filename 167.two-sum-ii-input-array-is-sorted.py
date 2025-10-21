#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
# get index of a list: lst.index(<val>)
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            target_ele = target - numbers[i]
            if target_ele in numbers:
                idx = numbers.index(target_ele)
                if i != idx:
                    return [i+1, idx+1]
# @lc code=end
if __name__ == "__main__":
    solution = Solution() 
    res = solution.twoSum([2,7,11,15], 9)   
    print(res)
