#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import string
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans('', '', string.punctuation + ' ')
        clean_text = s.translate(translator).lower()
        print(clean_text)
        print(clean_text[::-1])
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.isPalindrome("A man, a plan, a canal: Panama")
