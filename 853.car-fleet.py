#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
from typing import List
# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        
        for p, s in sorted(cars):
            print(f'p is {p}')
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])