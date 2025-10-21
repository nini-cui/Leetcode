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
        
        s_len = len(s)
        max_s = s[0]

        def expand_centre(left, right):
            while left >= 0 and right < s_len and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        for i in range(s_len-1):
            odd = expand_centre(i, i)
            even = expand_centre(i, i+1)

            if len(max_s) < len(odd):
                max_s = odd

            if len(max_s) < len(even):
                max_s = even

# @lc code=end
if __name__ == "__main__":
    palidrome = Solution() 
    res = palidrome.longestPalindrome("abba")