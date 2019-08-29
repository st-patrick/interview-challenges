#Input: "banana"
#Output: "anana"

#Input: "million"
#Output: "illi"
class Solution: 
    def longestPalindrome(self, s):
      pivot = 0.5
      longest = 1 #because every character is a palindrome in itself
      left = ''
      for c in s:
        # optimization: abort loop if longest palindrome is alrady longer than any new one could be
        
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
