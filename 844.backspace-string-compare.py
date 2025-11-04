#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert_string(s, stack):
            for i in s:
                if stack and i == '#':
                    stack.pop()    
                elif not stack and i == '#':
                    continue
                else:
                    stack.append(i)

            return "".join(stack) 

        return convert_string(s, []) == convert_string(t, [])

# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.backspaceCompare("a##c", "#a#c")
    print(res)