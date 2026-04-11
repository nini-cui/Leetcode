#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = len(s)
        max_str = ""
        for i in range(max_len):
            left = i
            right = i + 1
            cur_max_str = ""
            while right < max_len:
                cur_str = s[left: right]
                idx = cur_str.find(s[right])
                if len(cur_str) > len(cur_max_str):
                    cur_max_str = cur_str
                    right += 1
                
                if idx != -1:
                    if len(cur_max_str) > len(max_str):
                        max_str = cur_max_str
                    break

        return max_str


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))