#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        I want:
            1. the outer loop length has to be less than hLen
            2. the index has to increase by 1 if the current subtring doesnt match
            3. while in that specific iter, I want to continuous to compare chars: compare the 
            current val with the max len
        """

        # hLen = len(haystack)
        # nLen = len(needle)

        # # init i before the iteration starts
        # i = 0    

        # while i < hLen:
        #     j = i
        #     nIndex = 0

        #     while j < hLen and nIndex < nLen and haystack[j] == needle[nIndex]:
        #         j += 1
        #         nIndex += 1

        #     if nIndex == nLen:
        #         return i
            
        #     i += 1

        # return -1

        # this method using string comparasion
        # if haystack == needle:
        #     return 0
        
        # needle_len = len(needle)
        # haystack_len = len(haystack)

        # left = 0
        
        # while left <= (haystack_len-needle_len):
        #     haystack_res = haystack[left:left+needle_len]
        #     if haystack_res == needle:
        #         return left
        #     else:
        #         left += 1

        # return -1
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.strStr("leetcode", "leeto")
    print(res)
