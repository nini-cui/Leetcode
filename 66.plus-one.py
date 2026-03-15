#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List
        
# @lc code=end
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0

        new_number = [0] * (n + 1)
        new_number[0] = 1

        return new_number

        # if digits is None or len(digits) == 0:
        #     return []

        # digits_str = ""
        # res = []
        # for i in range(len(digits)):
        #     digits_str += str(digits[i])
        
        # plus_one = str(int(digits_str) + 1)

        # for digit in plus_one:
        #     res.append(int(digit))
        
        # return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([8,9,9]))


        
