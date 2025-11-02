#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:

        def compute(n: int):
            res = 0 
            while n: 
                digit = n % 10
                res += digit * digit
                n = n // 10

            return res
        
        slow = compute(n)
        fast = compute(compute(n))

        while slow != fast:
            if slow == 1:
                return True
            
            slow = compute(slow)
            fast = compute(compute(fast))

        return slow == 1

# @lc code=end
if __name__ == "__main__":
    s = Solution()
