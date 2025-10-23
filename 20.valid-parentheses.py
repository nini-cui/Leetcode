#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if st:
                if self.isPair(cur=i, last=st[-1]):
                   st.pop()
                   continue
            st.append(i)

        return not st

    def isPair(self, cur, last):
        return (cur == ')' and last == '(') or (cur == '}' and last == '{') or (cur == ']' and last == '[')

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.isValid("([])")
    print(res)
