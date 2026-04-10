#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
from collections import defaultdict
# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        res_dict = defaultdict(int)

        for i in s:
            res_dict[i] += 1

        for k, v in res_dict.items():
            if v == 1:
                return s.find(k)
        
        return -1
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.firstUniqChar("aabb"))
    # test
