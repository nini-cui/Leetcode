#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str
    
        # iteration
        # if s==s[::-1]: 
        #     return s
        # left = self.longestPalindrome(s[1:])
        # right = self.longestPalindrome(s[:-1])

        # if len(left)>len(right):
        #     return left
        # else:
        #     return right

        # brute force
        # s_len = len(s)
        
        # max_s = ""
        # for i in range(s_len-1):
        #     for j in range(i+1, s_len):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             if (j+1-i) > len(max_s):
        #                 max_s = s[i:j+1]

        # if len(max_s) > 1:
        #     return max_s
            
        # return s[0]

# @lc code=end
if __name__ == "__main__":
    palidrome = Solution() 
    res = palidrome.longestPalindrome("babad")
    print(res)