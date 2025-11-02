#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            ele = s[left]
            s[left] = s[right]
            s[right] = ele

            left += 1
            right -= 1
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.reverseString(["h","e","l","l","o"])