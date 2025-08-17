#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List

# @lc code=start
class Solution:
    def words_with_max_length(self, words: List[str], length: int):
        res = []
        len_sum = 0
        for word in words:
            len_sum += len(word)
            if len_sum <= length:
                res.append(word)
                len_sum += 1
            else:
                break

        return res
# @lc code=end
if __name__ == "__main__":
    words = ["algorithm", "banana", "catastrophe", "dog", "elephant", "fibonacci", "goat", "hypothesis", "iceberg", "juxtapose"]
    length = 15
    sol = Solution()
    res = sol.words_with_max_length(words, length)
    print(res)
