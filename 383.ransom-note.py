#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
from collections import defaultdict
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # method 2: deduct values in ransomNote
        
        ransomNote_dict = defaultdict(int)
        magazine_dict = defaultdict(int)
        for i in range(len(ransomNote)):
            ransomNote_dict[ransomNote[i]] += 1

        for i in range(len(magazine)):
            magazine_dict[magazine[i]] += 1

        for k, _ in ransomNote_dict.items():
            if ransomNote_dict[k] > magazine_dict[k]:
                return False
            
        return True
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.canConstruct("aa", "ab")