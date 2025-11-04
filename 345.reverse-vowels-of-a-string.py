#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
"""
Use 2 while loops like this:

while start < end:
    # Move the start pointer towards the end until it points to a vowel.
    while start < end and vowels.find(word[start]) == -1:
        start += 1
    
    # Move the end pointer towards the start until it points to a vowel.
    while start < end and vowels.find(word[end]) == -1:
        end -= 1

finding index syntax: lst.find(val)
"""
# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = ['a', 'e', 'i', 'o', 'u']
        vowels = "aeiouAEIOU"
        s = list(s)

        left = 0 
        right = len(s) - 1

        while left < right:
            while left < right and vowels.find(s[left]) == -1:
                left += 1

            while left < right and vowels.find(s[right]) == -1:
                right -= 1

            s[start], s[end] = s[end], s[start]
            
            # Move the pointers towards each other for the next iteration.
            start += 1
            end -= 1

        # while left < right:
        #     if (s[left].lower() in vowels) and (s[right].lower() in vowels):
        #         s[left], s[right] = s[right], s[left]

        #         left += 1
        #         right -= 1
        #     elif (s[left].lower() in vowels) and (s[right].lower() not in vowels):
        #         right -= 1
        #     elif (s[right].lower() in vowels) and (s[left].lower() not in vowels):
        #         left += 1
        #     else:
        #         left += 1
        #         right -= 1

        return "".join(s)
        
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    res = s.reverseVowels("cdfkl")
    # res = s.reverseVowels("IceCreAm")
    print(res)
