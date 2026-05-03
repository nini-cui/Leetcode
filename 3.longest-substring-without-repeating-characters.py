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
        if max_len < 2:
            return len(s)

        for i in range(max_len):
            left = i
            right = left + 1
            cur_max_str = s[left]

            while right <= max_len:
                cur_str = s[left:right]
                if len(cur_str) > len(cur_max_str):
                    cur_max_str = cur_str

                if right == max_len:
                    break

                if s[right] in cur_str:
                    break

                right += 1

            if len(cur_max_str) > len(max_str):
                max_str = cur_max_str

        return len(max_str)
 

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("au"))