#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # use strip, after split check if list is empty
        # print(s.strip())
        # split_res = [item for item in s.split(" ") if item != ""]
        # return len(split_res[-1])
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("   fly me   to   the moon  "))
